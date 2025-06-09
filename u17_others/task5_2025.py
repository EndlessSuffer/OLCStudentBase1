
# In [1]:    # Task 2.1
#           Program Code
#           Output:
# All code should have appropriate comments and all identifiers should be appropriately named. [4]

# Task 5.1
# Write a shift() function that has the parameter char passed to it. 
# The function must shift a lower-case letter down the alphabet sequence 
# by one position (a → b ... → y → z → a) and do nothing to other characters.    
#[4]


# This is the seCret me55age!
def shift(char):
    alpha="abcdefghijklmnopqrstuvwxyz"
    oidx=alpha.find(char)
    newidx=(oidx + 1)%26
    newchar=alpha[newidx]
    return newchar
print(shift("a"))
###############################################################
#### Note from T.DAVID - This sample question is from MOE for Y2025 Sample
#### Usually, you would use the ASCII table to do caesar encryption.
#### But since, details were not provided, we used a string instead
#### for translation.
###############################################################



# Task 5.2
# Write a function encrypt() that has the parameters message and positions 
# passed to it. The function must use the shift() function to encrypt the
#  message argument by shifting all the lower-case letters in the message 
# down the alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.                     [7]

# assume the return is the encrypted message
def encrypt(message, positions):
    alpha="abcdefghijklmnopqrstuvwxyz"
    ciphertext= ""

    for c in message:
        if c in alpha:
            temp = c # temporary value
            for i in range(positions):
                temp = shift(temp)
            ciphertext += temp
        else:
            ciphertext += c
    return ciphertext
    

print(encrypt("blah blah blah 3948kja!!!", 6))

# Task 5.3
# Write a function shift_up() that has the parameter char passed to it. 
# The function must shift a lower-case letter up the alphabet sequence by 
# one position (a ← b ... ← y ← z ← a) and do nothing to other characters.  
#[2]
def shift_up(char):
    oidx=ord(char) #finds me the ordinal value of the character
    newidx=(oidx-1)% (oidx+26) #find the encrypted index
    newchar= chr(newidx) # find the corresponding char from ASCII
    if newchar=="`":
        newchar="z"
    return newchar
print(shift_up("a"))




# Task 5.4
# Write a function decrypt() that has the parameters ciphertext and 
# positions passed to it. The function must use the shift_up() function 
# to decrypt the ciphertext argument by shifting all the letters up the 
# alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.      [1]
def decrypt(message, positions):
    alpha="abcdefghijklmnopqrstuvwxyz"
    msg= ""

    for c in message:
        if c in alpha:
            temp = c # temporary value
            for i in range(positions):
                temp = shift_up(temp)
            msg += temp
        else:
            msg += c
    return msg
print(decrypt("ccccc",1))


# Task 5.5
# Create a simple text-based user interface to:
# • request the user to enter ‘E’ to encrypt a message or ‘D’ to
#  decrypt a ciphertext (case insensitive) and to re-enter 
# if the input is not ‘E’, ‘D’, ‘e’ or ‘d’

# • request the user to enter the message or the ciphertext
# • request the user to enter the number of positions to shift the 
# letters and the user to re-enter the number if the input is not a positive integer

# • output the encrypted message and write the encrypted message to the file 
# encrypted.txt, if the user requested to encrypt a message

# • output the decrypted ciphertext if the user requested to decrypt a message.
# Your program should use the encrypt() and decrypt() functions. 
# Test your program with the following input:

#                         a, E, This is the seCret me55age!, -1, 12   

#  Save your JupyterLab notebook for Task 5 [7]
while True:
    option = input("Enter E to encrypt, D to decrypt: ")

    if option.lower() not in ['e','d']:
        print("You can only enter E or D")
    else:
        stringval= input("Enter the message to encrypt or ciphertext to decrypt: ")
        
        while True:
            pos=input("Enter the number of positions to shift by: ")
            if pos.isdigit() and int(pos)>0:
                pos = int(pos)
                break
            else: 
                print("You can only enter a positive integer")
        if option.lower()=="e":
            output= encrypt(stringval,pos)

            with open("encrypted.txt","w") as fobj:
                fobj.write(output)
        elif option.lower()=="d":
            output= decrypt(stringval,pos)
    print(output)