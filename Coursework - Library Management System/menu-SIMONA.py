#Started on 18/11/19
#by Simona Pometkova

#The following lines list all the possible options and ask the user to select an option.
while True:
    print(">>>>>>>>>>>>>>>>>>>>> LIBRARY MANAGEMENT SYSTEM <<<<<<<<<<<<<<<<<<<<<")
    print(" ")
    print("Welcome! Please choose one of the following options (or 'q' to quit):")
    print("\t (1) - search for books")
    print("\t (2) - return books")
    print("\t (3) - display list of books")
    print("\t (4) - check books out")
    print("\t (q) - quit")
    opt = input("Type the number/letter of the corresponding option:\n:> ")

#The following lines describe what each option does.
    if opt == '1': #search for books
        while True:
            from booksearch import book_Title,book_Author
            print('Please select how you would like to search for a book (or "q" to quit and go back to main menu):')
            print('\t (1) by title')
            print('\t (2) by author')
            print('\t (q) quit')
            search = input(':> ')
            if search == '1':
                title = input("Please enter the title of the book you are looking for:\n:> ")
                book_Title(title)
            elif search == '2':
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
        print("Return books chosen. Please wait...")
        #from bookreturn.py import
        break
    elif opt == '3': #display list of books
        print("Displaying list of books. Please wait...")
        #from booklist.py import
        break
    elif opt == '4': #check books out
        '''
        while True:
            from bookcheckout import *
            print("Withdraw a book?")
            print("\t (1) yes")
            print("\t (2) no")
            option = input(":> ")
            if option == '1':
                book_Availability()
            elif option == '2':
                print("Going back to main menu...")
                print(" ")
                break
            else:
                print("Error: invalid option.")
                print(">>>")
        '''
    elif opt == 'q':
        print("See you again soon! :)")
        break
    else:
        print("Error: no such option. Please try again!")
        print(" ")
