import sqlite3
from utilities import finditem, borrowitem, returnitem, donateitem, findevent, regirster, volunteer

def main():
    actions = ["find item", "borrow item", "return item", "donate item", "find event", 
    "register for event", "volunteer for us", "exist program"]
    keywords = ["findItem", "borrow", "return", "donate", "findEvent", 
    "register", "volunteer", "quit"]

    print("\nWelcome to the library! Here are List of actions below:\n")

    while True:
        for i in range(1,9):
            print("   ", i, ". ", actions[i-1], sep='')
        print("\n")

        userAction = input("what would you like to do (enter number 1~8): ") 
        print("\n")

        if userAction == '1':
            foundItem = finditem()
            if foundItem:
                for i in range(len(foundItem)):
                    print("\n   ", foundItem[i], sep='')
            else:
                print("ERROR: Failed to find item")
            print("\nAnything more we can assist with? Here are list of actions below\n")

        elif userAction == '2':
            transactionID = borrowitem()
            print("Your TransactionID is: " + str(transactionID) + ", please remember it.")
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
                    print(foundevent[i])
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
            return

        else:
            print("ERROR: Keyword not detected")

if __name__ == "__main__":
    main()