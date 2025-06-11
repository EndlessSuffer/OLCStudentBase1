### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

if action.lower() == "b": #1. double equal comparison and 2. requires the : 3. action reuire to be lowercase
    if books[book_id] == "AVAILABLE":  #4. Its needs to be AVAILABLE
        books[book_id] = "BORROWED"  #5. BORROWED
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action.lower() == "r":  #6.double equal comparison 7. action requires to be lowered
    if books[book_id] == "BORROWED":   #8. BORROWED
        books[book_id] = "AVAILABLE"          #9. book _idh
        print("You have returned the book.")   #10.missing quotation
    else:
        print("The book is already available.")  #11. missing indentation
else:  #12. unnecessary indentation
    print("Invalid action.")  #13. missing quotation