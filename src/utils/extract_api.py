import ast

def get_testerlib_base_functions(code, module):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    class ImportVisitor(ast.NodeVisitor):
        def __init__(self):
            self.explicit_imports = set()
            self.testerlib_wildcard = False

        def visit_Import(self, node):
            for alias in node.names:
                name = alias.asname or alias.name
                self.explicit_imports.add(name)
            self.generic_visit(node)

        def visit_ImportFrom(self, node):
            if node.module == module:
                for alias in node.names:
                    if alias.name == '*':
                        self.testerlib_wildcard = True
            else:
                for alias in node.names:
                    if alias.name != '*':
                        imported_name = alias.asname or alias.name
                        self.explicit_imports.add(imported_name)
            self.generic_visit(node)

    import_visitor = ImportVisitor()
    import_visitor.visit(tree)

    if not import_visitor.testerlib_wildcard:
        return []

    builtin_names = set(dir(__builtins__))
    # print(builtin_names)

    class FunctionCallVisitor(ast.NodeVisitor):
        def __init__(self, explicit_imports, builtin_names):
            self.explicit_imports = explicit_imports
            self.builtin_names = builtin_names
            self.functions = set()

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if (func_name not in self.explicit_imports and
                    func_name not in self.builtin_names):
                    self.functions.add(func_name)
            self.generic_visit(node)

    call_visitor = FunctionCallVisitor(import_visitor.explicit_imports, builtin_names)
    call_visitor.visit(tree)

    return sorted(call_visitor.functions)

if __name__ == "__main__":
    path = '/root/workspace/NetAutoTest/data/ref_projects/cepri-dev-new/Testcase/tc_6_7_6/main.py'
    code = open(path, 'r').read()
    functions = get_testerlib_base_functions(code, 'TesterLibrary.base')
    print(functions, len(functions))