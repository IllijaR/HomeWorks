from random import choice


class Mathobj:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def sum(self):
        return self.__a + self.__b

    def minus(self):
        return self.__a - self.__b

    def prod(self):
        return self.__a * self.__b

    def divide(self):
        if self.__b != 0:
            return self.__a / self.__b
        else:
            return "If you type zero - you are not a hero! "

    def __getrandoperation(self):
        list_oper = [self.sum, self.prod, self.minus, self.divide]
        return choice(list_oper)()

    def __str__(self):
        return str(self.__getrandoperation())


shifrator = Mathobj(10, 0)
print(shifrator)
