import sys

def create_td(name_element, symbol, atomic_mass, electron):
    mystring = """
        <td style="border: 1px solid black; padding:10px">
            <h4>""" + name_element + """</h4>
            <ul>
                <li>""" + symbol + """</li>
                <li>""" + atomic_mass + """</li>
                <li>""" + electron + """</li>
            </ul>
        </td>"""
    return mystring

def create_empty_td():
    mystring = """
        <td style="border: 1px solid black; padding:10px">
        </td>"""
    return mystring

def fct():
    index = 0
    with open('periodic_table.txt', 'r') as fileRead:

        #with open('a.html', 'w') as f:
        with open('periodic_table.html', 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Tableau de Mendeleiv</title>
</head>
<body>
<table>""")
            lines = fileRead.readlines()
            while index < len(lines):
                res = lines[index].split(',')
                name_element = res[0].split('=')
                name_element[0] = name_element[0].strip()
                #print(name_element[0]) ## is name_element
                number_element = res[1].split(':')
                #print(number_element[1]) ## number of element
                symbol_total = res[2].split(':')
                symbol = symbol_total[1].strip()
                #print(symbol) ## symbol of element
                atomic_mass_total = res[3].split(':')
                atomic_mass = atomic_mass_total[1]
                #print(atomic_mass) ## molar of element
                electron_total = res[4].split(':')
                electron = electron_total[1]
                electron = electron.rstrip("\n")
                #print(electron) ## eletron

                if number_element[1] == '1':
                    mystring = """
    <tr>"""
                    f.write(mystring)
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    for i in range(2,18):
                        mystring = create_empty_td()
                        f.write(mystring)

                if number_element[1] == '2':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = """
    </tr>"""
                    f.write(mystring)
                if number_element[1] == '3':
                    mystring = """
    <tr>"""
                    f.write(mystring)
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)

                if number_element[1] == '4':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    for i in range(2,12):
                        mystring = create_empty_td()
                        f.write(mystring)
                if number_element[1] == '5' or number_element[1] == '6' or number_element[1] == '7' or number_element[1] == '8' or number_element[1] == '9':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                if number_element[1] == '10':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = """
    </tr>"""
                    f.write(mystring)
                if number_element[1] == '11':
                    mystring = """
    <tr>"""
                    f.write(mystring)
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                if number_element[1] == '12':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    for i in range(2,12):
                        mystring = create_empty_td()
                        f.write(mystring)
                if int(number_element[1]) >= 13 and int(number_element[1]) <= 17:
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                if number_element[1] == '18':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = """
    </tr>"""
                    f.write(mystring)

                if number_element[1] == '19':
                    mystring = """
    <tr>"""
                    f.write(mystring)
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)

                if int(number_element[1]) >= 20 and int(number_element[1]) <= 35:
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)


                if number_element[1] == '36':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = """
    </tr>"""
                    f.write(mystring)


                if number_element[1] == '37':
                    mystring = """
    <tr>"""
                    f.write(mystring)
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)

                if int(number_element[1]) >= 38 and int(number_element[1]) <= 53:
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)


                if number_element[1] == '54':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = """
    </tr>"""
                    f.write(mystring)



                if number_element[1] == '55':
                    mystring = """
    <tr>"""
                    f.write(mystring)
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)

                if int(number_element[1]) == 56:
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = create_empty_td()
                    f.write(mystring)

                if int(number_element[1]) >= 58 and int(number_element[1]) <= 85:
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)

                if number_element[1] == '86':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = """
    </tr>"""
                    f.write(mystring)


                if number_element[1] == '87':
                    mystring = """
    <tr>"""
                    f.write(mystring)
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)

                if int(number_element[1]) == 88:
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = create_empty_td()
                    f.write(mystring)

                if int(number_element[1]) >= 104 and int(number_element[1]) <= 117:
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)

                if number_element[1] == '118':
                    mystring = create_td(name_element[0], symbol, atomic_mass, electron)
                    f.write(mystring)
                    mystring = """
    </tr>"""
                    f.write(mystring)

                index = index + 1




            
            f.write("""
</table>
</body>
</html>""")
if __name__ == '__main__':
    fct()
