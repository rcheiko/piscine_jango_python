if __name__ == '__main__':
    with open('numbers.txt', 'r') as f:
        for line in f:
            register = line.split(",")
            register[99] = 100
            for i in register:
                print(i)
