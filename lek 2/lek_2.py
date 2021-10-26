from tkinter import *
import random

listbutton=[]

def hello(event,b1): #обработчик кнопок мы играем 0, компьютер 1
    b1['text']='0'
    bt=listbutton[random.randint(0, 100)]
    while bt['text'] == '' or bt['text'] == '0':
        bt=listbutton[random.randint(0, 100)]
    bt['text']=1

def CreatButton():  #создаём 100 кнопок
    i=0
    while i<10:
        j=0
        while j<10:
           b1 = Button(w1, text=' ', width=2)
           b1.bind("<Button-1>", lambda event, b1=b1: hello(event, b1))
           b1.place(x=70 + j*20, y=100 + i*25)
           listbutton.append(b1)
           j +=1
        i += 1

w1 = Tk()
w1.geometry('500x500')
w1.title('windows')
CreatButton()
w1.mainloop()