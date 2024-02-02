from tkinter import *
import time
import random

windows = Tk()
windows.geometry('1980x1200')
windows.title('Морской бой')

#массивы
game1 = list(range(50))
game2=list(range(50))
game3 = list(range(50))
game4 =list(range(50))
game5 = list(range(50))

def GAME():
    nazv1.config(text= '             ')
    buttonsw.config(text='Повтор')
    buttons = [Button(windows,width=7,height=4,font=('Times New Roman',9, 'bold'),command= lambda  x = i:Player1(x))for i in range(50)]
    buttonsl = [Button(windows,width=7,height=4,font=('Times New Roman',9, 'bold'),command= lambda x = i: Player2(x))for i in range(50)]
    
    #моё поле
    row = 1
    col = 0
    for i in range(50):
        buttons[i].grid(row=row,column=col)
        col += 1
        if col ==10:
            row +=1
            col=0
    
    #поле противника
    row = 1
    col = 12
    pust = Label(windows,text='          ')
    pust.grid(row=3,column=11)
    for i in range(50):
        buttonsl[i].grid(row=row,column=col)
        col += 1
        if col ==22:
            row +=1
            col=12
    
   
    nothing = random.randrange(0,26) 
    shipsenemy = random.randrange(0,26)
    nothing2 = random.randrange(26,49)
    shipsenemy2 = random.randrange(26,49)
    
    nazv3 = Label(windows,text='                       ')
    nazv3.grid(row=1,column=11)
    nazv2 = Label(windows,text=':ваш противник',font=('Times New Roman',16))
    nazv2.grid(row=3,column=53)

    
    #вторая половина поля
    
    for item2 in range(game2[shipsenemy2]):
        buttonsl[item2].config(text='X')
        

    for item3 in range(game5[nothing2]):
        buttonsl[item3].config(text=' ')

    #первая половина поля
    for item in range(game3[shipsenemy]):
        buttonsl[item].config(text='X')
       
            
    for item1 in range(game4[nothing]):
        buttonsl[item1].config(text=' ')
    
        
    def Player1(w):
        
        game1[w]= '■'
        buttons[w].config(text='■',state='disabled')
    
    def Player2(l):
        
        enemy = random.randint(0,50)
        game1[enemy]='X'
        buttons[enemy].config(text='X',state='disabled')
        
        game1[l]='X'
        game3[shipsenemy]=' '
        game2[shipsenemy2]= '  '
        game5[nothing2]= '    '
        game4[nothing]= '   '
        
        if  game1[l] != game2[shipsenemy2]:
            buttonsl[l].config(text='X',state= 'disabled')
            nazv3['text'] = 'Вы попали!'
        if  game1[l] != game5[nothing2]:
            buttonsl[l].config(text='O',state='disabled')
            nazv3['text']= 'Вы промазали'
        
        if  game1[l] != game3[shipsenemy]:
            buttonsl[l].config(text='X',state= 'disabled')
            nazv3['text'] = 'Вы попали!'
        if  game1[l] != game4[nothing]:
            buttonsl[l].config(text='O',state='disabled')
            nazv3['text']= 'Вы промазали'
        
        
        #time.sleep(0.5)


    
nazv1 = Label(windows,text='Игра морской бой',font=('Times New Roman',30))
nazv1.place(relx = 0.4,rely=0.4)
buttonsw = Button(windows,text='Начать игру',width=20,height=5,command=GAME)
buttonsw.place(relx=0.4,rely=0.6)




windows.mainloop()
#nazv1['text'] = 'Вы проиграли((('
#nazv1['text'] = 'Вы победили!'