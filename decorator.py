class Coffee:
    def cost(self):
        return 5

class SugarDecorator:
    def __init__(self, coffee):
        self.__coffee = coffee

    def cost(self):
        return self.__coffee.cost() +2

class MilkDecorator:
    def __init__(self, coffee):
        self.__coffee = coffee

    def cost(self):
        return self.__coffee.cost() +4

a = Coffee()
print(a.cost())

b = SugarDecorator(a)
print(b.cost())

c = SugarDecorator(b)
print(c.cost())