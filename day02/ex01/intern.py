class Intern:
    def __init__(self, Name="My name? I’m nobody, an intern, I have no name."):
        self.Name = Name
    
    def __str__(self):
        return(self.Name)


    class Coffee:
        def __str__(self) -> str:
            return("This is the worst coffee you ever tasted.")

        def work(self):
            raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Intern.Coffee()

if __name__ == '__main__':
    first = Intern()
    second = Intern("Mark")
    a = first.__str__() # display name of no name
    print(a)



    b = second.__str__() # display name of Mark
    print(b)




    drink = second.Coffee() # Mark make a coffee
    c = drink.__str__()
    print(c)


    try:
        second.Coffee().work()  # no name try to work
    except Exception as event:
        print(event)
