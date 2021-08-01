#Started on 18/11/19
#Completed on 12/12/19
#by Simona Pometkova

''' This is the main module used to perform the library management system operations.

It asks the user to choose an option and calls corresponding functions from the rest of
the modules to perform the required tasks.'''

#The following lines list all the possible options and ask the user to select an option.
while True:
    '''This is the main menu.

    It contains the program's name and all available options the user can choose from.'''
    
    print(">>>>>>>>>>>>>>>>>>>>> LIBRARY MANAGEMENT SYSTEM <<<<<<<<<<<<<<<<<<<<<")
    print(" ")
    print("Welcome! Please choose one of the following options (or 'q' to quit):")
    print("\t (1) - search for books")
    print("\t (2) - return books")
    print("\t (3) - display list of books")
    print("\t (4) - check books out")
    print("\t (q) - quit")
    opt = input("Type the number/letter of the corresponding option:\n:> ")

    #The following lines perform tasks based on the user's chosen option.
    if opt == '1': #search for books
        while True:
            from booksearch import book_Title,book_Author
            print('Please select how you would like to search for a book (or "q" to quit and go back to main menu):')
            print('\t (1) by title')
            print('\t (2) by author')
            print('\t (q) quit')
            search = input(':> ')
            if search == '1': #searching by title
                title = input("Please enter the title of the book you are looking for:\n:> ")
                book_Title(title)
            elif search == '2': #searching by author
                author = input("Please enter the name of the author you are looking for:\n:> ")
                book_Author(author)
            elif search == 'q':
                print("Going back to main menu...")
                print(" ")
                break
            else:
                print("Error: invalid option.")
                print(">>>")
    elif opt == '2': #return books
        while True:
            from bookreturn import book_Return
            print("Return a book?")
            print("\t (1) yes")
            print("\t (2) no")
            optionCheck = input(":> ")
            if optionCheck == '1': 
                book_Return()
            elif optionCheck == '2':
                print("Going back to main menu...")
                print(" ")
                break
    elif opt == '3': #display list of books
        print("Displaying list of books. Please wait...")
        break
    elif opt == '4': #check books out
        while True:
            from bookcheckout import book_Checkout
            print("Withdraw a book?")
            print("\t (1) yes")
            print("\t (2) no")
            optionCheck = input(":> ")
            if optionCheck == '1':
                book_Checkout()
            elif optionCheck == '2':
                print("Going back to main menu...")
                print(" ")
                break
    elif opt == 'q':
        print("See you again soon! :)")
        break
    else: #incorrect input
        print("Error: no such option. Please try again!")
        print(" ")

''' I have tested the module and it works. ''' 
