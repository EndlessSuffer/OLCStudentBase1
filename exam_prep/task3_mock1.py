### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

if action = "b"
    if books[book_id] == "Available":
        books["B"] = "borrowed"
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action = "r":
    if books[book_id] == "borrowed":
        books("R") = "available"
        print(You have returned the book.")
    else:
    print("The book is already available.")
    else:
        print("Invalid action.)