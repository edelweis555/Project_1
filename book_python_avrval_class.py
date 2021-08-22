class AvrVal:
    
    a = 'Переменная класса, Атрибут класса, Постоянный атрибут'
    b = 1
    
    #______----
    
    @staticmethod
    def ex_static_method():
        print("static method")
    @classmethod
    def ex_class_method(cls):
        print("class method")
    def ex_method(self):
        print("method")
    
    def __init__(self, char: str='', var: float=0, cnt: int=0, res: float=0) -> None:
        self.char = char
        self.var = var
        self.cnt = cnt
        self.res = res
    
    def input_char(self) -> None:
        print('Input digital Var:')
        print('YES press "y" or NOT press "n"')
        self.char = input()
        while self.char != 'n':
            self.var += float(input())
            self.cnt +=1
            print('Continue?')
            print('YES press "y" or NOT press "n"')
            self.char = input()
    
    def averages(self) -> None:
        self.res = self.var/self.cnt
        
        
    def __repr__(self) -> str:
        return str(self.res)
