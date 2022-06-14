from local_lib.path import Path

def fct():

    exo = Path('exercice').mkdir_p()

    w = Path('./exercice/' + exo + '.txt').touch()

    w.write_text('salut comment ca va')

    read_text = Path.read_text('./exercice/' + exo + '.txt')

    print(read_text)

if __name__ == '__main__':
    fct()