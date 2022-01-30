from tkinter import *
from tkinter import messagebox


ListDinamicObject = []
Vibor = '1234'

def hidenObject():
    label1.place_forget()
    label2.place_forget()
    label3.place_forget()
    InputPole1.place_forget()
    InputPole2.place_forget()
    InputPole3.place_forget()

def MainWindows():
    w1 = Tk()
    w1.geometry('1000x500')
    w1.title('Задание №3 - Калькулятор')
    w1.resizable(False, False)
    return w1

def CircleView():  # круг 
    global Vibor 
    Vibor = 'Circle'
    hidenObject()
    label1.place(x=450, y=50)
    label1['text']='Введите радиус = '
    InputPole1.place(x=650, y=50)
def SquareView():  # квадрат 
    global Vibor 
    Vibor = 'Square'
    hidenObject()
    label1.place(x=450, y=50)
    label1['text']='Введите сторону А = '
    InputPole1.place(x=650, y=50)
def rectangleView(): # Прямоугольник
    global Vibor
    Vibor = 'rectangle'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label1['text']='Введите сторону А = '
    label2['text']='Введите сторону B = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)
def TriangleView(): # Треугольник  S=1/2Bh
    global Vibor
    Vibor = 'Triangle'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label1['text']='Введите основание треугольника = '
    label2['text']='Введите высоту h = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)
def TrapezoidView(): # Трапеция
    global Vibor
    Vibor = 'Trapezoid'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label3.place(x=450, y=250)
    label1['text']='Введите основание a = '
    label2['text']='Введите основание b = '
    label3['text']='Введите высоту h = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)
    InputPole3.place(x=650, y=250)
def RhombView(): # Ромб
    global Vibor
    Vibor = 'Rhomb'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label1['text']='Введите основание a = '
    label2['text']='Введите высоту h  = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)
def SphereView(): # сфера
    global Vibor
    Vibor = 'Sphere'
    hidenObject()
    label1.place(x=450, y=50)
    label1['text']='Введите радиус = '
    InputPole1.place(x=650, y=50)
def cubeView(): # куб
    global Vibor
    Vibor = 'cube'
    hidenObject()
    label1.place(x=450, y=50)
    label1['text']='Введите сторону a = '
    InputPole1.place(x=650, y=50)
def parallelepipedView(): # параллелепипед
    global Vibor
    Vibor = 'parallelepiped'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label3.place(x=450, y=250)
    label1['text']='Введите сторону a = '
    label2['text']='Введите сторону b = '
    label3['text']='Введите сторону с = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)
    InputPole3.place(x=650, y=250)
def pyramidView(): #пирамида
    global Vibor
    Vibor = 'pyramid'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label1['text']='Введите длину основания a = '
    label2['text']='Введите апофему L = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)
def cylinderView(): # цилиндр
    global Vibor
    Vibor = 'cylinder'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label1['text']='Введите радиус r = '
    label2['text']='Введите высоту h = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)
def coneView(): #конус
    global Vibor
    Vibor = 'cone'
    hidenObject()
    label1.place(x=450, y=50)
    label2.place(x=450, y=150)
    label1['text']='Введите образующую l = '
    label2['text']='Введите радиус r = '
    InputPole1.place(x=650, y=50)
    InputPole2.place(x=650, y=150)

def CreateButton(): # тут потом засунем в цикл
    ListNameButton =['Круг','Квадрат','Прямоугольник','Треугольник','Трапеция','Ромб','сфера','куб','параллелепипед','пирамида','цилиндр','конус'] # :list[str]
    ListButton = []

    bt=Button(mw, text=ListNameButton[0], width=15, height=5, command=lambda x=mw: CircleView())
    bt.place(x=50, y=50)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[1], width=15, height=5, command=lambda x=mw: SquareView())
    bt.place(x=170, y=50)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[2], width=15, height=5, command=lambda x=mw: rectangleView())
    bt.place(x=290, y=50)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[3], width=15, height=5, command=lambda x=mw: TriangleView())
    bt.place(x=50, y=150)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[4], width=15, height=5, command=lambda x=mw: TrapezoidView())
    bt.place(x=170, y=150)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[5], width=15, height=5, command=lambda x=mw: RhombView())
    bt.place(x=290, y=150)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[6], width=15, height=5, command=lambda x=mw: SphereView())
    bt.place(x=50, y=270)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[7], width=15, height=5, command=lambda x=mw: cubeView())
    bt.place(x=170, y=270)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[8], width=15, height=5, command=lambda x=mw: parallelepipedView())
    bt.place(x=290, y=270)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[9], width=15, height=5, command=lambda x=mw: pyramidView())
    bt.place(x=50, y=370)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[10], width=15, height=5, command=lambda x=mw: cylinderView())
    bt.place(x=170, y=370)
    ListButton.append(bt)
    bt=Button(mw, text=ListNameButton[11], width=15, height=5, command=lambda x=mw: coneView())
    bt.place(x=290, y=370)
    ListButton.append(bt)

    canvas = Canvas(width=355, height=5,)
    canvas.create_line(0, 2, 355, 2)
    canvas.place(x=50, y=250)
  
    return ListButton

def Rewenie(Vibor):
    try: 
        if Vibor == 'Circle':
            S= 3.14 * float(InputPole1.get()) ** 2
            messagebox.showinfo('Результат', 'Площадь круга = '+ str(S))
        elif Vibor == 'Square':
            S= float(InputPole1.get()) ** 2
            messagebox.showinfo('Результат', 'Площадь квадрата = '+ str(S))
        elif Vibor == 'rectangle':
            S= float(InputPole1.get()) * float(InputPole2.get())
            messagebox.showinfo('Результат', 'Площадь прямоугольника = '+ str(S))
        elif Vibor == 'Triangle':
            S= 0.5 * float(InputPole1.get()) * float(InputPole2.get())
            messagebox.showinfo('Результат', 'Площадь треугольник = '+ str(S))
        elif Vibor == 'Trapezoid':
            S= 0.5 * float(InputPole3.get()) * (float(InputPole1.get()) + float(InputPole2.get()))
            messagebox.showinfo('Результат', 'Площадь трапеции = '+ str(S))
        elif Vibor == 'Rhomb':
            S= float(InputPole1.get()) * float(InputPole2.get())
            messagebox.showinfo('Результат', 'Площадь ромба = '+ str(S))
        elif Vibor == 'Sphere':
            S= 4 * 3.14 * (float(InputPole1.get()) ** 2)
            messagebox.showinfo('Результат', 'Площадь сферы = '+ str(S))
        elif Vibor == 'cube':
            S= 6 * (float(InputPole1.get()) ** 2)
            messagebox.showinfo('Результат', 'Площадь куба = '+ str(S))
        elif Vibor == 'parallelepiped':
            S= 2 * (float(InputPole1.get()) * float(InputPole2.get()) + 
                    float(InputPole2.get()) * float(InputPole3.get()) + 
                    float(InputPole2.get()) * float(InputPole3.get()))  
            messagebox.showinfo('Результат', 'Площадь параллелепипеда = '+ str(S))
        elif Vibor == 'pyramid':
            S= 0.5 * 4 * float(InputPole1.get()) * float(InputPole2.get()) + float(InputPole1.get()) * float(InputPole1.get())
            messagebox.showinfo('Результат', 'Площадь пирамиды = '+ str(S))
        elif Vibor == 'cylinder':
            S= (2 * 3.14 * float(InputPole1.get()) ** 2) + (2 * 3.14 * float(InputPole1.get()) * float(InputPole2.get()))
            messagebox.showinfo('Результат', 'Площадь цилиндра = '+ str(S))
        elif Vibor == 'cone':
            S= (3.14 * float(InputPole1.get()) * float(InputPole2.get())) + (3.14 * float(InputPole2.get()) ** 2)
            messagebox.showinfo('Результат', 'Площадь конуса = '+ str(S))
    except:
        messagebox.showinfo('Ошибка ввода', 'Введите численное значение')


mw = MainWindows()
lb = CreateButton()

label1 = Label(mw,text="  ", justify=LEFT)
label1.place(x=450, y=50)
InputPole1 = Entry(textvariable=StringVar(), width=30)
InputPole1.place(x=650, y=50)

label2 = Label(mw,text="  ", justify=LEFT)
label2.place(x=450, y=150)
InputPole2 = Entry(textvariable=StringVar(), width=30)
InputPole2.place(x=650, y=150)

label3 = Label(mw,text="  ", justify=LEFT)
label3.place(x=450, y=250)
InputPole3 = Entry(textvariable=StringVar(), width=30, name="bbb")
InputPole3.place(x=650, y=250)

mw.children['bbb'].place(x=150, y=150)
#for _ in mw.children.items():
#    print(_[1])
#    _[1].place(x=650, y=150)

# w1.children['bbb'].place(x=150, y=150)
        #for _ in mw.children.items():
        #    print(_[1])
        #    _[1].place(x=650, y=150)

bt=Button(mw, text='Вычислить', width=73, height=2, command=lambda x=mw: Rewenie(Vibor))
bt.place(x=440, y=415)

mw.mainloop()