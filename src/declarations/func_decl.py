
class FuncDecl():
    def __init__(self, func_name, func_coord, func_type, func_storage):
        """Constructor of FuncDeclVisitor
        """
        self.func_name = func_name
        self.func_coord = func_coord
        self.func_type = func_type
        self.func_storage = func_storage