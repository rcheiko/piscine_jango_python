import sys

def fct():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if len(sys.argv) != 2:
        return
    for key,value in states.items():
        if key == sys.argv[1] and value in capital_cities:
            print(capital_cities[value])
            return
    print('Unknown state')

if __name__ == '__main__':
    fct()
