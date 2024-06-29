#defining variables for items to be stored and used later in the program
allBooks = [
                ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
                ['9780134494166',"The Human Body","Dave R",1,[]],
                ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
           ]
borrowedISBNs = []

bookname = []

#defining the main variable
def start():
    
    #creating a fucntion for the menu printing 
    def printMenu():
        print("\n######################\n")
        print("1: (A)dd a new book.\n")
        print("2: Bo(r)row books.\n")
        print("3: Re(t)urn a book.\n")
        print("4: (L)ist all books.\n")
        print("5: E(x)it.\n")
        print("######################\n")
    
    #calling the print menu function 
    printMenu()
    
    #asking the user for their input 
    selection = str(input("Your selection> ")).upper()
    
    #creating a function that allows the user to create a new book 
    def newBook():
    # Initialize an empty list to store ISBNs.
        isbns = []

        # Prompt the user to enter the book name and store it in the 'bookName' variable.
        bookName = str(input("Book name> "))
        
        # Check if the book name contains '*' or '%'. If it does, ask the user to enter a valid book name.
        while '*' in bookName or '%' in bookName:
            print("Invalid book name!")
            bookName = str(input("Book name> "))

        # Prompt the user to enter the author's name and store it in the 'Author' variable.
        Author = str(input("Author name> "))
        
        # Use a loop to ensure that the edition is a valid integer.
        while True:
            edition = input("Edition> ")

            # Check if the entered edition is a digit (integer). If it is, exit the loop.
            if edition.isdigit():
                break
            else:
                print("Invalid input. Please enter a valid integer edition.")
        
        # Use a loop to ensure that the ISBN is valid.
        while True:
            isbn = input("ISBN>  ")

            # Remove any non-digit characters from the entered ISBN.
            isbn = ''.join(filter(str.isdigit, isbn))

            # Check if the ISBN has exactly 13 digits.
            if len(isbn) != 13:
                print("Invalid ISBN!")
                continue

            # Define a list of weights for ISBN validation.
            weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
            
            # Initialize a variable to store the total for ISBN validation.
            total = 0

            # Calculate the total using ISBN validation weights and digits.
            for i in range(13):
                digit = int(isbn[i])
                weight = weights[i]
                total += digit * weight

            # Check if the total is divisible by 10, which is a valid ISBN condition.
            if total % 10 == 0:
                # Create a list of existing ISBNs for comparison.
                for x in range(len(allBooks)):
                    isbns.append(allBooks[x][0])
                
                # Check if the entered ISBN is already in the list of existing ISBNs.
                if isbn in isbns:
                    print("Duplicate ISBN is found! Cannot add the book.")
                    start()
                else:
                    # If the ISBN is valid and not a duplicate, add the book to the library.
                    print("A new book is added successfully.")
                    oneNewBook = [isbn, bookName, Author, edition, []]           
                    allBooks.append(oneNewBook)
                    start()
            else:
                # If the ISBN is invalid, inform the user and return to the starting point.
                print("Invalid ISBN.")
                start()

    # Define a function for searching books based on a search term.
    def search_books(search_term):
        # Store the original search term.
        original = search_term

        # Extract the search mode (indicated by the last character) and convert the search term to lowercase.
        search_mode = search_term[-1]
        search_term = search_term[:-1].lower()

        # Initialize an empty list to store matching books.
        matching_books = []

        # Iterate through the list of allBooks.
        for book in allBooks:
            # Check if the book's ISBN is not in the borrowedISBNs list.
            if book[0] not in borrowedISBNs:
                # Convert the book title to lowercase for case-insensitive matching.
                book_title = book[1].lower()

                # Depending on the search mode, match the search term with book titles.
                if search_mode == '*':
                    # If search_mode is '*', check if the search term is contained within the book title.
                    if search_term in book_title:
                        matching_books.append(book)
                elif search_mode == '%':
                    # If search_mode is '%', check if the book title starts with the search term.
                    if book_title.startswith(search_term):
                        matching_books.append(book)
                else:
                    # If no special search mode is specified, check for an exact match between the original term and book title.
                    if original == book_title:
                        matching_books.append(book)

        # Return the list of matching books.
        return matching_books

    #creating a new function to allow books to be returned
    def Return():
        #asking the user for the ISBN number
        Isbn = str(input("ISBN> "))
        
        #looking if the Isbn is in the borrowedISBN's list, and if it is, it says the book is returned and removes the book from the borrowed list
        if Isbn in borrowedISBNs:
            print(bookname[borrowedISBNs.index(Isbn)],"is returned")
            bookname.remove(bookname[borrowedISBNs.index(Isbn)])
            borrowedISBNs.remove(Isbn)

            start()
        #if the book is not found in the ISBN it states that no book was found
        else:
            print("No book is found!")
            start()
    
    #creating a function to list all the books and whether they are borrowed or not.
    def List():
        #iterating through all the books
        for x in range(len(allBooks)):
            #if the book is in the borrowed isbn list it prints the book is unavailable and if its not, its says its a available
            if allBooks[x][0] in borrowedISBNs:
                print("\n---------------\n\n[Unavailable]\n")
            else:
                print("\n---------------\n\n[Available]\n")
            #printing all the information for the book in the proper fasion
            print(allBooks[x][1],"-",allBooks[x][2],"\n")
            print("E:",allBooks[x][3],"ISBN:",allBooks[x][0],"\n")
            print("Borrowed by:",allBooks[x][4])
        
        start()
    
    #creating a funtion that prints the final list of books using the same method as the List function
    def end():
        #printing a title
        print("\n$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
        #if the book is in the borrowed isbn list it prints the book is unavailable and if its not, its says its a available
        for x in range(len(allBooks)):
            if allBooks[x][0] in borrowedISBNs:
                print("\n---------------\n\n[Unavailable]\n")
            else:
                print("\n---------------\n\n[Available]\n")
            #printing all the information for the book in the proper fasion
            print(allBooks[x][1],"-",allBooks[x][2],"\n")
            print("E:",allBooks[x][3],"ISBN:",allBooks[x][0],"\n")
            print("Borrowed by:",allBooks[x][4])
        exit()
    
    if selection == "1" or selection == "A":  # Option for adding a new book
        newBook()
    elif selection == "2" or selection == "R":  # Option for searching and borrowing books
        while True:
            borrower_name = input("Enter the borrower name> ").strip()
            user_input = input("Search term> ").strip().lower()
            
            matching_books = search_books(user_input)  # Search for books based on the user's input
            
            if matching_books:  # If there are matching books
                for i, book in enumerate(matching_books):
                    print('-"'+book[1]+'" is borrowed!')  # Display the borrowed book's title
                    book[4].append(borrower_name)  # Add borrower's name to the book's information
                    bookname.append(book[1])  # Add the book's title to a list
                    borrowedISBNs.append(book[0])  # Add the book's ISBN to a list
                
                start()  # Return to the main menu
            else:
                print("No books found!")  # If no matching books, inform the user
                start()  # Return to the main menu
            
    elif selection == "3" or selection == "T":  # Option for returning a borrowed book
        Return()
    elif selection == "4" or selection == "L":  # Option for listing books
        List()
    elif selection == "5" or selection == "X":  # Option to exit the program
        end()
    else:
        print("Wrong selection! Please select a valid option.")  # Handle invalid user input
        start()  # Return to the main menu

        
start()
