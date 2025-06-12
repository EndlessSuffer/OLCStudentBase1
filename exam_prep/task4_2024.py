def div_2(number): 
    halved = int(number/2) 
    return halved 

#Task 4.1 # checked 4.5
def odd_or_even(number):
    remainder= number%2
    if remainder>0: ## ? -0.5 strange way of checking
        return "Odd"
    else:
        return "Even"
#print(odd_or_even(6))

#Task 4.2
def prime(number):
    number=int(number)
    if number< 2:
        return "Not prime"
    if number==2:
        return "Prime"
    if odd_or_even(number)=="Even":
        return "Not prime"
    for i in range(3,div_2(number)+1):
        remainder=number % i
        if remainder == 0: #???
            return "Not prime"
    return "Prime"

#Task 4.3
while True:
    number=input("Enter a whole number to check if it is prime or not: ")
    if number.isdigit():
        pnumber=prime(number)
        print(f"The number {number} is {pnumber} number")
        break
    else:
        print("Input a proper whole number.")

# for i in range(100):
#     if prime(i) == "Prime":
#         print(i)
