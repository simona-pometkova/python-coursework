#This module takes information from database.txt
'''
The user can search for books either by title or by author,
e.g. if they type "J.K.Rowling" all books by this author will come up.
'''

bookList=[]
f = open("database.txt","r")
for line in f:
    bookList.append(line)
    s = line.strip()
    bookList = s.split(' ; ')
    print(bookList) #delete after code works

def bookSearch():
    '''
    print("Please select how you would like to search for a book:")
    print("\t (1) by title")
    print("\t (2) by author")
    option=int(input(":>"))
    if option==1:
    '''
    book=input("Please enter the title of the book:\n:>")
    if book==bookList[1]:
        if bookList[4]=='0':
            avb="Available"
        else:
            avb="Unavailable"
        print("Book '"+bookList[1]+"' with ID-number",bookList[0]+", written by",bookList[4]+":")
        print(avb)

bookSearch()
    


