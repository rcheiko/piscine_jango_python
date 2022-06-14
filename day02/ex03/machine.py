import random
import beverages

class CoffeeMachine:

    machine_repair = 0

    def __init__(self):
        pass

    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90
        desc = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        CoffeeMachine.machine_repair = 10

    def serve(self, drink):
        if CoffeeMachine.machine_repair <= 0:
            raise CoffeeMachine.BrokenMachineException 
        else:
            choice = []
            choice.append(drink)
            choice.append(CoffeeMachine.EmptyCup)
            rand = random.choice(choice)
            CoffeeMachine.machine_repair -= 1
            return rand()

if __name__ == '__main__':

    machine = CoffeeMachine()

    machine.repair()

    choice = []
    choice.append(beverages.Coffee)
    choice.append(beverages.Tea)
    choice.append(beverages.Chocolate)
    choice.append(beverages.Cappuccino)

    try:
        for i in range(1,12):
            rand = random.choice(choice)
            print(machine.serve(rand))
            print('')
    except CoffeeMachine.BrokenMachineException as event:
        print(event)


    machine.repair()



    try:
        for i in range(1,15):
            rand = random.choice(choice)
            print(machine.serve(rand))
            print('')
    except CoffeeMachine.BrokenMachineException as event:
        print(event)
