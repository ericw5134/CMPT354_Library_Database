import sqlite3
from utilities import finditem, borrowitem, returnitem, donateitem, findevent, regirster, volunteer

actions = ["find item", "borrow item", "return item", "donate item", "find event", 
"register for event", "volunteer for us"]
keywords = ["findItem", "borrow", "return", "donate", "findEvent", 
"register", "volunteer"]

print("List of actions below")
for i in range(7):
    print(actions[i] + " uses keyword: " + keywords[i])

userAction = input("what would you like to do (enter keyword): ") 
print("\n")

if userAction == "findItem":
    foundItem = finditem()
    if foundItem:
        for i in range(len(foundItem)):
            print(foundItem[i])
    else:
        print("ERROR: Failed to find item")
    print("Ok, everything is done. Thank you for your time!")

elif userAction == "borrow":
    transactionID = borrowitem()
    print("Your TransactionID is: " + str(transactionID) + ", please remember it.")
    print("Ok, everything is done. Thank you for your time!")

elif userAction == "return":
    returnitem() 
    print("Ok, everything is done. Thank you for your time!")

elif userAction == "donate":
    itemID = donateitem()
    print("Your itemID is: " + str(itemID) + ", please remember it.")
    print("Ok, everything is done. Thank you for your time!")

elif userAction == "findEvent":
    foundevent = findevent()
    if foundevent:
        for i in range(len(foundevent)):
            print(foundevent[i])
    else:
        print("ERROR: Failed to find event")
    print("Ok, everything is done. Thank you for your time!")

elif userAction == "register":
    regirster()
    print("Ok, everything is done. Thank you for your time!")

elif userAction == "volunteer":
    volunteer()
    print("Ok, everything is done. Thank you for your time!")

else:
    print("ERROR: Keyword not detected")
