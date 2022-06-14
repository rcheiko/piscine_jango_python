def fct():
    d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
    }   
    sorted_values = sorted(d.values()) # Sort the values
    sorted_key = sorted(d.keys())

    d_order = []
    for values in sorted_values:
        for key in sorted_key:
            for k,v in d.items():
                if k == key and values == v:
                    if key not in d_order:
                        d_order.append(key)
    for res in d_order:
        print(res)
            

if __name__ == '__main__':
    fct()
