from tkinter import *
import time
import random
windows = Tk()
windows.geometry('1980x1200')
windows.title('Морской бой')


game =list(range(50))
def BOT():
    global game
    buttonsl = [Button(windows,width=7,height=4,font=('Times New Roman',9, 'bold'),command=lambda x = i: Player2(x))for i in range(50)]
    row = 1
    col = 12
    pust = Label(windows,text='          ')
    pust.grid(row=1,column=11)
    for i in range(50):
        buttonsl[i].grid(row=row,column=col)
        col += 1
        if col ==22:
            row +=1
            col=12
   
    
    nazv2 = Label(windows,text=':ваш противник',font=('Times New Roman',16))
    nazv2.grid(row=3,column=53)
    
    def Player2(l):
        
        global game
        v = random.randint(0,50)
        game[v]='X'
        buttons[v].config(text='X',state='disabled')
        
        tt = random.randrange(0,50)
        t = random.randrange(0,50)
        game[l]='X'
        game[tt]='  '
        game[t]=' '
       
        for  k in range(t):
            buttonsl[k].config(text=' ')
            if  game[l] != game[t]:
                buttonsl[l].config(text='X',state= 'disabled')
        for kk in range(tt):
            buttonsl[kk].config(text='  ')
            if game[l] != game[tt]:
                buttonsl[l].config(text='-',state='disabled')
        time.sleep(0.5)
        
def Player1(w):
   
    global game
    game[w]= '■'
    buttons[w].config(text='■',state='disabled')
    
nazv1 = Label(windows,text='          ')
nazv1.grid(row=2,column=11)
buttons = [Button(windows,width=7,height=4,font=('Times New Roman',9, 'bold'),command= lambda  x = i:Player1(x))for i in range(50)]

buttonsw = Button(windows,text='Начать игру',width=20,height=5,command=BOT)
buttonsw.place(relx=0.5,rely=0.7)



row = 1
col = 0
for i in range(50):
    buttons[i].grid(row=row,column=col)
    col += 1
    if col ==10:
        row +=1
        col=0






windows.mainloop()

