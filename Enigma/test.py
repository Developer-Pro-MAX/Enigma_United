import cryptography 
from cryptography.fernet import Fernet
key = Fernet.generate_key()
message = "this is a test message"
encoded = message.encode()
f = Fernet(key)
encrypted = f.encrypt(encoded)
print(encrypted)

f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
origin = decrypted.decode()
print(origin)
 
