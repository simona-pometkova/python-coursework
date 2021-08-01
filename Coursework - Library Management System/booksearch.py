#This module takes information from database.txt
#Started on 18/11/19
#Completed on 24/11/19
#by Simona Pometkova

'''The user can search for books either by title or by author.'''

def book_Title(title):
    ''' This function searches through database.txt and displays all copies of the title the user
    has input and their availability.

    title = input(str)
    
    If the book is unavailable, it also prints out the member ID-number of the member who currently
    has the book. If the title is not found in database.txt, the program returns a message that
    the library doesn't have the book.'''
    
    foundBook = False
    d = open('database.txt', 'r')
    for line in d: #create a list of lists, each on a new line
        s = line.strip()
        book = s.split(' ; ') 
        if title == book[1]: #if the user input matches with the book title (index[1])
            if book[4] == '0': #'0' indicates that the book is not taken by any member
                avb = 'available'
                takenBy = ' '
            else:
                avb = 'unavailable, book currently taken by member with ID-number'
                takenBy = book[4]
            print('- Book "'+book[1]+'" with ID-number',book[0]+', written by',book[2])
            print('- Availability:',avb,takenBy)
            print('>>>')
            foundBook = True #there are books with this title
    if foundBook == False: #there aren't any books with this title
        print('Unfortunately, we don\'t have this book.')
        print('>>>')
    d.close()
    

def book_Author(author):
    ''' This function searches through database.txt and returns all copies that match with the
    user's input.

    author = input(str)

    If the input matches with the book's author, all book copies and their ID-numbers are returned.
    Otherwise, the program returns a message that the library doesn't have any books by the input author.'''
    
    foundAuthor = False
    d = open('database.txt','r')
    for line in d:
        s = line.strip()
        book = s.split(' ; ')
        if author == book[2]: #if the user input matches with the book's author (index[2])
            foundAuthor = True #there are books by this author
            print('-',book[0]+':',book[1]) 
            print('>>>')
    if foundAuthor == False: #there aren't any books by this author
        print('Unfortunately, we do not have any books by this author.')
        print('>>>')
    d.close()

if __name__ == "__main__":
    title = input('Please enter the title of the book you are looking for:\n:> ')
    book_Title(title)
    author = input('Please enter the name of the author you are looking for:\n:> ')
    book_Author(author)
    
