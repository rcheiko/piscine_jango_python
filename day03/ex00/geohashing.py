import sys
import antigravity

def fct():
    if len(sys.argv) != 4:
        print("You need to put three argument !")
        print("Exemple : 37.421542 -122.085589 b'2005-05-26-10458.68'")
        return

    try:
        a = float(sys.argv[1])
    except ValueError:
        print('This is not a float argument (1) !')
        return
    try:
        b = float(sys.argv[2])
    except ValueError:
        print('This is not a float argument (2) !')
        return

    try:
        c = bytes(sys.argv[3], 'utf-8')
    except ValueError:
        print('This is not a argument bytes !')
        return
    
    antigravity.geohash(a, b, c)

if __name__ == '__main__':
    fct()