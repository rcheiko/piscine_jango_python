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

    newList = []

    li = sys.argv[1].split(',')
    counter = 0
    for delSpace in li:
        newList.append(delSpace.strip())
    for avList in newList:
        for key,value in states.items():
            if key.lower() in avList.lower():
                print(capital_cities[value], 'is the capital of', key)
                counter = 1

        for key,value in capital_cities.items():
            if counter == 1:
                break
            if avList.lower() == value.lower():
                for key2, value2 in states.items():
                    if key == value2:
                        print(capital_cities[value2], 'is the capital of', key2)
                        counter = 1
        if (counter == 1):
            counter = 0
        elif avList != '':
            print(avList, 'is neither a capital city nor a state')


if __name__ == '__main__':
    fct()
