class FuncDeclVisitor(c_ast.NodeVisitor):
    """Visitor class for function declarations
    """

    def __init__(self):
        """Constructor of FuncDeclVisitor
        """

    def visit_Decl(self, node) -> None:
        """_summary_

        Args:
            node (_type_): node of ast
        """
        #if hasattr(node, 'decl'):
        #   print('%s at %s' % (node.decl.name, node.decl.coord))
        #if hasattr(node.type, 'declname'):
        #    print(f"Func Name: {node.type.declname} at {node.coord}")
        #else:
        #    print(node)
        if node.name is not None:
           pass# ret.var_types[decl.name] = decl.type
        if isinstance(node.type, c_ast.FuncDecl):
            self.visit(node.type)
            #print(node.name)
            func_name = node.name
            func_coord = node.coord
            func_type = node.storage
            node_type = node.type
            while(not isinstance(node_type, c_ast.IdentifierType)):
                if isinstance(node_type, c_ast.PtrDecl):
                    func_type.append("Ptr")
                node_type = node_type.type
            func_type = func_type + node_type.names
            #if isinstance(node.type.type.type, c_ast.IdentifierType):
            #    func_type = node.type.type.type.names
            #elif isinstance(node.type.type, c_ast.PtrDecl):
            #    func_type = node.type.type.type.type.names
            #    func_type.append("Ptr")
            print(f"Func Name: {func_name} at {func_coord} of type: {func_type}")

