import os
import my_crypto

clear = lambda: os.system('cls')

encrypted = False
message = ''
key = 0

entry = input('Sua mensagem está criptografada? (S N): ')
clear()

if entry == 'S' or entry == 's':
  encrypted = True

request = 'Digite a message criptograda: ' if encrypted else 'Digite sua message: '

message = input(request)
clear()

key = input('Digite a chave: ')
clear()

if encrypted:
  print(my_crypto.decrypt(message, key))
else:
  print(my_crypto.encrypt(message, key))