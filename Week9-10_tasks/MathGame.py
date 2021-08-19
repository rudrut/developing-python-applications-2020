from tkinter import *
from tkinter.font import Font
from playsound import playsound
import random

root = Tk()

root.title("Math Game")

e = Entry(root, width=25, borderwidth=2)
e.grid(row=2, column=2)
e.insert(END, 0)

answerText = Label(text="")
answerText.configure(font=("Helvetica", 36, "bold"))


def reset():
    answerText.configure(text="")
    button_reset.configure(text="GENERATE NEW")
    e.delete(0, END)
    e.insert(END, 0)
    global random_variable_1
    global random_variable_2
    random_variable_1 = random.randint(0, 20)
    random_variable_2 = random.randint(0, 20)

    global label_1
    global label_2
    global label_3
    label_1 = Label(text=random_variable_1)
    label_2 = Label(text=random_variable_2)
    label_3 = Label(text='+')

    global correctAnswer
    correctAnswer = random_variable_1 + random_variable_2
    label_1.grid(row=1, column=1)
    label_2.grid(row=1, column=3)
    label_3.grid(row=1, column=2)
    button_check = Button(root, text="CHECK ANSWER",
                          padx=40, pady=20, command=click_answer)
    button_check.grid(row=4, column=2)


def click_answer():
    proposal = int(e.get())
    print(proposal)
    if proposal == correctAnswer:
        print("YAY!")
        answerText.grid(row=6, column=2)
        answerText.configure(text="CORRECT!")
        playsound("fanfare.mp3")
    else:
        print("TRY AGAIN!")
        playsound("chainsaw.mp3")
        answerText.configure(text="WRONG!")
        answerText.grid(row=6, column=2)


button_reset = Button(root, text="START GAME", padx=40, pady=20, command=reset)
button_reset.grid(row=3, column=2)

root.mainloop()
