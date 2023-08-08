#Title: WhatABook_Console_application.py
#Author: Tatyana Romanova
#Date: 08/04/2023
#Description:  Module 11 / Assignment: Write the Python code to support the business requirements of WhatABook assiignment. 


#import statements ~
import simple_colors
import sys
import mysql.connector
from mysql.connector import errorcode


#database config object~
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


def show_menu():
    print("    ~~ Main Menu ~~\n")
    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n\n    4. Exit Program\n")
    try:
        choice = int(input('      <Please choose one option from above>: '))
        return choice
    except ValueError:
        print("\n  Invalid Input, program will close...\n")
        sys.exit(0)

def show_books(cursor):
    #query ~
    cursor.execute("SELECT book_id, book_name, author, details from book")
    #get the results from the cursor object ~
    books = cursor.fetchall()
    print("\n  ~~ LIST OF AVALABLE BOOKS ~~")  
    #iterate over the player data set and display the results ~
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store")
    locations = cursor.fetchall()
    print("\n  ~~~  STORE LOCATIONS ~~~")
    for location in locations:
                print("  Locale: {}\n".format(location[1]))

def validate_user():
    #validate the users ID~
    try:
        user_id = int(input('\n      Enter your id <id1=1 | id2=2 | id3=3>: '))
        if user_id < 0 or user_id > 3:
            print("\n  Invalid Input number, program will close...\n")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\n  Invalid Input, program will close...\n")
        sys.exit(0)

def show_account_menu():
    #cursor.execute("SELECT user_id, first_name,last_name FROM user ")
    #bookz = cursor.fetchall()
    #
    #display the users account menu~
    try:
        print("\n      ~~ Customer Menu ~~ \n")
        #for id in bookz:
            #print("          ~~   Name: {}   ~~ )\n".format(bookz[0]))
        
        
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu\n")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))
        return account_option
    except ValueError:
        print("\n  Incorect Imput, program will close...\n")
        sys.exit(0)

def show_wishlist(cursor, _user_id):
    #query the database for a list of books added to the users wishlist~

    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = cursor.fetchall()
    print("\n        ~~~ WISHLIST ITEMS ~~~\n")
    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(cursor, _user_id):
    #query the database for a list of books not in the wishlist of users~
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    cursor.execute(query)
    books_to_add = cursor.fetchall()
    print("\n        ~~~ AVAILABLE BOOKS ~~~")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(cursor, _user_id, _book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    #try/catch potential database errors~
    #connect to database true Config Section~
    db = mysql.connector.connect(**config)  
    #queries
    cursor = db.cursor() 
    print("\n  ~~ WhatABook Application! ~~ ")
    #show the main menu~
    user_selection = show_menu() 

    #while the user's selection is not 4
    while user_selection != 4:

        #if the user selects option 1, call the show_books method and display the books~
        if user_selection == 1:
            show_books(cursor)

        #if the user selects option 2, call the show_locations method and display the configured locations~
        if user_selection == 2:
            show_locations(cursor)

        #if the user selects option 3, call the validate_user method to validate the entered user_id~
        #call the show_account_menu() to show the account settings menu~
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            #while account option does not equal 3
            while account_option != 3:
                #if the use selects option 1, call the show_wishlist() method to show the current users 
                #configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                #if the user selects option 2, call the show_books_to_add function to show the user 
                #the books not currently configured in the users wishlist
                if account_option == 2:
                    #show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)
                    #get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    #add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    #cursor.execute("SELECT first_name, last_name FROM user  ")
                    #bookuser = cursor.fetchall()
                    #commit the changes to the database 
                    db.commit() 
                    print("\n        Book id: {} was added to your wishlist!".format(book_id))
                    #print("          ~~ {} ~~ \n".format(bookuser[1]))
                #if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please try another option...")
                #show the account menu 
                account_option = show_account_menu()      
        #if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid Input, please try again ...")           
        #show the main menu
        user_selection = show_menu()
    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    #handle errors~ 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The imputed username or password are incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    #close the connection with Database~
    db.close()

