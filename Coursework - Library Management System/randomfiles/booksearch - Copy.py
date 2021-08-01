#This module takes information from database.txt
#Completed on 24/11/19
#by Simona Pometkova

'''The user can search for books either by title or by author,
e.g. if they type "J.K.Rowling" all books by this author will be displayed.'''

import database

def book_Title(title):
    #use docstring to describe what this function does
    bookList = database.database_Read()
    opt = 0   #do i really need a counter??
    if title == bookList[1]: #modify code so that books show up even if only a part of their
                             #title is written, e.g. inputting 'Harry Potter'
                             #would still bring up all the Harry Potter books
        if bookList[4] == '0':
            avb = "available"
            takenBy = " "
        else:
            avb = "unavailable, book currently taken by member with ID-number"
            takenBy = bookList[4]
        print('- Book "'+bookList[1]+'" with ID-number',bookList[0]+', written by',bookList[2])
        print('- Availability:',avb,takenBy)
        print(">>>")
        opt =1
     #add code which checks whether the input is of string type and returns an error if not
    if opt == 0:
        print("Unfortunately, we don't have this book.")
        print(">>>")
        
#DOESN'T CARE ABOUT INPUT AT ALL AND PRINTS OUT LAST STATEMENT. WHY?
title = input("Please enter the title of the book you are looking for:\n:> ")
book_Title(title)

def book_Author(author):
    #use docstring to describe what this function does
    opt = 0
    f = open("database.txt","r")
    for line in f:
        s = line.strip()
        book = s.split(' ; ')
        if author == book[2]:
            print('-',book[0]+':',book[1]) #modify code so that it prints only one copy of each book?
            print('>>>')
            opt = 1
    if opt == 0: #add code which checks whether the input is of string type and returns an error if not
        print('Unfortunately, we do not have any books by this author.')
        print(">>>")
    f.close()

'''
author = input('Please enter the name of the author you are looking for:\n:> ')
book_Author(author)
'''
     
