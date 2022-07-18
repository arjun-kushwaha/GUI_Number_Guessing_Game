from tkinter import *
import random
from tkinter import messagebox as msg

root = Tk()

#title for main page
root.title("Number Guessing Game ")

#icon of game
root.wm_iconbitmap('game.ico')

# window size
root.geometry('500x500')

#making non-resizable
root.resizable(0,0)

#background color
root.configure(bg='#e3ebfa')

# settings new limits of upper and lower guess 
def limit(w):

    #making global variable
    global randomvalue, count, l, lower, upper, m, n 

    #fetching values from entry box
    m=int(lower.get())
    n=int(upper.get())

    #regenerating random value at custom upper and lower limits
    randomvalue = random.randint(m,n)

    # changing label text of home page with custom range 
    l.configure(text=f"Guess a Number between {m} to {n} ")

    #popup message box
    msg.showinfo("Set Current Game Limits","Current Game Limit has been set ! ")

    #initializing empty entry box
    upper.set('')
    lower.set('')

    #destroying settings window
    w.destroy()
    playAgain()


def playAgain():
    global randomvalue, count, n, m

    #regenerating random value at custom upper and lower limits
    randomvalue = random.randint(m,n)
    count = 0

    # removing hint too low/ too high
    result.configure(text="") 

    #initializing empty entry box
    var.set("")   

    #enable submit button
    b1.config(state='normal')

def getval():
    global count
    count += 1

    #checking whether entry box is empty or not
    if var.get() != "":

        #fetching value from var
        guessnumber = int(var.get())

        # checking entered value matching or not
        if guessnumber == randomvalue:
            result.configure(text=f" Number was {randomvalue} ! \n \n Congrates !! You Guessed in {count} times", fg = '#046e0c')
            var.set("")

            # button disable 
            b1.config(state='disabled')

            # cheking hints for low or high number
        else:
            if guessnumber < randomvalue:
                result.configure(text="Too low ", fg = '#e00b87') 
                var.set("")        
            else:
                result.configure(text="Too High ", fg = 'red') 
                var.set("")     
def settings():
    global upper, lower

    # creating new windows for settings
    newWindow = Toplevel(root)

    #title for settings page 
    newWindow.title("New page")

    #window size for settings page
    newWindow.geometry("300x300")

    # making non-resizable
    newWindow.resizable(0,0)

    #icon of setting page
    newWindow.wm_iconbitmap('game.ico')
    # title for setting page
    newWindow.title("Set Upper Guess limit ")

    #setting page background
    newWindow.configure(bg='#e3ebfa')
    #text label
    l21 = Label(newWindow,text='Enter Lower Range', bg='#e3ebfa')
    l21.place(x=75,y=10)

    #entrybox for lower range
    e=Entry(newWindow,textvariable=lower)
    e.place(x=75,y=40)

   #label text
    l22 = Label(newWindow,text='Enter Upper Range', bg='#e3ebfa')
    l22.place(x=75,y=70)

     #entrybox for upper range
    e21=Entry(newWindow,textvariable=upper)
    e21.place(x=75,y=100)

    #submit button 
    b21 = Button(newWindow,text='Submit',bg='#363369', fg='white', command=lambda:limit(newWindow))
    b21.place(x=115,y=130)

    #developer details
    developer = Label(newWindow,text='Developed by:Arjun Kushwaha \n feedback : arjunkushwahaji@gmail.com',font=" '' 9 italic",bg='#e3ebfa')
    developer.place(x=10,y=250)
   
n=m=0

upper=StringVar()
lower=StringVar()
var = StringVar()

randomvalue = random.randint(1,100)
count = 0
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

#new game button
b2 = Button(root,text='New Game',bg='red', fg='white', command=playAgain)
b2.place(x=410,y=460)

#settings button
b3 = Button(root,text='Settings',bg='red', fg='white', command=settings)
b3.place(x=430,y=10)

#about developer
developer = Label(text='Developed by:Arjun Kushwaha',font=" '' 9 italic",bg='#e3ebfa')
developer.place(x=10,y=470)

root.mainloop()