import requests
import time
from bs4 import BeautifulSoup

start_time = time.time()

def pull(link):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all('a', href=lambda href: href and "Classes.aspx?ID=" in href)
    except:
        print("Error loading the webpage")
        return()
    return(elements)

def tablify(input):
    output = [];
    try:
        for element in input:
            if element.text != "Details":
                output.append(element.text)
    except:
        print("Parameter of tablify is not a ResultSet")
        return ()
    return(output)

tab = tablify(pull("https://2e.aonprd.com/Classes.aspx"))
print(tab)

def addThreeMinusOne(tab):
    tab.append("One")
    tab.append("Two")
    tab.append("Three")
    tab.pop()

    return(tab)

print (addThreeMinusOne(tab))

print(f"\n\nTime taken: {time.time() - start_time} seconds")