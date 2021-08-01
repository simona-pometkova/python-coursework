#This module takes information from database.txt and calls functions from database.py
#Started on 30/11/19
#Completed on 06/12/19
#by Simona Pometkova

'''The user is asked to input the ID-number of the book they wish to return.

The program returns an error message if the ID is invalid or if the book is
already available. Otherwise, it returns the book by updating its status in
database.txt and logfile.txt.'''

from database import book_NumberCheck,database_UpdateReturn,logfile_UpdateReturn

def book_Return():
    ''' This function takes a 4-digit book ID-number and proceeds to return the book.

    bookID = input(int)

    If a match is found between the user's input and the book's ID in database.txt, the program
    asks the user whether they want to return the book and if they choose to do so, updates database.txt
    and logfile.txt accordingly. Otherwise, the program terminates. If no match is found, the program
    returns a message that the library doesn't have the book.'''
    
    bookID = book_NumberCheck() #call function from database.py which asks for a 4-digit number
    foundBook = False
    d = open('database.txt', 'r')
    for line in d: #create a list of lists, each on a new line
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]:
            foundBook = True #a match is found
            if book[4] != '0': #the book is currently taken by a member
                print('- Book "'+book[1]+'" with ID-number',book[0]+', written by',book[2])
                print('- Book currently taken by member with ID-number',book[4]+'. Return book?')
                print('\t (1) yes')
                print('\t (2) no')
                option = int(input(':> '))
                if option == 1:
                    print('Proceeding to return...')
                    '''Calling function from database.py which updates database.txt by 
                    replacing the member ID (index[4] of the corresponding book) with a '0' '''
                    database_UpdateReturn(bookID)
                    '''Calling function from database.py which updates logfile.txt by replacing
                    the '???' (indicating no return date) with the user's input as the return date'''
                    logfile_UpdateReturn(bookID)        
                    '''Program has finished updating the files and the book has been returned'''
                    print('Return successful!')
                    print('>>>')
                elif option == 2:
                    print('Terminating...')
                    print('>>>')
                    break
                else:
                    break
            else: #if index[4] of the corresponding book is '0' (the book is already available)
                print('- Book "'+book[1]+'" with ID-number',book[0]+', written by',book[2])
                print('- Book is already available!')
                print('>>>')
    if foundBook == False: #no match is found
        print('Unfortunately, we don\'t have this book.')
        print('>>>')
    d.close()

if __name__ == "__main__":   
    book_Return()
