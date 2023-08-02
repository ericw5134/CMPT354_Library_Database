import sqlite3
import random
from datetime import date

conn = sqlite3.connect('library.db')

def finditem():  

    if not conn:
        print("ERROR: Failed to connect to database, exiting program")
        return
    
    inputItemID = input("Enter the itemID of the item you are looking for: ")
    
    cursor = conn.cursor()
    query = "SELECT * FROM Item AS I WHERE I.itemID=:input"
    try: 
        cursor.execute(query, {"input": inputItemID})
    except sqlite3.IntegrityError:
        print("Error: This item is not in our database")
    item = cursor.fetchall()

    conn.close()

    return item

def borrowitem():   

    if not conn:
        print("Failed to connect to database, exiting program")
        return

    transactionID = random.randint(1, 1000000)
    itemID = input("Enter the itemID of the item you are borrowing: ")
    personID = input("Enter your personID: ")
    firstName = input("What is your first name: ")
    lastName = input("What is your last name: ")
    contactNumber = input("What is your contact number (xxx-xxx-xxxx format): ")
    email = input("What is your email: ")
    borrowDate = date.today()

    cursor = conn.cursor()
    query = "INSERT INTO Person(personID, firstName, lastName, contactNumber, email) VALUES(?,?,?,?,?)"
    try:
        cursor.execute(query, (personID, firstName, lastName, contactNumber, email))
        conn.commit()
    except sqlite3.IntegrityError:  # this person's personID is already in database 
        pass
    query = "INSERT INTO BorrowTransaction(transactionID, itemID, personID, borrowDate, returnDate, fineAmount) VALUES(?, ?, ?, ?, NULL, NULL)"
    try: 
        cursor.execute(query, (transactionID, itemID, personID, borrowDate))
        conn.commit()
    except sqlite3.IntegrityError:
        print("ERROR: There was a problem retrieving your item from the dabase!\n")

    conn.close()

    return transactionID

def returnitem():

    if not conn:
        print("Failed to connect to database, exiting program")
        return

    transactionID = input("What was the transactionID you were provided: ")

    cursor = conn.cursor()
    query = "DELETE FROM BorrowTransaction WHERE transactionID=:input"
    try:
        cursor.execute(query, {"input": transactionID})
        conn.commit()
    except sqlite3.IntegrityError:
        Print("Error: This item was never borrowed")
    
    conn.close()
    return

def donateitem():
    
    if not conn:
        print("Failed to connect to database, exiting program")
        return
    
    types = ['Print Book', 'Online Book', 'Magazine', 'Scientific Journal', 'CD', 'Record']
    print("These are the types of items you can donate:")
    for i in range(len(types)):
        print(types[i])
    print("\n")
    itemID = random.randint(1, 1000000)
    itemType = input("Which type of item would you like to donate: ")
    title = input("Please provide the title of this item: ")
    author = input("Please provide the author of this item: ")
    publisher = input("Please provide the publisher of this item: ")
    releaseDate = input("Please provide the release date of this item in the following format - yyyy-mm-dd : ")
    
    cursor = conn.cursor()
    query = "INSERT INTO Item(itemID, itemType, title, author, publisher, releaseDate) VALUES(?, ?, ?, ?, ?, ?)"
    try:
        cursor.execute(query, (itemID, itemType, title, author, publisher, releaseDate))
        conn.commit()
    except sqlite3.IntegrityError:
        print("ERROR: There was a problem adding your item to the dabase!\n")
    
    conn.close()

    return itemID

def findevent():
    
    if not conn:
        print("Failed to connect to database, exiting program")
        return   

    eventID = input("Enter the eventID of the event you are looking for: ")
    
    cursor = conn.cursor()
    query = "SELECT * FROM Event AS E WHERE E.eventID=:input"
    try: 
        cursor.execute(query, {"input": eventID})
    except sqlite3.IntegrityError:
        print("Error: Could not find this event.")
    event = cursor.fetchall()

    conn.close()

    return event

def regirster(): 

    if not conn:
        print("Failed to connect to database, exiting program")
        return   

    eventID = input("Enter the eventID of the event you want to register for: ")
    audienceID = input("Enter you personID to register: ")
    firstName = input("What is your first name: ")
    lastName = input("What is your last name: ")
    contactNumber = input("What is your contact number (xxx-xxx-xxxx format): ")
    email = input("What is your email: ")

    cursor = conn.cursor()
    query = "INSERT INTO Person(personID, firstName, lastName, contactNumber, email) VALUES(?,?,?,?,?)"
    try:
        cursor.execute(query, (personID, firstName, lastName, contactNumber, email))
        conn.commit()
    except sqlite3.IntegrityError:  # this person's personID is already in database 
        pass
    query = "INSERT INTO EventAudiences(eventID, audienceID) VALUES(?,?)"
    try:
        cursor.execute(query, (eventID, audienceID))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: A problem occured during registeration.")

    conn.close()

    return

def volunteer():

    if not conn:
        print("Failed to connect to database, exiting program")
        return
    
    print("Thank you! Let's collect some personal information first.")
    personID = input("What is your personID: ")
    firstName = input("What is your first name: ")
    lastName = input("What is your last name: ")
    contactNumber = input("What is your contact number (xxx-xxx-xxxx format): ")
    email = input("What is your email: ")

    cursor = conn.cursor()
    query = "INSERT INTO Person(personID, firstName, lastName, contactNumber, email) VALUES(?,?,?,?,?)"
    try:
        cursor.execute(query, (personID, firstName, lastName, contactNumber, email))
        conn.commit()
    except sqlite3.IntegrityError:  # this person's personID is already in database 
        pass
    
    query = "INSERT INTO Personnel(personnelID, jobTitle) VALUES(?,?)"
    try: 
        cursor.execute(query, (personID, 'volunteer'))
        conn.commit()
    except sqlite3.IntegrityError:
        print("ERROR: There was a problem adding your information to the dabase!\n")
    
    conn.close()

    return




