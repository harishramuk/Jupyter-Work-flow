import requests
response = requests.get('https://blockchain.info/ticker')
binf = response.json()
INPUT = input('enter wich rate if you want USD,GBP,EUR:')
for k,v in binf[INPUT.upper()].items():
    print(k  ,  v)