age = 0
height = float(0) 
rejected = 0   #5. rejected needs to start from 0
rider = 0
age = int(input("Please enter your age ")) #1. missing quotation
height = float(input("Please enter your height "))
while age != 0 or height != 0:  #4. missing != and 5. use or not and
    if age <= 7 or age > 70 or height <= 1.3: 
        if age <= 7:
            print("You are too young to ride") 
        if age > 70: #2. age is more than 70
            print("You are too old to ride") 
        if height <= 1.3:
            print("You are too short to ride") 
        rejected = rejected + 1     # 3. rejected add 1
    else: #10. missing indentation
        print("You can ride the Roller Coaster") 
        rider = rider + 1  #7. wrong variable
    age = int(input("Please enter your age "))
    height = float(input("Please enter your height ")) 
print("Number of people rejected ", rejected) #8.rejected not rider
print("Number of riders ", rider) #9.rider not rejected