import sqlite3
from utilities import finditem, borrowitem, returnitem, donateitem, findevent, regirster, volunteer, ask_librarian_for_help

def main():
    actions = ["Find item", "Borrow item", "Return item", "Donate item", "Find event", 
    "Register for event", "Volunteer for us", "Ask for help from librarian", "Exist program"]
    # keywords = ["findItem", "borrow", "return", "donate", "findEvent", "register", "volunteer", "quit"]

    print("\nWelcome to the library! Here are List of actions below:\n")

    while True:
        for i in range(1,10):
            print("   ", i, ". ", actions[i-1], sep='')
        print("\n")

        userAction = input("what would you like to do (enter number 1~9): ") 
        print("\n")

        if userAction == '1':
            foundItem = finditem()
            if foundItem:
                for i in range(len(foundItem)):
                    print("\n---------------------------------------")
                    print("Title:          ", foundItem[i][2], sep="")
                    print("Author:         ", foundItem[i][3], sep="")
                    print("Type:           ", foundItem[i][1], sep="")
                    print("Publisher:      ", foundItem[i][4], sep="")
                    print("Release Date:   ", foundItem[i][5], sep="")
                    print("---------------------------------------")
                    # print("\n   ", foundItem[i], sep='')
            else:
                print("ERROR: Failed to find item")
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '2':
            transactionID = borrowitem()
            print("Your TransactionID is: " + str(transactionID) + ", please remember it and return back after a month.")
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '3':
            returnitem() 
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '4':
            itemID = donateitem()
            print("Your itemID is: " + str(itemID) + ", please remember it.")
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '5':
            foundevent = findevent()
            if foundevent:
                for i in range(len(foundevent)):
                    print("\n---------------------------------------")
                    print("Type:       ", foundevent[i][1], sep="")
                    print("Price:      ", foundevent[i][2], sep="")
                    print("Room:       ", foundevent[i][3], sep="")
                    print("---------------------------------------")
            else:
                print("ERROR: Failed to find event")
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '6':
            regirster()
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '7':
            volunteer()
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '8':
            ask_librarian_for_help()
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '9':
            return

        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()