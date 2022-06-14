def fct():
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
       ('Burton' , '1939')
    ]
    #dct = dict((y, x) for x, y in d)
    #dct = dict((letter, number) for (number, letter) in d)
    res = dict()
    for j, i in d:
        if i in res:
            res[i] = res[i] + ' ' + j
        else:
            res[i] = j
    for key, value in res.items():
        print(key + ' : ' + value)

if __name__ == '__main__':
    fct()
