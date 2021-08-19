from tkinter import *
import re

root = Tk()

root.title("Form Check")

entry1 = Entry(root, width = 25, borderwidth = 2)
entry2 = Entry(root, width = 25, borderwidth = 2)
entry3 = Entry(root, width = 25, borderwidth = 2)
entry4 = Entry(root, width = 25, borderwidth = 2)
entry5 = Entry(root, width = 25, borderwidth = 2)

label1 = Label(text = "First Name")
label2 = Label(text = "Last Name")
label3 = Label(text = "Birthdate")
label4 = Label(text = "Phone Number")
label5 = Label(text = "Email Address")

label1.grid(row = 1, column = 2)
label2.grid(row = 3, column = 2)
label3.grid(row = 5, column = 2)
label4.grid(row = 7, column = 2)
label5.grid(row = 9, column = 2)

entry1.grid(row = 2, column = 2)
entry2.grid(row = 4, column = 2)
entry3.grid(row = 6, column = 2)
entry4.grid(row = 8, column = 2)
entry5.grid(row = 10, column = 2)

sendText = Label(text = "")
sendText.configure(font = ("Helvetica", 36, "bold"))

submitButton = Button(root, text = "SUBMIT", padx = 40, pady = 20)
submitButton.grid(row = 12, column = 2)

def firstNameCheck():
    firstNameLength = len(str(entry1.get()))
    if firstNameLength <= 20 and firstNameLength >= 2:
        print("right first name!")
        return True
    else:
        print("incorrect first name")
        return False

def lastNameCheck():
    lastNameLength = len(str(entry2.get()))
    if lastNameLength <= 20 and lastNameLength >= 2:
        print("right last name!")
        return True
    else:
        print("incorrect last name")
        return False

def birthdateCheck():
    stringToTest = str(entry3.get())

    separator = re.split("\.", stringToTest)

    day = separator[0]
    month = separator[1]
    year = separator[2]

    if int(day) > 0 and int(day) <= 31:
        if int(month) > 0 and int(month) <=12:
            if int(year) > 1900 and int(year) <= 2006:
                print("birthdate successful")
                return True
    else:
        return False

def numberCheck():
    count = 0
    phoneNumber = int(entry4.get())

    while(phoneNumber > 0):
        phoneNumber = phoneNumber//10
        count = count + 1
    
    if count == 9:
        print("right length!")
        return True
    else:
        print("incorrect phone number")
        return False

def emailCheck():
    stringToTest = str(entry5.get())

    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(fi|com|net|edu)"

    if (re.search(pattern, stringToTest)):
        print("valid email")
        return True
    else:
        print("invalid email")
        return False

def checkAll():
    if firstNameCheck() == True and lastNameCheck() == True and birthdateCheck() == True and numberCheck() == True and emailCheck() == TRUE:
        submitButton.configure(state = NORMAL)
        return TRUE
    else:
        return FALSE
    
def submit():
    if checkAll() == TRUE:
        print("form sent!")
        sendText.grid(row = 6, column = 2)
        sendText.configure(text = "FORM SENT!")
        return TRUE
    else:
        print("check fields!")
        sendText.grid(row = 14, column = 2)
        sendText.configure(text = "CHECK FIELDS!")
        return False

submitButton.configure(command = submit)

root.mainloop()