class Foo:
    def __init__(self, x=None):
        self._x = x


    # Para Retornar o valor precisa de um propety retornavel 
    @property
    def x(self):
        return self._x or 0
    
    # Para alterar o valor eu preciso definir um valor para ela
    @x.setter
    def x(self, value):
        self._x += value
    
    # Para Deletar preciso passar o parametro
    @x.deleter
    def x(self):
        self._x = 0 


foo = Foo(10)        
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)