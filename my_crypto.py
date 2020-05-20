def encrypt(message, key):
  encrypted_message = ''

  for character in message:
    encrypted_message += str(chr(ord(character) + int(key)))
  
  return encrypted_message

def decrypt(message, key):
  decrypted_message = ''

  for character in message:   
    decrypted_message += str(chr(ord(character) - int(key)))
  
  return decrypted_message