# Code by 6icada
# Please do not copy code

# Adding libraries
import requests
import os
from bs4 import BeautifulSoup

# GET request to site to get html script
response = requests.get('https://valuta.exchange/ka/btc-to-gel?amount=1')

# Opening(Making) file to paste html script
f = open('response.html', 'w')
f.write(f'{response.text}')
f.close()

# Reading html file with 
with open('response.html', 'r') as f:
    document = BeautifulSoup(f, 'html.parser')

# Making vars
tag = document.find_all(text='GEL')
parent = tag[0].parent
span = parent.find('span')

# Printing result
print(f'Lari(GEL) is Georgian currency')
print(f'BTC to GEL price is: {span.string} Lari')

# Removing html file
os.system('rm -f response.html 2&1> /dev/null')