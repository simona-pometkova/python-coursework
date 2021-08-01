#This module takes information from database.txt and calls functions from database.py
#Started on 25/11/19
#Completed on 02/12/19
#by Simona Pometkova

'''The user is asked to input borrower's member-ID and the ID of the book
they wish to withdraw.

The program performs validity checks and funcionality and returns a message
letting the librarian know whether they have withdrawn the book successfully.'''

from database import member_NumberCheck,book_NumberCheck,database_UpdateCheckout,logfile_UpdateCheckout

def book_Checkout():
    ''' This function takes 4-digit member and book ID-numbers and proceeds to checkout a book
    by updating database.txt and logfile.txt.

    memberID = input(int)
    bookID = input(int)

    If a match is found between the user's input and the book's ID-number in database.txt, the program
    asks the user whether they want to proceed with withdrawal and if they choose to do so, updates
    database.txt and logfile.txt accordingly. Otherwise, the program terminates. If no match is found,
    the program returns a message that the library doesn't have the book.'''
    
    memberID = member_NumberCheck() #call function from database.py which asks for a 4-digit number
    bookID = book_NumberCheck() #call function from database.py which asks for a 4-digit number
    foundBook = False
    d = open('database.txt', 'r')
    for line in d: #create a list of lists, each on a new line
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]: #if the book ID-number the user has input matches with the book's ID-number from database.txt
            foundBook = True #a match is found
            if book[4] == '0': #'0' indicates that the book is not taken by any member
                print('- Book "'+book[1]+'" with ID-number',book[0]+', written by',book[2])
                print('- Availability: available to withdraw. Proceed with withdrawal?')
                print('\t (1) yes')
                print('\t (2) no')
                option = int(input(':> '))
                if option == 1:
                    print('Proceeding to withdraw...')
                    '''Calling function from database.py which updates database.txt by replacing '0'  
                    (index[4] of the corresponding book) with the member ID-number input by the user'''
                    database_UpdateCheckout(memberID,bookID)
                    '''Calling function from database.py which updates logfile.txt by adding a new line 
                    with the book's information, checkout date and '???' indicating no return date'''
                    logfile_UpdateCheckout(bookID) 
                    '''Program has finished updating the files and the book has been withdrawn'''
                    print('Withdrawal successful!')
                    print(">>>")
                elif option == 2:
                    print('Terminating...')
                    print('>>>')
                    break
                else:
                    break
            else: #if index[4] of the corresponding book is not '0' (the book is not available)
                print('- Book "'+book[1]+'" with ID-number',book[0]+', written by',book[2])
                print('- Availability: unavailable to withdraw, book currently taken by member with ID-number',book[4])
                print('>>>')
    if foundBook == False: #no match is found
        print('Unfortunately, we don\'t have this book.')
        print('>>>')
    d.close()

if __name__ == "__main__":
    book_Checkout()

