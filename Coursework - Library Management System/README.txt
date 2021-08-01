# Notes on Introduction to Programming coursework by Simona Pometkova
# Library Management System
# 12/12/2019

# database.txt 
The database contains 30 copies in total of 18 book titles. The file is formatted as follows: 

book ID ; book title ; book author ; purchase date ; availability (0 indicates that the book is available)

Each book copy is written on a new line.

# logfile.txt
The logfile contains data of 22 checkouts. The file is formatted as follows:

book ID ; book title ; checkout date ; return date ("???" indicates that the book hasn't been returned)

Each log is written on a new line. The first 12 entries contain full data. The rest of the entries are books who are currently checked out (information taken from database.txt). Therefore they don't have a return date.

# menu.py
This is the main program used to interact with the user. It contains all the options the user can choose from and performs the rest of the programs depending on the user's choice.

# booksearch.py
The program successfully searches through the database textfile and prints out all copies given by the user's input. Note that the program is case sensitive and doesn't accept lowercase input when the content in database.txt contains uppercase letters. The input must be a literal copy of the book's title (or author). Also note that the user can search for books either by entering a title or the name of an author.

# bookcheckout.py
The program successfully withdraws books one at a time. First it asks for a member ID which must be a 4-digit number, then asks for a book ID which has the same restriction. If there exists a copy with the book ID provided, the program asks the user to enter the date and then proceeds to check the book out by changing its availability status in database.txt and adding a line in logfile.txt with the book's information and the date entered by the user.

# bookreturn.py
The program successfully returns books one at a time. It only requires the book's ID which again must be a 4-digit number. If there exists a book with the ID provided, the program checks its availability and if it's currently on loan, proceeds to return the book by changing its availability status in database.txt and adding a return date in logfile.txt.