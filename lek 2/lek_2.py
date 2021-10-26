from tkinter import *
import random
from tkinter import messagebox

listbutton=[]

def CheckWin(): # пока проверка только по горизонтали. Очень криво) 
    i=0
    while i < 10:
        j=0
        k1=0
        k2=0
        while j<10:
            bt=listbutton[i][j]
            print(bt['text'])
            if str(bt['text']) == '0':
                k1 +=1
            if str(bt['text']) != '0':
                k1 = 0

            if str(bt['text']) == '1':
                k2 +=1
            if str(bt['text']) != '1':
                k2 = 0
            
            if k1==5: 
                messagebox.showinfo(' ', 'Win PC')
                break
            if k2==5: 
                messagebox.showinfo(' ', 'You Win')
                break
            j +=1
        i +=1
        print('-------------------------')
    print(k1, k2)

def handlerButton(event,b1): #обработчик кнопок мы играем 0, компьютер 1, ПК проверяет чтобы кнопка не была нажата до того как
    b1['text']='0'
    CheckWin()   
    while True:
        i=random.randint(0, 9)
        j=random.randint(0, 9)
        bt=listbutton[i][j]
        if bt['text'] == ' ': 
            print(bt['text'])
            break
    bt=listbutton[i][j]
    bt['text']=1
    CheckWin()

def CreatButton():  #создаём 100 кнопок
    i=0
    while i<10:
        j=0
        listbuttontemp=[]
        while j<10:
           b1 = Button(w1, text=' ', width=2)
           b1.bind("<Button-1>", lambda event, b1=b1: handlerButton(event, b1))
           b1.place(x=70 + j*20, y=100 + i*25)
           listbuttontemp.append(b1)
           j +=1
        listbutton.append(listbuttontemp)
        i += 1

w1 = Tk()
w1.geometry('350x400')
w1.title('windows')
CreatButton()
w1.mainloop()