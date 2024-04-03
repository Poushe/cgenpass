import string
import random
 
def genpass(length):# Getting password length
    alphabet = string.ascii_letters + string.digits
    password = []
    
    for i in range(length):
    
        # Picking a random character from alphabet
        randomchar = random.choice(alphabet)
        
        # appending a random character to password
        password.append(randomchar)
    
    # printing password as a string
    return ("".join(password))