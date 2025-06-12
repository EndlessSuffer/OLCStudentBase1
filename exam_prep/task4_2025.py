#Task 5.1
def shift(char):
    alphas = 'abcdefghijklmnopqrstuvwxyz' 
    if char in alphas:
        idx=alphas.find(char)
        shifted_idx=(idx+1)%26
        return alphas[shifted_idx]
    else:
        return(char)
#print(shift("a"))

#Task 5.2
def encrypt(message, positions):
    sentence=""
    for c in message:
        tempchar=c
        for i in range(positions):
            tempchar= shift(tempchar)
        sentence= sentence+c
    return sentence
print(encrypt("ba na na", 2))

