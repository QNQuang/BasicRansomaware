from cryptography.fernet import Fernet
import os

def decrypt(key, contents):
    plaintext = Fernet(key).decrypt(contents)
    return plaintext
#Read key    
with open("secret.txt", "rb") as f:
    key = f.read()
    
for i in os.listdir():    
    if i == "test.py" or i == "test2.py" or i == "secret.txt" or os.path.isfile(i)==False:
        continue
    
    #read file name
    with open(i, "rb") as f:
        contents = f.read()
        
    #decrypt file
    plaintext=decrypt(key, contents)

    with open (i, "wb") as f:
        f.write(plaintext)

    print(f"{i}: Done")