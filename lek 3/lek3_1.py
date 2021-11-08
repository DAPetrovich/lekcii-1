from tkinter import *
from tkinter import messagebox


class Primitiv:
    name = ''

    def square(self):
        return 0
    
    def squareStr(self):
        return 'Площадь {0} = {1}'.format(self.name, self.square())
    
    def volumeStr(self):
        return 'Объём {0} = {1}'.format(self.name, self.volume())


class Circle(Primitiv):
    name = 'Круг'
    def __init__(self, radius):
        super(Primitiv, self).__init__()
        self.radius = radius

    def square(self):
        return 3.14 * float(self.radius) ** 2


class Box(Primitiv):
    name = 'Квадрат'
    def __init__(self, width):
        super(Primitiv, self).__init__()
        self.width = width

    def square(self):
        return self.width ** 2


class Rectangle(Primitiv):
    name = 'Прямоугольника'
    def __init__(self, a,b):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b


class Triangle(Primitiv):
    name = 'треугольника'
    def __init__(self, a,b):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b
    
    def square(self):
        return 0.5 * self.a * self.b


class Trapezoid(Primitiv):
    name = 'трапеции'
    def __init__(self, a,b,z):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b
        self.z = z
    
    def square(self):
        return 0.5 * self.a * self.b + self.z


class Rhomb(Primitiv):
    name = 'ромба'
    def __init__(self, a,b):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b
    
    def square(self):
        return self.a * self.b
        

class Sphere(Primitiv):
    name = 'сферы'
    def __init__(self, a):
        super(Primitiv, self).__init__()
        self.a = a
    
    def square(self):
        return 4 * 3.14 * self.a ** 2 


class cube(Primitiv):
    name = 'куба'
    def __init__(self, a):
        super(Primitiv, self).__init__()
        self.a = a
    
    def square(self):
        return 6 * self.a ** 2 
    
    def volume(self):
        return self.a * self.a * self.a


class parallelepiped(Primitiv):
    name = 'параллелепипеда'
    def __init__(self, a,b,c):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b
        self.c = c
    
    def square(self):
        return 2 * ((self.a * self.b) + (self.a * self.c) + (self.b * self.c))


class pyramid(Primitiv):
    name = 'пирамиды'
    def __init__(self, a,b):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b
    
    def square(self):
        return 0.5 * 4 * self.a * self.b + self.a * self.a


class cylinder(Primitiv):
    name = 'цилиндра'
    def __init__(self, a,b):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b
    
    def square(self):
        return (2 * 3.14 * self.a ** 2) + (2 * 3.14 * self.a * self.b)


class cone(Primitiv):
    name = 'конуса'
    def __init__(self, a,b):
        super(Primitiv, self).__init__()
        self.a = a
        self.b = b
    
    def square(self):
        return (3.14 * self.a * self.b) + (3.14 * self.b ** 2)


def unitTest():
    box = Box(5)
    if box.square() != 25:
        raise Exception('ne pravilno dla box')
    print('unit test passed!')

unitTest()

class Calc(Frame):    # Класс для создания окна
    def __init__(self, root):
        super(Calc, self).__init__(root)
        self.Vibor = ''  
        ListNameButton =['Круг','Квадрат','Прямоугольник','Треугольник',
                         'Трапеция','Ромб','сфера','куб','параллелепипед',
                         'пирамида','цилиндр','конус'] # :list[str]
        x = 50
        y = 50
        func=0
        for eltext in ListNameButton:
            bt=Button(w1, text=eltext, width=15, height=5, command=lambda x=eltext: self.calcview(x))
            bt.place(x=x, y=y)
            x += 120
            func += 1
            if x > 400: 
                y += 100
                x = 50
        self.label0 = Label(w1,text="", justify=LEFT)
        self.label0.place(x=450, y=30)
        self.label1 = Label(w1,text="", justify=LEFT)
        self.InputPole1 = Entry(textvariable=StringVar(), width=30, name="input1")
        self.label2 = Label(w1,text="", justify=LEFT)      
        self.InputPole2 = Entry(textvariable=StringVar(), width=30, name="input2")      
        self.label3 = Label(w1,text="", justify=LEFT)  
        self.InputPole3 = Entry(textvariable=StringVar(), width=30, name="input3")     
        bt=Button(w1, text='Вычислить', width=73, height=2, command=lambda x='Button_result': self.Rewenie())
        bt.place(x=440, y=415)
        
    def hidenObject(self):
        self.label1.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()
        self.InputPole1.place_forget()
        self.InputPole2.place_forget()
        self.InputPole3.place_forget()

    def calcview(self,func):
        self.label0['text'] = 'S '+ str(func) 
        if func == 'Круг':
            self.Vibor ='Circle'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label1['text']='Введите радиус = '
            self.InputPole1.place(x=650, y=50)
        elif func == 'Квадрат':
            self.Vibor ='Square'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label1['text']='Введите сторону А = '
            self.InputPole1.place(x=650, y=50)
        elif func == 'Прямоугольник':
            self.Vibor ='rectangle'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label1['text']='Введите сторону А = '
            self.label2['text']='Введите сторону B = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150)
        elif func == 'Треугольник':
            self.Vibor ='Triangle'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label1['text']='Введите основание треугольника = '
            self.label2['text']='Введите высоту h = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150)
        elif func == 'Трапеция':
            self.Vibor ='Trapezoid'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label3.place(x=450, y=250)
            self.label1['text']='Введите основание a = '
            self.label2['text']='Введите основание b = '
            self.label3['text']='Введите высоту h = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150)
            self.InputPole3.place(x=650, y=250)
        elif func == 'Ромб':
            self.Vibor ='Rhomb'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label1['text']='Введите основание a = '
            self.label2['text']='Введите высоту h  = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150)
        elif func == 'сфера':
            self.Vibor ='Sphere'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label1['text']='Введите радиус = '
            self.InputPole1.place(x=650, y=50)
        elif func == 'куб':
            self.Vibor = 'cube'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label1['text']='Введите сторону a = '
            self.InputPole1.place(x=650, y=50)
        elif func == 'параллелепипед':
            self.Vibor ='parallelepiped'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label3.place(x=450, y=250)
            self.label1['text']='Введите сторону a = '
            self.label2['text']='Введите сторону b = '
            self.label3['text']='Введите сторону с = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150)
            self.InputPole3.place(x=650, y=250)
        elif func == 'пирамида':
            self.Vibor ='pyramid'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label1['text']='Введите длину основания a = '
            self.label2['text']='Введите апофему L = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150)
        elif func == 'цилиндр':
            self.Vibor ='cylinder'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label1['text']='Введите радиус r = '
            self.label2['text']='Введите высоту h = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150) 
        elif func == 'конус':
            self.Vibor ='cone'
            self.hidenObject()
            self.label1.place(x=450, y=50)
            self.label2.place(x=450, y=150)
            self.label1['text']='Введите образующую l = '
            self.label2['text']='Введите радиус r = '
            self.InputPole1.place(x=650, y=50)
            self.InputPole2.place(x=650, y=150)

    def Rewenie(self):
        try:
            obj = None
            if self.Vibor == 'Circle':
                obj = Circle(float(self.InputPole1.get()))                
            elif self.Vibor == 'Square':
                obj = Box(float(self.InputPole1.get()))
            elif self.Vibor == 'rectangle':
                obj = Rectangle(float(self.InputPole1.get()), float(self.InputPole2.get()))
            elif self.Vibor == 'Triangle':
                obj = Triangle(float(self.InputPole1.get()), float(self.InputPole2.get()))
            elif self.Vibor == 'Trapezoid':
                obj = Trapezoid(float(self.InputPole3.get()), float(self.InputPole1.get()), float(self.InputPole2.get()))
            elif self.Vibor == 'Rhomb':
                obj = Rhomb(float(self.InputPole1.get()), float(self.InputPole2.get()))
            elif self.Vibor == 'Sphere':
                obj = Sphere(float(self.InputPole1.get()))
            elif self.Vibor == 'cube':
                obj = cube(float(self.InputPole1.get()))
                messagebox.showinfo('Результат', obj.volumeStr())
            elif self.Vibor == 'parallelepiped':
                obj = parallelepiped(float(self.InputPole1.get()), float(self.InputPole2.get()), float(self.InputPole3.get()))
            elif self.Vibor == 'pyramid':
                obj = pyramid(float(self.InputPole1.get()), float(self.InputPole2.get()))
            elif self.Vibor == 'cylinder':
                obj = cylinder(float(self.InputPole1.get()), float(self.InputPole2.get()))
            elif self.Vibor == 'cone':
                obj = cone(float(self.InputPole1.get()), float(self.InputPole2.get()))

            messagebox.showinfo('Результат', obj.squareStr())
        except:
            messagebox.showinfo('Ошибка ввода', 'Введите численное значение')

w1 = Tk()
w1.geometry('1000x500')
w1.title('Задание №3 - Калькулятор')
w1.resizable(False, False)

x = Calc(w1)
x.mainloop()
