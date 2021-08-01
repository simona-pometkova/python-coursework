#This module takes information from database.txt
#Started on 25/11/19
#Completed on 02/12/19
#by Simona Pometkova

'''The user is asked to input borrower's member-ID and the ID of the
book(s) they wish to withdraw.

The program performs validity checks and funcionality and returns
a message letting the librarian know whether they have withdrawn
the book successfully.'''

def checkout_Member():
    while True:
        memberID = input("Please enter the 4-digit member ID-number:\n:> ")
        try: 
            member_ID = int(memberID)
        except ValueError:
            print("Error: invalid number. Please enter a 4-digit number.")
            print(">>>")
            continue
        else:
            if member_ID >= 1000 and member_ID <= 10000:
                print(">>>")
                break
            elif member_ID < 1000:
                print("Error: invalid number. Please enter a 4-digit number.")
                print(">>>")
            else:
                print("Error: invalid number. Please enter a 4-digit number.")
                print(">>>")
    return memberID

def checkout_Book():
    #use docstring to describe what this function does
    while True:
        bookID = input("Please enter the 4-digit ID-number of the book you wish to withdraw:\n:> ")
        try:
            book_ID = int(bookID)
        except ValueError:
            print("Error: invalid number. Please enter a 4-digit number.")
            print(">>>")
            continue
        else:
            if book_ID >= 1000 and book_ID <= 10000:
                print(">>>")
                break
            elif book_ID < 1000:
                print("Error: invalid number. Please enter a 4-digit number.")
                print(">>>")
            else:
                print("Error: invalid number. Please enter a 4-digit number.")
                print(">>>")
    return bookID

memberID = checkout_Member()
bookID = checkout_Book()

def book_Checkout(bookID): #this function makes the appropriate changes to database.txt and logfile.txt
    bookList = []
    f = open("databaseTEST.txt", "r+")
    for line in f:
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]:
            book[4] = memberID
            line = " ; ".join(book)
            bookList.append(line)
        else:
            book = " ; ".join(book)
            bookList.append(book)
    bookList.sort()
    line = '\n'.join(bookList)
    f.seek(0)
    f.truncate(0)
    f.write(line)
    f.close()
    
    d = open("logfileTEST.txt","a")
    f = open("databaseTEST.txt","r")
    today = input("Please enter the current date in format dd/mm/yyyy:\n:> ")
    for line in f:
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]:
            newLine = book[0]+" ; "+book[1]+" ; "+today+" ; ???"
    d.write("\n"+newLine)
    d.close()
    

def book_Availability():
    opt = 0
    f = open("databaseTEST.txt", "r")
    for line in f:
        s = line.strip()
        book = s.split(' ; ')
        if bookID == book[0]:
            opt = 1
            if book[4] == '0':
                print('- Book "'+book[1]+'" with ID-number',book[0]+', written by',book[2])
                print("- Availability: available to withdraw. Proceed with withdrawal?")
                print("\t (1) yes")
                print("\t (2) no")
                option = int(input(":> "))
                if option == 1:
                    print("Proceeding to withdraw...")
                    book_Checkout(bookID)
                    print("Withdrawal successful!")
                    print(">>>")
                elif option == 2:
                    print("Terminating...")
                    print(">>>")
                    break
                else:
                    break
            else:
                print('- Book "'+book[1]+'" with ID-number',book[0]+', written by',book[2])
                print("- Availability: unavailable to withdraw, book currently taken by member with ID-number",book[4])
                print(">>>")
    if opt == 0:
        print("Unfortunately, we don't have this book.")
        print(">>>")
    f.close()


book_Availability()

