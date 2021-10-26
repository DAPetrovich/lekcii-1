from tkinter import *
import random
from tkinter import messagebox
import numpy as np

listbutton=[] #type: list

def CheckWinLine(LB): # Проверка горизонтальных и вертикальных прямых  
    i=0
    while i < 10: # цикл по столбцам кнопок
        j=0
        CounterLineUser=0   #счётчик пользователя по строкам
        CounterLinePC=0     #счётчик ПК по строкам
        CounterColumnUser=0 #счётчик пользователя по столбцам
        CounterColumnPC=0   #счётчик ПК по столбцам
        while j < 10:       # цикл по строке кнопок
            if str(LB[i][j]['text']) == '0': CounterLineUser +=1 
            else: CounterLineUser = 0
            if str(LB[i][j]['text']) == 'X': CounterLinePC +=1
            else: CounterLinePC = 0 
            if str(LB[j][i]['text']) == '0': CounterColumnUser +=1 
            else: CounterColumnUser = 0
            if str(LB[j][i]['text']) == 'X': CounterColumnPC +=1
            else: CounterColumnPC = 0
            if CounterLineUser==5 or CounterColumnUser==5: 
                messagebox.showinfo(' ', 'Win PC')
                exit()
            if CounterLinePC==5 or CounterColumnPC==5: 
                messagebox.showinfo(' ', 'You Win')
                exit()
            j +=1
        i +=1

def CheckWindiagonal(LB): # Проверка диагоналей
    CounterDiagRUser=0   #счётчик пользователя по строкам
    CounterDiagRPC=0     #счётчик ПК по строкам
    CounterDiagLUser=0   #счётчик пользователя по столбцам
    CounterDiagLPC=0     #счётчик ПК по столбцам
    ListButtonL = np.fliplr(LB) # создаём перевернутую копию массива
    offset = -5          # от -5 до 5 достаточно так как остальные диагонали короче 
    while offset <= 5:   
        ar = np.diagonal(LB, offset, axis1=0, axis2=1)  # Возвращаем главную диагональ 
        al = np.diagonal(ListButtonL, offset, axis1=0, axis2=1) # Возвращаем побочную диагональ
        i=0
        while i < len(ar):
            if ar[i]['text'] == '0': CounterDiagRUser += 1
            else: CounterDiagRUser = 0
            if ar[i]['text'] == 'X': CounterDiagRPC += 1
            else: CounterDiagRPC = 0
            if al[i]['text'] == '0': CounterDiagLUser += 1
            else: CounterDiagLUser = 0
            if al[i]['text'] == 'X': CounterDiagLPC += 1
            else: CounterDiagLPC = 0
            if CounterDiagRUser==5 or CounterDiagLUser==5: 
                messagebox.showinfo(' ', 'Win PC')
                exit()
            if CounterDiagLPC==5 or CounterDiagRPC==5: 
                messagebox.showinfo(' ', 'You Win')
                exit()
            i +=1
        offset += 1


def handlerButton(event,b1): #обработчик кнопок мы играем 0, компьютер X, ПК проверяет чтобы кнопка не была нажата до того как
    b1['text']='0'
    CheckWinLine(listbutton)
    CheckWindiagonal(listbutton)
    while True:
        i=random.randint(0, 9)
        j=random.randint(0, 9)
        bt=listbutton[i][j]
        if bt['text'] == ' ': 
            print(bt['text'])
            break
    bt=listbutton[i][j]
    bt['text']='X'
    CheckWinLine(listbutton)
    CheckWindiagonal(listbutton)

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
w1.title('Крестики нолики')
CreatButton()
w1.mainloop()