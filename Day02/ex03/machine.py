#!/usr/bin/env python3

import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    class EmptyCup(HotBeverage):
        prise = 0.90
        name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, say="This coffee machine has to be repaired."):
            Exception.__init__(self, say)

    def __init__(self):
        self.total_served = 0
        self.served = 0

    def serve(self, drink):
        if self.served < 10:
            if random.randint(1, 2) == 1:
                result = drink()
            else:
                result = self.EmptyCup()
            self.total_served += 1
            self.served += 1
            return result
        else:
            raise self.BrokenMachineException()

    def repair(self):
        self.served = 0


if __name__ == "__main__":

    def use_machine(machine, times):
        drinklst = [Coffee, Tea, Chocolate, Cappuccino]
        for _ in range(times):
            try:
                print(machine.serve(random.choice(drinklst)))
            except Exception as e:
                print(e)

    machine = CoffeeMachine()
    use_machine(machine, times=12)
    machine.repair()
    use_machine(machine, times=12)
