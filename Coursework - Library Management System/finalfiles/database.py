#Started on 25/11/19
#Completed on 10/12/2019
#by Simona Pometkova

'''This module includes functions that are called by the rest of the modules.'''

def book_NumberCheck():
    ''' This function asks for a 4-digit book ID-number until a 4-digit number is entered.

    The input must be of (int) data type and be 4-digits long. If the input is
    less than 4-digits long or more than 4-digits long, or of data type different
    than (int), the program returns an error. The user is forced to enter a 4-digit
    number.'''
    
    while True:
        bookID = input('Please enter the 4-digit book ID-number:\n:> ')
        try:
            book_ID = int(bookID) #input must be of int data type
        except ValueError:
            print('Error: invalid number. Please enter a 4-digit number.')
            print('>>>')
            continue
        else:
            if book_ID >= 1000 and book_ID < 10000: #input must be 4-digits
                print('>>>')
                break
            elif book_ID < 1000: #input must be 4-digits
                print('Error: invalid number. Please enter a 4-digit number.')
                print('>>>')
            else:
                print('Error: invalid number. Please enter a 4-digit number.')
                print('>>>')
    return bookID

def member_NumberCheck():
    ''' This function asks for a 4-digit member ID-number until a 4-digit number is entered.

    The input must be of (int) data type and be 4-digits long. If the input is
    less than 4-digits long or more than 4-digits long, or of data type different
    than (int), the program returns an error. The user is forced to enter a 4-digit
    number.'''
    
    while True:
        memberID = input('Please enter the 4-digit member ID-number:\n:> ')
        try: 
            member_ID = int(memberID) #input must be of int data type
        except ValueError:
            print('Error: invalid number. Please enter a 4-digit number.')
            print('>>>')
            continue
        else:
            if member_ID >= 1000 and member_ID < 10000: #input must be 4-digits
                print('>>>')
                break
            elif member_ID < 1000: #input must be 4-digits
                print('Error: invalid number. Please enter a 4-digit number.')
                print('>>>')
            else:
                print('Error: invalid number. Please enter a 4-digit number.')
                print('>>>')
    return memberID

def database_UpdateCheckout(memberID,bookID):
    ''' This function updates database.txt when checking out a book.

    bookID = int
    memberID = int

    It searches through database.txt line by line until a match is found. When
    a match is found, it changes the book's availability status (replaces '0' with the
    member ID entered by the user), truncates the file and then rewrites it with
    the new information.'''
    
    d = open('database.txt', 'r+')
    bookList = []
    for line in d:
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]: 
            book[4] = memberID #change book status
            line = " ; ".join(book)
            bookList.append(line)
        else:
            book = " ; ".join(book)
            bookList.append(book)
    line = '\n'.join(bookList)
    d.seek(0)
    d.truncate(0)
    d.write(line)
    d.close()

def database_UpdateReturn(bookID):
    ''' This function updates database.txt when returning a book.

    bookID = int

    It searches through database.txt line by line until a match is found. When
    a match is found, it changes the book's availability status (replaces the member
    ID-number with '0'), truncates the file and then rewrites it with the new information.'''
    
    d = open('database.txt', 'r+')
    bookList = []
    for line in d:
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]:
            book[4] = '0' #change book status
            line = " ; ".join(book)
            bookList.append(line)
        else:
            book = " ; ".join(book)
            bookList.append(book)
    line = '\n'.join(bookList)
    d.seek(0)
    d.truncate(0)
    d.write(line)
    d.close()

def logfile_UpdateCheckout(bookID):
    ''' This function updates logfile.txt when checking out a book.

    bookID = int

    It appends the text file by adding a new line with the book's information
    (ID, title, checkout date and '???' which indicates no return date).'''
    
    l = open('logfile.txt','a')
    d = open('database.txt','r')
    today = input('Please enter the current date in format dd/mm/yyyy:\n:> ') #the date the book was withdrawn
    for line in d:
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]:
            newLine = book[0]+' ; '+book[1]+' ; '+today+' ; ???' #creates the new line with the book's information
    l.write('\n'+newLine)
    l.close()

def logfile_UpdateReturn(bookID):
    ''' This function updates logfile.txt when returning a book.

    bookID = int

    It searches through logfile.txt line by line until a match is found. When
    a match is found, it changes the book's return date (replaces '???' with the
    user's input), truncates the file and then rewrites it with the new information.'''
    
    l = open('logfile.txt', 'r+')
    today = input('Please enter the current date in format dd/mm/yyyy:\n:> ') #the date the book was returned
    bookLog = []
    for line in l:
        s = line.strip()
        books = s.split(' ; ')
        if bookID == books[0] and books[3] == '???': #book must not have a return date
            books[3] = today #change book status
            line = ' ; '.join(books)
            bookLog.append(line)
        else:
            books = ' ; '.join(books)
            bookLog.append(books)
    line = '\n'.join(bookLog)
    l.seek(0)
    l.truncate(0)
    l.write(line)
    l.close()
