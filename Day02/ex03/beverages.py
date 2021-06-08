#!/usr/bin/env python3


class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30

    def __str__(self):
        return "name : {0}\nprice : {1}\ndescription : {2}".format(
            self.name, self.price, self.description()
        )

    def description(self):
        return "Just some hot water in a cup."


class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        self.name = "tea"
        self.price = 0.30


class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == "__main__":
    mug = Coffee()
    cuppa = Tea()
    choc = Chocolate()
    caf = Cappuccino()
    for instance in [mug, cuppa, choc, caf]:
        print(instance)
