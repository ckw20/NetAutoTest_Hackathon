import logging, json, ast
from abc import ABC, abstractmethod
from ..code_generator.task import Task
import builtins

logger = logging.getLogger(__name__)

class Entry(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def corpus(self):
        raise NotImplementedError("Entry.corpus() is not implemented yet")

class APIDocEntry(Entry):
    def __init__(self, func: dict):
        super().__init__()
        self.func = func
        if "method_name" not in self.func.keys():
            # logging.warning("WARNING in DocEntry.__init__(): Currently no support on class")
            self.type = "class"
        else:
            self.type = "func"
            self.method_name: str = self.func["method_name"]
            # self.func_type = self.func["func_type"]
            self.description = self.func.get("description", "WARNNING: No Description")
            self.parameters = self.func.get("parameters", [])
            self.kwargs = self.func.get("kwargs", None)
            self.return_ = self.func.get("return", None)
            self.return_type = self.func.get("return_type", None)
            self.example = self.func.get("example", None)
            self.conflicts = self.func.get("conflicts", None)
            if self.conflicts is not None and len(self.conflicts) > 0: pass

    # TODO: need better corpus for retrieval
    def corpus(self):
        corpus = self.method_name + ': ' + self.description
        # for parameter in self.parameters:
        #     try:
        #         corpus += ". " + parameter["description"]
        #     except Exception as e:
        #         logging.warning(f"WARNING in DocEntry.gen_corpus(): {e}")
        return corpus

    def to_dict_prompt(self):
        return {
            "method_name": self.method_name.split('.')[-1] if '.' in self.method_name else self.method_name,
            "description": self.description,
            "parameters": [{
                "parameter_name": para["name"],
                "parameter_type": para["type"],
                "description": para["description"],
                "default": None if para["default"] == "not_found" else para["default"],
                "range_or_options": None if para["range_or_options"] == "not_found" else para["range_or_options"],
            } for para in self.parameters],
            "return": self.return_,
            "return_type": self.return_type,
        }

    def to_prompt(self):
        return json.dumps(self.to_dict_prompt(), ensure_ascii=False)

class ExampleEntry(Entry):
    def __init__(self, example: Task):
        super().__init__()
        self.example = example

    def corpus(self):
        return self.example.to_example_corpus()

    def to_prompt(self):
        return self.example.to_prompt()

    def extract_api(self, module: str = 'TesterLibrary.base'):
        code = self.example.result_code
        try: tree = ast.parse(code)
        except SyntaxError: return []
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

        if not import_visitor.testerlib_wildcard: return []
        # builtin_names = set(dir(__builtins__))
        builtin_names = set(dir(builtins)) | {'None', 'True', 'False', 'Ellipsis', 'NotImplemented'}
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

class ExperienceEntry(Entry):
    def __init__(self, experience: dict):
        super().__init__()
        self.experience = experience
        self.run_info = experience.get("run_info", None)
        self.error_info = experience.get("error_info", None)
        self.suggestion = experience.get("suggestion", None)
        self.code = experience.get("code", None)

    def to_dict(self):
        return {
            "run_info": self.run_info,
            "error_info": self.error_info,
            "suggestion": self.suggestion,
            "code": self.code
        }

    def corpus(self):
        return json.dumps({
            'error_info': self.error_info
            # 'detailed run info': self.run_info
        }, indent=4, ensure_ascii=False)