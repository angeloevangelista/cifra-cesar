import os
import platform
import my_crypto

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

encrypted = False
message = ''
key = 0

entry = raw_input('Sua mensagem esta criptografada? (S N): ')

if entry == 'S' or entry == 's':
  encrypted = True

request = 'Digite a message criptograda: ' if encrypted else 'Digite sua message: '

message = raw_input(request)
# clear()

key = raw_input('Digite a chave: ')
# clear()

if encrypted:
  print(my_crypto.decrypt(message, key))
else:
  print(my_crypto.encrypt(message, key))