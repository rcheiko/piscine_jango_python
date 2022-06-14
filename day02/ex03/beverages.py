class HotBeverage:
    name = "hot beverage"
    price = 0.30
    desc = "Just some hot water in a cup."
    def description(self):
        return(self.desc)

    def __str__(self):
        string = "name : " + self.name + "\n"
        a = "price : "
        b = str(self.price) + "\n"
        c = self.desc
        return string + a + b + c


class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    desc = "A coffee, to stay awake."

class Tea(HotBeverage):
    name = "tea"

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    desc = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    desc = "Un po’ di Italia nella sua tazza!"

if __name__ == '__main__':
    h = HotBeverage()  ### DEFAULT
    print(h.__str__())

    print('')

    coff = Coffee()     ### COFFEE
    print(coff.__str__())

    print('')

    tea = Tea()         ### TEA
    print(tea.__str__())

    print('')

    choc = Chocolate()  ### CHOCOLATE
    print(choc.__str__())

    print('')

    capp = Cappuccino()     ### CAPPUCCINO
    print(capp.__str__())
