from tkinter import *
import random
from tkinter import messagebox

listbutton=[]

def CheckWinLine(): # пока проверка только по горизонтали. Очень криво) 
    i=0
    while i < 10: # цикл по столбцам кнопок
        j=0
        CounterLineUser=0   #счётчик пользователя по строкам
        CounterLinePC=0     #счётчик ПК по строкам
        CounterColumnUser=0 #счётчик пользователя по столбцам
        CounterColumnPC=0   #счётчик ПК по столбцам
        while j < 10:       # цикл по строке кнопок
            btline = listbutton[i][j]
            btcolumn = listbutton[j][i]
            if str(btline['text']) == '0': CounterLineUser +=1 #
            else: CounterLineUser = 0
            if str(btline['text']) == 'X': CounterLinePC +=1
            else: CounterLinePC = 0 
            if str(btcolumn['text']) == '0': CounterColumnUser +=1 #
            else: CounterColumnUser = 0
            if str(btcolumn['text']) == 'X': CounterColumnPC +=1
            else: CounterColumnPC = 0
            if CounterLineUser==5 or CounterColumnUser==5: 
                messagebox.showinfo(' ', 'Win PC')
                exit()
            if CounterLinePC==5 or CounterColumnPC==5: 
                messagebox.showinfo(' ', 'You Win')
                exit()
            j +=1
        i +=1

 
def handlerButton(event,b1): #обработчик кнопок мы играем 0, компьютер X, ПК проверяет чтобы кнопка не была нажата до того как
    b1['text']='0'
    CheckWinLine()
    while True:
        i=random.randint(0, 9)
        j=random.randint(0, 9)
        bt=listbutton[i][j]
        if bt['text'] == ' ': 
            print(bt['text'])
            break
    bt=listbutton[i][j]
    bt['text']='X'
    CheckWinLine()

def CreatButton():  #создаём 100 кнопок
    i=0
    while i < 10:
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