import random
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
# user1="user"
# user2="computer"

bot_score=0
user_score=0

def click(userChoice,name,root,canvas):
    list1=["rock","paper","scissors"]
    botChoice = random.choice(list1)
    winnner=compare(userChoice,botChoice)

    if (bot_score <= 5 or user_score <= 5):
        
        if winnner=='tie':
         messagebox.showinfo("It's a Tie ! ", )
        
        elif winnner == 'bot' :
            
            messagebox.showinfo("Score", ("Bot wins !\n"+"bot="+str(bot_score)+"\n"+name+"="+str(user_score)))

        elif winnner == 'user' :
            
            messagebox.showinfo("Score", (name+" wins!"+"\n"+"bot="+str(bot_score)+"\n"+name+"="+str(user_score)))
    
    else:
        canvas.destroy()
        canvas3 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
        canvas3.pack()
        if(bot_score>user_score):

            
            lbl=Label(root, text = 'LOSER')
            canvas3.create_window(200, 50, window=lbl)
        else:
            lbl=Label(root, text = "WINNER")
            canvas3.create_window(200, 50, window=lbl)

        

        


def onClick(canvas,root,name):
    canvas.destroy()
    name=name.get()
    gameScreen(root,name)

def gameScreen(root,name):
    canvas2 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
    canvas2.pack()

    lbl=Label(root, text = name + " , Let's Play !")
    canvas2.create_window(200, 50, window=lbl)
    
    stonePhoto = PhotoImage(file = "rock.png").subsample(10,10) 
    stoneBtn=Button(root,image=stonePhoto,command=lambda:click('rock',name,root,canvas2))
    stoneBtn.image=stonePhoto
    canvas2.create_window(100, 100, window=stoneBtn)
    
    paperPhoto = PhotoImage(file = "paper.png").subsample(10,10)  
    paperBtn=Button(root, text = "paper",image=paperPhoto,command=lambda:click('paper',name,root,canvas2))
    paperBtn.image=paperPhoto
    canvas2.create_window(200, 100, window=paperBtn)
    
    scissorsPhoto = PhotoImage(file = "scissors.png").subsample(10,10) 
    scissorBtn=Button(root, text = "scissor",image=scissorsPhoto,command=lambda:click('scissors',name,root,canvas2))
    scissorBtn.image=scissorsPhoto
    canvas2.create_window(300, 100, window=scissorBtn)

    
        
        


    




def gui():
    
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
    canvas1.pack()

    label2 = tk.Label(root, text='Enter your Name:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label2)

    entry1 = tk.Entry(root) 
    canvas1.create_window(200, 140, window=entry1)

    
    button1 = tk.Button(text='OK', command=lambda:onClick(canvas1,root,entry1), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)

    root.mainloop()




def compare(user,bot):
    
    global bot_score
    global user_score
    
    print('user input :'+user)
    print('bot input : '+bot)
    
    if user==bot:
        return('tie')

    elif user=='rock':
        
        if bot=="paper":
            bot_score = bot_score + 1
            return('bot')

        elif bot=="scissors":
            user_score = user_score + 1
            return('user')
    
    elif user=='paper':
        
        if bot=="scissors":
            bot_score = bot_score + 1
            return('bot')

        elif bot=="rock":
            user_score = user_score + 1
            return('user')

    elif user=='scissors':
        
        if bot=="rock":
            bot_score = bot_score + 1
            return('bot')

        elif bot=="paper":
            user_score = user_score + 1
            return('user')







if __name__ == '__main__':
    
    gui()
    

	