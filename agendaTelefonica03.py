
from os import system

def displayMainMenu():
    print("** AddressBook **")
    print('*****************')
    print()
    print(MAIN_OP_ADD_NUMBER    ,               OP_MENU_SEPARATOR, menuText1)
    print(MAIN_OP_REMOVE_NUMBER    ,            OP_MENU_SEPARATOR,"Remove")
    print(MAIN_OP_SEARCH_NUMBER    ,            OP_MENU_SEPARATOR,"Search")
    print(MAIN_OP_PRINT_ADDRESSBOOK    ,        OP_MENU_SEPARATOR,"Display All")
    print(MAIN_OP_CHANGE_LANGUAGE    ,          OP_MENU_SEPARATOR,"Change language in ", language)
    print(MAIN_OP_SAVE  ,                       OP_MENU_SEPARATOR, "Save" )
    print(OP_EXIT    ,                          OP_MENU_SEPARATOR,"Exit Addressbook")

def menuActionAddContact():
    print("Your are adding a new contact")
    contactName = input("Enter the name of the new contact " )
    contactNumber = (input("Enter the phone number " ))  
    addContact = True 
    contactPoz = searchContactByName(contactName)
    if contactPoz != -1:
        print()
        print("Contact already present in addressbook")
        addIt = input("Do you want to add this one as well? Yes(Y) or No(N) ")
        if addIt == "No" or addIt == "N":
            replaceIt = input("Do you want to replace this existing number " + phoneNumbers[contactPoz] + " of " + names[contactPoz] + "? Yes(Y) or No(N)? " )
            if replaceIt.lower() == "Yes" or replaceIt == "Y":
                 deleteContact(contactPoz)
                 print("Old contact has been replaced")
            else:
                 addContact = False

    if addContact:
        names.append(contactName)
        phoneNumbers.append(contactNumber)
        print("The contact was successfully added")


def menuActionRemoveContact():
    contactName = input("Enter the name of the contact you want to be deleted:" )
    contactPoz = searchContactByName(contactName)
    if contactPoz == -1:
            contactNotFound()
    else:
        deleteContact(contactPoz)
        print("The contact was successfully removed")

def menuActionSearch():
    contactName = input("Enter the name of the contact you are looking for " )
    contactPoz = searchContactByName(contactName)
    if contactPoz == -1:
            contactNotFound()
    else:
            print(names[contactPoz], phoneNumbers[contactPoz])
    
def menuActionPrintAddressBook():
    for i in range(0, len(names)):
        print(names[i]+","+ phoneNumbers[i])    

def searchContactByName(contactName):
    n = len(names)
    contactNameLower = contactName.lower()
    poz = -1
    i = 0
    for i in range(n): 
        if names[i].lower() == contactNameLower:
            poz = i
            i = i + 1
            return poz
    return poz


def loadMenu(language):
    try:
        with open(PROGRAM_PATH + language + ".menu", "r") as file:
            global menuText1
            found = False
            for row in file:
                row = row.strip()  # Remove unnecessary spaces/newlines
                poz = row.find("=")

                if poz > -1:
                    key = row[:poz].strip()
                    value = row[poz + 1:].strip()
                    if key == "menuText1":
                        menuText1 = value
                        found = True
            
            if not found:
                print("Warning: 'menuText1' not found in the menu file for language", language)
    
    except FileNotFoundError:
        print("Error: Menu file for language", language, "not found!")

    file.close()

def menuActionChangeLanguage():
    global language
    if language == "en":
        language = "ro"
    else:
        language = "en"

    loadMenu(language)


def menuActionSave():
    file = open(PROGRAM_PATH + "agendaTelefonica.csv", "w") #comma separated values (csv)
    for i in range(0, len(names)):
        file.write(names[i]+","+ phoneNumbers[i] + "\n")
        print("Agenda a fost salvata cu succes")
    file.close()
     

def deleteContact(contactPoz):
    names.pop(contactPoz)
    phoneNumbers.pop(contactPoz)
def contactNotFound():
    print("Contact not found...")

PROGRAM_PATH = "C:\\pythonLearning\\agendaTelefonica\\"

OP_EXIT = 99
MAIN_OP_ADD_NUMBER = 1
MAIN_OP_REMOVE_NUMBER = 2
MAIN_OP_SEARCH_NUMBER = 3
MAIN_OP_PRINT_ADDRESSBOOK = 4
MAIN_OP_CHANGE_LANGUAGE = 5
MAIN_OP_SAVE = 6
OP_MENU_SEPARATOR = "--"

language = "en"

menuText1 = "Add new"

names = ["John", "Robert", "Bob", "Mihai", "Mircea"]
phoneNumbers = ["31231", "545454", "66645454", "22221111", "9090909"]

option = 0

while option != OP_EXIT:
    system("cls")
    displayMainMenu()

    option = int(input("Select an option number: "))
    if option == MAIN_OP_ADD_NUMBER:
        menuActionAddContact()

    if option == MAIN_OP_REMOVE_NUMBER:
        menuActionRemoveContact()

    if option == MAIN_OP_SEARCH_NUMBER:
        menuActionSearch()

    if option == MAIN_OP_PRINT_ADDRESSBOOK:
        menuActionPrintAddressBook()

    if option == MAIN_OP_CHANGE_LANGUAGE:
         menuActionChangeLanguage()
    
    if option == MAIN_OP_SAVE:
        menuActionSave()

    if option != OP_EXIT:
        input("Press Enter to continue")

print("Goodbye!")
