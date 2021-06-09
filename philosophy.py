from bs4 import BeautifulSoup
import requests

page = input('Enter the name of the term you want to start from (instead of spaces put "_" (test_test) >> ')

html = requests.get('https://en.wikipedia.org/wiki/'+page)
soup = BeautifulSoup(html)
links = []
n = 0

while True:
    for i in sites: 
        if n == 0:
            n += 1
            continue
        else:
            n += 1

            soup = requests.get
            
        for a in soup.find_all('a', href=True):
            if a == 'Philosophy':
                links.append(a)
                break
            else:
                links.append(a)
                    

        

    



