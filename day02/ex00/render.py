import sys
import os
import settings

def fct():
    if len(sys.argv) != 2 or os.path.exists(sys.argv[1]) == False:
        return
    lenTemplate = len(sys.argv[1])
    if sys.argv[1].endswith('.template') == False or lenTemplate <= 9:
        return
    a = vars(settings)

    cv_name = sys.argv[1][:len(sys.argv[1]) - 8]
    cv_name = cv_name + 'html'

    html = open(cv_name, 'w')
    done = False
    with open(sys.argv[1], 'r') as template:
        lines = template.readlines()
        j = 0
        while j < len(lines): 
            i = 0
            for key,value in a.items():
                i = i + 1
                if i > 8 and type(value) == str:
                    if key in lines[j]:
                        lines[j] = lines[j].replace('{'+key+'}', value)
                        done = True
            if done == True:
                html.write(lines[j])
                j = j + 1
                done = False
            else:
                html.write(lines[j])
                j = j + 1
    html.close()



if __name__ == '__main__':
    fct()
