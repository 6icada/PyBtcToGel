# Code by 6icada
# Please do not copy code

# Adding libraries
import requests
import os
from bs4 import BeautifulSoup

# GET request to site to get html script
responseGEL = requests.get('https://valuta.exchange/ka/btc-to-gel?amount=1')
responseUSD = requests.get('https://valuta.exchange/ka/btc-to-usd?amount=1')
responseRUB = requests.get('https://valuta.exchange/ka/btc-to-rub?amount=1')

print('1) GEL')
print('2) USD')
print('3) RUB')
# userInput to choose what currency he/she wants
userInput = input('Enter what currency you want: ')

if userInput == 1 or userInput == '1':
    # Opening(Making) file to paste html script
    f = open('responseGEL.html', 'w')
    f.write(f'{responseGEL.text}')
    f.close()

    # Reading html file with BeautifulSoup
    with open('responseGEL.html', 'r') as f:
        document = BeautifulSoup(f, 'html.parser')

    # Making vars
    tag = document.find_all(text='GEL')
    parent = tag[0].parent
    span = parent.find('span')

    # Printing result
    print(f'BTC to GEL price is: {span.string} Lari')

    # Removing html file
    os.system('rm -f responseGEL.html 2&1> /dev/null')
elif userInput == 2 or userInput == '2':
    # Opening(Making) file to paste html script
    f = open('responseUSD.html', 'w')
    f.write(f'{responseUSD.text}')
    f.close()

    # Reading html file with BeautifulSoup
    with open('responseUSD.html', 'r') as f:
        document = BeautifulSoup(f, 'html.parser')
    
    # Making vars
    tag = document.find_all(text='USD')
    parent = tag[0].parent
    span = parent.find('span')

    # Printing result
    print(f'BTC to USD price is: {span.string} Dollar')

    # Removing html file
    os.system('rm -f responseUSD.html > /dev/null')
elif userInput == 3 or userInput == '3':
    # Opening(Making) file to paste html script
    f = open('responseRUB.html', 'w')
    f.write(f'{responseRUB.text}')
    f.close()

    # Reading html file with BeautifulSoup
    with open('responseRUB.html', 'r') as f:
        document = BeautifulSoup(f, 'html.parser')
    
    # Making vars
    tag = document.find_all(text='RUB')
    parent = tag[0].parent
    span = parent.find('span')

    # Printing result
    print(f'BTC to RUB price is: {span.string} Ruble')

    # Removing html file
    os.system('rm -f responseRUB.html 2&1> /dev/null')
