flag = True #1.Flag must be true for it to work
while flag:
    length = float(input("What is the length of the parcel?"))
    width = float(input("What is the width of the parcel?"))
    depth = float(input("What is the depth of the parcel?"))
    if length > 50 and length > 50 and depth > 50:
        parcel_size = "large"
    elif length > 50 and width > 50 and depth <= 50: #8. requires the and  9.requires depth to be lesser than 50 or 50
        parcel_size = "medium"
    else:   #2. else not elif
        parcel_size = "small"
    print("The size of your parcel is", parcel_size) #6.The size of the parcel is parcel_size not more_parcels and 7. it must be inside the loop to work
    more_parcels = input("Do you want to enter another parcel? Y or N ").upper()   #10. Requires to uppercase the letter
    if more_parcels == "N":   #3.double equal when comparison and 4. put qoutation for N
        flag = False   #5.Flag must be False tom exit the loop
    