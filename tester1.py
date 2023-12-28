from tkinter import *
import time
import random
windows = Tk()
windows.geometry('1000x360')
windows.title('Морской бой')

#Противник
def butb():
    windowst = Tk()
    windowst.geometry('1000x360')
    windowst.title('Морской бой:противник')
    buttonsl = [Button(windowst,width=7,height=4,font=('Times New Roman',9, 'bold'),command= lambda  x = i:Player2(x))for i in range(50)]
    nazv = Label(windowst,text='Ваш противник',font=('Times New Roman',16))
    nazv.place(rely=0.2, relx=0.7)
    buttonsw.destroy()
    
    def Player2(bot):
        
        gamelo= [None]*50
        gameb =list(range(50))
       
        gameb[bot]='X'
        buttonsl[bot].config(text='X',state= 'disabled')
        gamelo.remove(bot)
        if gameb[bot]!= gameb[t]:
            buttons[bot].config(text='X',state= 'disabled')
        
        t=random.randint(gamelo)
        gameb[t]=' '
        buttonsl[t].config(text=' ')
    ow = 1
    ol = 0
    for i in range(50):
        buttonsl[i].grid(row=ow,column=ol)
        ol += 1
        if ol ==10:
            ow +=1
            ol=0
   
#Пользователь
gamel= [None]*50
game =list(range(50))

def Player1(w):
    global turn
    global gamel
    global game
    
    game[w]='■'
    buttons[w].config(text='■',state='disabled')
    gamel.remove(w)
    if w == range(50):
        t = random.choice(gamel)
        game[t]='X'
        time.sleep(0.5)
        buttons[t].config(text='X',state='disabled')

nazv1 = Label(windows,text=' ')
nazv1.place(rely=0.3,relx=0.7)
buttons = [Button(windows,width=7,height=4,font=('Times New Roman',9, 'bold'),command= lambda  x = i:Player1(x))for i in range(50)]
buttonsw = Button(windows,text='Начать игру',width=10,height=5,command=butb)
buttonsw.place(rely=0.5,relx=0.7)



row = 1
col = 0
for i in range(50):
    buttons[i].grid(row=row,column=col)
    col += 1
    if col ==10:
        row +=1
        col=0






windows.mainloop()

