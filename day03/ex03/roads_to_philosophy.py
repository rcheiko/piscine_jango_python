import sys, requests
from bs4 import BeautifulSoup

def fct():
    if len(sys.argv) != 2:
        print("You need to have two arguments.")
        return
    
    listOfLinkSearch = []
    listOfLinkSearch.append(sys.argv[1])
    search = '/wiki/'+sys.argv[1]
    while 1:
        debug = 0
        url = "https://en.wikipedia.org/"

        req = requests.get(url + search)

        text = req.text

        soup = BeautifulSoup(text, 'html.parser')
        if "Philosophy" in soup.find({"h1"}, {"class":"firstHeading"}):
            for i in listOfLinkSearch:
                print(i)
            print(len(listOfLinkSearch), 'roads from', sys.argv[1], "to philosophy")
            return

        res = soup.find({"div"}, {"class":"mw-parser-output"})
        res =  res.find_all({"p"}, {"class":False})
        for balise_p in res:
            if len(balise_p.find_all('a')) >= 1:
                res = balise_p
                break
        try:
            resultAllA = res.find_all('a')
        except Exception as event:
            print("It leads to a dead end !")
            return
        for link in resultAllA:
            website = link.get("href")
            if "/wiki/" in website:
                if "wikipedia:" not in website:
                    search = website
                    if search.replace('/wiki/', '') in listOfLinkSearch:
                        # print(search)
                        print("It leads to an infinite loop !")
                        return
                    listOfLinkSearch.append(search.replace('/wiki/', ''))
                    debug = 1
                    # print('LIST :',listOfLinkSearch)
                    break
        if debug == 0:
            print("It leads to a dead end !")
            return

if __name__ == '__main__':
    fct()
    # example : python3 roads_to_philosophy.py "Philosophical methodology"