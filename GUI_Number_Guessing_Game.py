from tkinter import *
import random

root = Tk()

#title
root.title("Number Guessing gmae ")

#icon
root.wm_iconbitmap('game.ico')
root.geometry('500x500')

#non resizable
root.resizable(0,0)
root.configure(bg='#e3ebfa')

#newGame function
def playAgain():
    global randomvalue
    global count

    #regenrate randomvalue
    randomvalue = random.randint(1,100)

    # re-starting count
    count = 0

    #making Entry widgets Empty by initializing ""
    result.configure(text="") 
    var.set("")   
    #submit button normal
    b1.config(state='normal')

#function to check whether number is low or high or same to computer generated no.
def getval():

    #count number of attemption 
    global count
    count += 1

    #checking whether input field is  empty or not
    if var.get() != "":

        #fetching value
        guessnumber = int(var.get())

        # checking user input value is equal to computer generated value or not 
        if guessnumber == randomvalue:
            result.configure(text=f" Number was {randomvalue} ! \n \n Congrates !! You Guessed in {count} times", fg = '#046e0c')
            var.set("")

            #submit button disable
            b1.config(state='disabled')
        
        #showing hint whether guessing number is low or high
        else:
            if guessnumber < randomvalue:
                result.configure(text="Too low ", fg = '#e00b87') 
                var.set("")        
            else:
                result.configure(text="Too High ", fg = 'red') 
                var.set("")     

#generating Random value
randomvalue = random.randint(1,100)

count = 0
var = StringVar()
#home page 
l1 = Label (text="Number Guessing Game ", font= "Arial 20 bold", fg = '#363369' , bg='#e3ebfa' )
l1.pack(pady=30)

l = Label(text="Guess a Number between 0 to 100 ",font= "Arial 12 " , bg='#e3ebfa')
l.pack()

e1 = Entry(root, font="Arial 15 bold ", textvariable=var)
e1.pack(pady=15, padx=20)

#submit button
b1 = Button(root,text='Submit',bg='#363369', fg='white', command=getval, font="Arial 10 bold", width=12, height=1)
b1.pack()

result = Label(text='',font= "Arial 15 bold " , bg='#e3ebfa' )
result.pack(pady=20)

#Adding newGame button
b2 = Button(root,text='New Game',bg='red', fg='white', command=playAgain)
b2.place(x=400,y=450)

#showing developer details
developer = Label(text='Developed by:Arjun Kushwaha',font=" '' 8 italic",bg='#e3ebfa')
developer.place(x=10,y=470)

root.mainloop()