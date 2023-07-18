from pycparser import c_ast
from src.declarations.func_decl import FuncDecl

class FuncDeclVisitor(c_ast.NodeVisitor):
    """Visitor class for function declarations
    """

    def __init__(self):
        """Constructor of FuncDeclVisitor
        """
        self.func_decl = {}

    def visit_Decl(self, node) -> None:
        """_summary_

        Args:
            node (_type_): node of ast
        """
        if isinstance(node.type, c_ast.FuncDecl):
            self.visit(node.type)
            #print(node.name)
            func_name = node.name
            func_coord = node.coord
            func_type = []
            func_storage = node.storage
            node_type = node.type
            while(not isinstance(node_type, c_ast.IdentifierType)):
                if isinstance(node_type, c_ast.PtrDecl):
                    func_type.append("Ptr")
                node_type = node_type.type
            func_type = func_type + node_type.names

            func_decl = FuncDecl(func_name, func_coord, func_type, func_storage)
            self.func_decl[func_coord] = func_decl

            print(f"Func Name: {func_name} at {func_coord} with range: {func_storage} of type: {func_type} ")

