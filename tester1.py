from tkinter import *
import time
import random

windows = Tk()
windows.geometry('1980x1200')
windows.title('Морской бой')

#массивы
game1 =  list(range(10*10))
game2 =  [['' for i in range(10*10)]]
game3 =  [['' for i in range(10*10)]]


def GAME():
    nazv1.config(text= '                    ')
    buttonsw.config(text='Повтор')
   
    nazv3 = Label(windows,text='                          ')
    nazv3.grid(row=1,column=11)
    nazv2 = Label(windows,text=':ваш противник',font=('Times New Roman',18))
    nazv2.grid(row=5,column=60)
    buttonsw.place(relx = 0.8,rely = 0.6)
    
    
    buttons = [Button(windows,width=7,height=4,font=('Times New Roman',9, 'bold'),command= lambda  x = i:Player1(x))for i in range(10*10)]
    buttonsl = [[Button(windows,width=7,height=4,font=('Times New Roman',9, 'bold'),command = lambda x = i:Player2(x))for i in range(10*10)]]
    
    
    #моё поле
    row = 0
    col = 0
    for i in range(len(buttons)):
        buttons[i].grid(row=row,column=col)
        col += 1
        if col == 10:
            row +=1
            col=0
            
    pust = Label(windows,text='        ')
    pust.grid(row=1,column=11)
    
    #поле противника
    row = 0
    col = 12
    for i in range(len(buttonsl)):
        for j in range(len(buttonsl[i])):
            buttonsl[i][j].grid(row=row, column=col)
            col += 1
            if col == 22:
                row += 1
                col = 12
                
    
    #Список с длинами кораблей
    ship_lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for length in ship_lengths:
    # Генерация случайных координат для размещения корабля
        direction = random.choice(['horizontal', 'vertical'])
        while True:
            x = random.randint(
                0, 10*10) if direction == 'horizontal' else random.randint(0, 10*10 - length)
            y = random.randint(
                0, 10*10 - length) if direction == 'vertical' else random.randint(0, 10*10)
            break
        
        #Размещение корабля на поле
        for i in range(length):
            print(x,y,i)
            if direction == 'horizontal':
                buttonsl[y][x + i].config(text = 'X')
            else:
                buttonsl[y + i][x].config(text = 'x')
    
    def Player1(w):
        
        game1[w]= '■'
        buttons[w].config(text='■',state='disabled')
    
    def Player2(l):
        
        enemy = random.randint(0,10*10)
        game1[enemy]='X'
        for i in range(buttons):
            buttons[i][enemy].config(text='X',state='disabled')
        game2[l] = 'X'
    
        #game2[x] = 'X'
        #game3[y] = 'X'
        
        #if  game1[l] != game2[x]:
            #buttonsl[l].config(text='X',state= 'disabled')
            #nazv3['text'] = 'Вы попали!'
        #else:
            #buttonsl[l].config(text='O',state= 'disabled')
            #nazv3['text'] = 'Вы промазали!'
        #if  game1[l] != game3[y]:
            #buttonsl[l].config(text='X',state='disabled')
            #nazv3['text']= 'Вы попали!'
        #else:
            #buttonsl[l].config(text='O',state= 'disabled')
            #nazv3['text'] = 'Вы промазали!'
        
        #time.sleep(0.5)
    
nazv1 = Label(windows,text='Игра морской бой',font=('Times New Roman',30))
nazv1.place(relx = 0.4,rely=0.4)
buttonsw = Button(windows,text='Начать игру',width=20,height=5,command=GAME)
buttonsw.place(relx=0.4,rely=0.6)

windows.mainloop()
#nazv1['text'] = 'Вы проиграли((('
#nazv1['text'] = 'Вы победили!'

