import requests, json, sys, dewiki

def fct():
    if len(sys.argv) != 2:
        print('You should have 2 arguments.')
        return

    PARAMS = {
    "action": "parse",
    "page": sys.argv[1],
    "format": "json",
    "prop": "wikitext"
    }
    
    URL = "https://fr.wikipedia.org/w/api.php"

    try:
        a = requests.get(URL, params=PARAMS)
    except Exception as event:
        print('Erreur in Get')

    data = a.json()

    try:
        res = data["parse"]["wikitext"]["*"]
    except Exception as event:
        print("Error name doesn't exist")

    final_res = dewiki.from_string(res)

    with open(sys.argv[1]+'.wiki', 'w') as wiki:
        wiki.write(final_res)

if __name__ == '__main__':
    fct()