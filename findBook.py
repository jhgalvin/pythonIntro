#A function to search for a book using loops

books = ["Narnia", "Harry Potter", "Winn Dixie", "Lord of the Flies"]
print("Enter the name of the book: ")
bookNeeded = input()

for book in books:
    if book == bookNeeded:
        print("Book was found!")
        break
else:
    print("Book was not found in inventory!")