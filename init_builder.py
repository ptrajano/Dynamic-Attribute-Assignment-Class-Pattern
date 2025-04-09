
class A:
    def __init__(self, a, b, c):
        (lambda local: self.__dict__.update({name: local[name] for 
                                             name in self.__init__.__code__.co_varnames[1:]}))(locals())
        
        


obj = A(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)