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

def addThreeMinusOne(tab):
    tab.append("One")
    tab.append("Two")
    tab.append("Three")
    tab.pop()

    return(tab)

def longestName(tab):
    longest = 0
    iLongest = 0
    i = 0
    for elements in tab:
        lengthWord = 0
        for letters in elements:
            lengthWord += 1
        if (lengthWord > longest):
            longest = lengthWord
            iLongest = i
#        print(tab[i])
#        print(lengthWord)
        i += 1
    print("\n")
    return (tab[iLongest])

def countLetterEach(tab, letter):
    countTot = 0
    id = 0
    for elements in tab:
        count = 0
        for letters in elements:
            if letters == letter:
                count += 1
        countTot += count
        print(f"{tab[id]} has {count} times the letter {letter}.")
        id += 1

    print(f"\nThe letter {letter} is present {countTot} times in total.\n")
    return()

print (tab)
print (f"\n{countLetterEach(tab, 'i')}")

print(f"\nTime taken: {time.time() - start_time} seconds")