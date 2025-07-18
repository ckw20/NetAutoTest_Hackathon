import os
import ast
import json
import argparse
from typing import Dict, List, Optional

class FunctionExtractor:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.functions = {}
        self.imports = {}
        self.current_class = None
        self.current_file = None
        self.lines = []

    def process_file(self, file_path: str):
        self.current_file = file_path
        self.imports = {}
        self.current_class = None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
        
        try:
            tree = ast.parse(''.join(self.lines), filename=file_path)
            self.visit(tree)
        except SyntaxError as e:
            print(f"Syntax error in {file_path}: {e}")

    def visit(self, node):
        """Dispatch to the appropriate visitor method."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Called if no explicit visitor method exists."""
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)
            elif isinstance(value, ast.AST):
                self.visit(value)

    def visit_Import(self, node):
        for alias in node.names:
            self.imports[alias.asname or alias.name] = alias.name

    def visit_ImportFrom(self, node):
        module = node.module or ""
        level = node.level  # For relative imports
        
        # Handle relative imports
        if level > 0:
            rel_path = os.path.relpath(os.path.dirname(self.current_file), start=self.root_dir)
            module_parts = rel_path.split(os.sep)
            module_prefix = ".".join(module_parts[:level-1]) if level > 1 else ""
            module = f"{module_prefix}.{module}" if module_prefix else module
        
        for alias in node.names:
            full_name = f"{module}.{alias.name}" if module else alias.name
            self.imports[alias.asname or alias.name] = full_name

    def visit_ClassDef(self, node):
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = None

    def visit_FunctionDef(self, node):
        # Get function source code
        start_line = node.lineno
        end_line = node.end_lineno
        
        # Include decorators
        if node.decorator_list:
            decorator_start = min(d.lineno for d in node.decorator_list)
            start_line = min(start_line, decorator_start)
        
        source_code = ''.join(self.lines[start_line-1:end_line])
        
        # Get docstring
        docstring = ast.get_docstring(node) or ""
        
        # Get dependencies
        dependencies = set()
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                dep_name = self.resolve_call(child)
                if dep_name and dep_name.startswith(self.root_dir.replace(os.sep, '.')):
                    dependencies.add(dep_name)
        
        # Get fully qualified name
        fqn = self.get_fqn(node.name)
        
        # Store function info
        self.functions[fqn] = {
            "fqn": fqn,
            "source_code": source_code.strip(),
            "docstring": docstring.strip(),
            "dependencies": list(dependencies)
        }
        
        self.generic_visit(node)

    def get_fqn(self, function_name: str) -> str:
        """Construct fully qualified name"""
        # Get relative path from root directory
        rel_path = os.path.relpath(self.current_file, start=self.root_dir)
        # Convert to module path
        module = rel_path.replace('.py', '').replace(os.sep, '.')
        # Add class name if in a class
        if self.current_class:
            return f"{self.root_dir.replace(os.sep, '.')}.{module}.{self.current_class}.{function_name}"
        return f"{self.root_dir.replace(os.sep, '.')}.{module}.{function_name}"

    def resolve_call(self, node: ast.Call) -> Optional[str]:
        """Resolve a function call to its FQN"""
        if isinstance(node.func, ast.Name):
            # Direct function call (e.g. func())
            name = node.func.id
            if name in self.imports:
                imported = self.imports[name]
                if imported.startswith(self.root_dir.replace(os.sep, '.')):
                    return imported
            # Check if it's a function in current module
            elif self.current_class:
                return f"{self.get_fqn('')}.{name}"
            else:
                return f"{self.get_fqn('').rsplit('.', 1)[0]}.{name}"
                
        elif isinstance(node.func, ast.Attribute):
            # Method or module function (e.g. obj.method())
            parts = []
            current = node.func
            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value
                
            if isinstance(current, ast.Name):
                base_name = current.id
                parts.reverse()
                
                # Check imports
                if base_name in self.imports:
                    base_import = self.imports[base_name]
                    if base_import.startswith(self.root_dir.replace(os.sep, '.')):
                        return f"{base_import}.{'.'.join(parts)}"
                
                # Check if it's a method in current class
                if self.current_class and base_name == self.current_class:
                    class_fqn = self.get_fqn('').rsplit('.', 1)[0]
                    return f"{class_fqn}.{'.'.join(parts)}"
                
        return None

def find_py_files(directory: str) -> List[str]:
    """Find all .py files in directory"""
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                py_files.append(os.path.join(root, file))
    return py_files

def extract_functions(root_dir: str) -> Dict[str, dict]:
    """Extract all functions from directory"""
    extractor = FunctionExtractor(root_dir)
    py_files = find_py_files(root_dir)
    
    for file_path in py_files:
        extractor.process_file(file_path)
    
    return extractor.functions

def main():
    parser = argparse.ArgumentParser(description='Extract functions from Python codebase')
    parser.add_argument('-d', '--directory', help='Root directory of the Python project')
    parser.add_argument('-o', '--output', default='function_info.json', help='Output JSON file path')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        return

    functions = extract_functions(args.directory)
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(list(functions.values()), f, indent=2, ensure_ascii=False)
    
    print(f"Extracted {len(functions)} functions to {args.output}")

if __name__ == '__main__':
    main()