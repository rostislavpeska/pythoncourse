# SINGLETON

class Singleton(object):
    _instance = None
    def __new__(class_):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance

class DBClient(Singleton):
    def print_something(self):
        print("something")

x = DBClient()
y = DBClient()
z = DBClient()

# FACTORY

class Circle:
    pass

class Square:
    pass

class Oval:
    pass

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str):
        if shape_type == "circle":
            Circle()
        elif shape_type == "square":
            Square()
        else:
            Oval()

circle = ShapeFactory.create_shape("circle")

# BUILDER

class Pizza:
    def __init__(self):
        self.ketchup = None
        self.salami = None
        self.ham = None
        self.cheese = None

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def with_ketchup(self):
        self.pizza.ketchup = True
        return self

    def with_cheese(self):
        self.pizza.cheese = True
        return self

    def with_salami(self):
        self.pizza.salami = True
        return self

    def with_ham(self):
        self.pizza.ham = True
        return self

    def build(self):
        return self.pizza

builder = PizzaBuilder()
cheese_pizza = builder.with_cheese().with_ketchup().build()
everything_pizza = builder.with_cheese().with_ketchup().with_salami().with_ham().build()

