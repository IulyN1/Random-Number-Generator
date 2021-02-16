# Random number generator

from tkinter import *
import random

#creating the window for the app
window = Tk()
window.title("Random number generator")

#creating the title with the instructions as a label
Label(window,text="Type the lowest and highest number and press the button to generate a random number "+
    "within that range.", fg="black", font="none 16 bold").grid(row=0 ,column=0, sticky=W, columnspan=2)

#creating a label "MIN:" and its entry field for the input of the lowest number 
Label(window,text="MIN:", font="none 16 bold").grid(row=1 ,column=0, sticky=W)
text_entry_min = Entry(window, width=10, bg="grey", fg="white", font="none 16 bold")
text_entry_min.place(x=70, y=30)

#creating a label "MAX:" and its entry field for the input of the highest number 
Label(window,text="MAX:", font="none 16 bold").grid(row=2 ,column=0, sticky=W)
text_entry_max = Entry(window, width=10, bg="grey", fg="white", font="none 16 bold")
text_entry_max.place(x=70, y=60)

def click():
    '''
    This function inserts in the output field the random number if the input data is correct.
    If it isn't, it inserts a "Invalid number given!" message.
    '''
    output.delete(0,END)
    minim = text_entry_min.get()
    maxim = text_entry_max.get()
    try:
        number = random.randint(int(minim),int(maxim))
    except ValueError:
        output.insert(0,"Invalid number given!")
        return
    output.insert(0,number)

#create the button which generates the random number
generate_button = Button(window, text="Generate random number", font="none 16 bold", command=click, bg="yellow")
generate_button.grid(row=3, column=0, sticky=W)

#create the label "Output:" and the field where the result is printed in
Label(window,text="Output:", font="none 16 bold", pady=10).grid(row=4 ,column=0, sticky=W)
output = Entry(window,text="", font="none 16 bold", bg="red", fg="black", width=20)
output.place(x=90, y=140)

# run the main app
window.mainloop()
