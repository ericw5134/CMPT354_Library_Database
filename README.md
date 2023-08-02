# CMPT354 Library Database

## Table of Contents

- [Project Info](#project-info)
- [Functions](#Functions)
- [How To Run](#Running)
- [Installation](#installation)

## Project Info
CMPT 354 Project - A Custom Library Database

Contributers:
- Eric Wang
- Roy Shi

## Functions

finditem()
* First, check if connnection to the database was established. Program terminates if connection was not established.
* The function then asks user to enter the itemID of the item the user wants to find using input().
* A query is then executed using the user's input as a parameter
* If found, the resulting tuple will be saved into variable **item** and returned. 
* If not found, an error message will print, and program terminates

borrowitem(): 
* First, check if connnection to the database was established. Program terminates if connection was not established.
* A transactionID primary key that determines this unique transaction will be given by choosing a random integer between 1 and 1000000.
* The function then asks user to enter some information using input(). Moreover, the borrowDate value will be today's date using the .today() function from the datetime library.
* A query is then executed using the user's input as parameters to register the user if needed.
* A query is then executed using the user's input as parameters to register the user's action into BorrowTransaction table.

returnitem()
* First, check if connnection to the database was established. Program terminates if connection was not established.
* The function then asks user to enter the transactionID this program provided when this item was borrowed.
* A query is then executed to delete the tuple with a matching transactionID from BorrowTransaction table.
* An error message will play if the transactionID was not in BorrowTransaction table.

donateitem()
* First, check if connnection to the database was established. Program terminates if connection was not established.
* The program will list the type of items user can donate.
* An itemID will be determined via choosing a random integer between 1 and 1000000.
* The user will then be asked to enter information about the item being donated
* A query is then executed using the user's input as parameters to register the item.
* An error message will play if the insert query failed.

findevent()
* First, check if connnection to the database was established. Program terminates if connection was not established.
* The function then asks user to enter the eventID of the event the user wants to find using input().
* A query is then executed using the user's input as a parameter
* If found, the resulting tuple will be saved into variable **event** and returned. 
* If not found, an error message will print, and program terminates

register()
* First, check if connnection to the database was established. Program terminates if connection was not established.
* The function then asks user to enter the eventID of the event the user wants to register for using input(), as well as the user's information.
* A query is then executed using the user's input as parameters to register the user if needed.
* A query is then executed using the user's input as parameters to register the user's action into EventAudiences table.
* An error message will play if insertion failed.

volunteer()
* First, check if connnection to the database was established. Program terminates if connection was not established.
* The function then asks user to enter some personal information.
* A query is then executed using the user's input as parameters to register the user if needed.
* A query is then executed using the user's input as parameters to register the user's action into Personnel table.
* An error message will play if insertion failed.

## Running
This project uses a CLI. Simply run main.py, and follow the printed messages. 

## Installation
Via https
```bash
git clone https://github.com/ericw5134/cmpt-354-project.git
cd cmpt-354-project
```
