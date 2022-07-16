# Library Management System

class Library:
    owner={}
    def __init__(self,listOfBooks,libName):
        self.libName1=libName
        self.available_books=list(listOfBooks.split(","))

    def displayBook(self):
        print("Books in the library are:")
        for i in self.available_books:
            print(i)
        # print("Borrowed books are:")
        # print(self.owner)

    def addBook(self):
        bookName=input("Please enter the book name you want to donate:\n")
        self.available_books.append(bookName)
        print("Thanks for your donation. Your books has been successfully added in our library !!")

    def lendBooks(self):
        try:
            bookName=input("Please enter the book name you want to lend:")
            if bookName not in self.available_books:
                print(f"This book is currently owned by {self.owner[bookName]}")
            else:
                user_name=input("Please enter your name:")
                self.owner[bookName] = user_name
                self.available_books.remove(bookName)
                print("Book has been lended successfully.!!")
        except:
            print("We couldn't find the match in our system. Please provide the correct information.")

    def returnBook(self):
        ownerName=input("Please provide your username:")
        bookName=input("Enter the book name you want to return:")
        try:
            if(self.owner[bookName]==ownerName):
                self.available_books.append(bookName)
                self.owner.pop(bookName)
                print("Book has been returned successfully !!")
            else:
                print("We couldn't find the match in our system. Please provide the correct information.")
        except:
            print("We couldn't find the match in our system. Please provide the correct information.")

if __name__=='__main__':
    l=Library("C,C++,Java","SachinLibrary")
    while 1:
        print("\nPlease select the action:\n"
              "1. Display all books in the library\n"
              "2. Add book in the library\n"
              "3. Lend book from the library\n"
              "4. Return book to the library\n"
              "5. Exit\n")
        option=int(input(""))
        if option==1:
            l.displayBook()
        elif option==2:
            l.addBook()
        elif option==3:
            l.lendBooks()
        elif option==4:
            l.returnBook()
        elif option==5:
            print("Thanks for using our library management system. Hope to see you next time.")
            break
        else:
            print("Wrong input. Please try again...")

