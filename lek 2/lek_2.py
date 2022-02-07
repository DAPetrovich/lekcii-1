from tkinter import *
import random
from tkinter import messagebox
import numpy as np

game_array = []  # type: list


def check_win_line(
    playing_field, display
):  # Проверка горизонтальных и вертикальных прямых  вернёт True если кто то выиграл
    i = 0
    while i < 10:  # цикл по столбцам кнопок
        j = 0
        counter_line_user = 0  # счётчик пользователя по  строкам
        counter_line_pc = 0  # счётчик ПК по строкам
        counter_column_user = 0  # счётчик пользователя по столбцам
        counter_column_pc = 0  # счётчик ПК по столбцам
        while j < 10:  # цикл по строке кнопок
            if str(playing_field[i][j]["text"]) == "0":
                counter_line_user += 1
            else:
                counter_line_user = 0
            if str(playing_field[i][j]["text"]) == "X":
                counter_line_pc += 1
            else:
                counter_line_pc = 0
            if str(playing_field[j][i]["text"]) == "0":
                counter_column_user += 1
            else:
                counter_column_user = 0
            if str(playing_field[j][i]["text"]) == "X":
                counter_column_pc += 1
            else:
                counter_column_pc = 0
            if counter_line_user == 5 or counter_column_user == 5:
                if display:
                    messagebox.showinfo(" ", "Вы проиграли")
                return True
            if counter_line_pc == 5 or counter_column_pc == 5:
                if display:
                    messagebox.showinfo(" ", "Вы выиграли!")
                return True
            j += 1
        i += 1
    return False


def check_win_diagonal(
    playing_field, display
):  # Проверка диагоналей вернёт True если кто то выиграл
    copy_playing_field = np.fliplr(playing_field)  # создаём перевернутую копию массива
    offset = -10
    while offset <= 10:
        main_diagonal = np.diagonal(
            playing_field, offset, axis1=0, axis2=1
        )  # Возвращаем главную диагональ
        side_diagonal = np.diagonal(
            copy_playing_field, offset, axis1=0, axis2=1
        )  # Возвращаем побочную диагональ
        i = 0
        counter_diag_right_user = 0  # счётчик пользователя по строкам
        counter_diag_right_pc = 0  # счётчик ПК по строкам
        counter_diag_left_user = 0  # счётчик пользователя по столбцам
        counter_diag_left_pc = 0  # счётчик ПК по столбцам
        while i < len(main_diagonal):
            if main_diagonal[i]["text"] == "0":
                counter_diag_right_user += 1
            else:
                counter_diag_right_user = 0
            if main_diagonal[i]["text"] == "X":
                counter_diag_right_pc += 1
            else:
                counter_diag_right_pc = 0
            if side_diagonal[i]["text"] == "0":
                counter_diag_left_user += 1
            else:
                counter_diag_left_user = 0
            if side_diagonal[i]["text"] == "X":
                counter_diag_left_pc += 1
            else:
                counter_diag_left_pc = 0
            if counter_diag_right_user == 5 or counter_diag_left_user == 5:
                if display:
                    messagebox.showinfo(" ", "Вы проиграли")
                return True
            if counter_diag_left_pc == 5 or counter_diag_right_pc == 5:
                if display:
                    messagebox.showinfo(" ", "Вы выиграли!")
                return True
            i += 1
        offset += 1
    return False


def computer_move_line():  # Шаг компьютера проверкой подряд когда рандом не может попасть в клетку
    i = 0
    j = 0
    while i <= 9:
        j = 0
        while j <= 9:
            bt = game_array[i][j]
            if bt["text"] == "":
                bt["text"] = "X"
                if (check_win_line(game_array, 0)) or (
                    check_win_diagonal(game_array, 0)
                ):
                    bt["text"] = ""
                else:
                    i = 20
                    j = 20
            j += 1
        i += 1
    if (i == 10) and (j == 10):
        messagebox.showinfo(" ", "У меня ходов не осталось... Вы выиграли ")
        exit()


def computer_move_random():  # Шаг компьютера случайным образом
    bool = True
    complexity = 0
    while bool and (complexity < 10000):
        i = random.randint(0, 9)
        j = random.randint(0, 9)
        bt = game_array[i][j]
        if bt["text"] == "":
            bt["text"] = "X"
            if (check_win_line(game_array, 0)) or (check_win_diagonal(game_array, 0)):
                bool = True
                bt["text"] = ""
            else:
                bool = False
        complexity += 1
    if complexity == 10000:
        return True
    else:
        return False


def handlerbutton(
    event, b1
):  # обработчик кнопок мы играем 0, компьютер X, ПК проверяет чтобы кнопка не была нажата до того как

    if (b1["text"] != "0") and (b1["text"] != "X"):
        b1["text"] = "0"
        if check_win_line(game_array, 1) or check_win_diagonal(game_array, 1):
            exit()
        if computer_move_random():  # поиск хода случайным образом.
            computer_move_line()  # если не нашли ход рандомом то ищем по подряд
        if check_win_line(game_array, 1) or check_win_diagonal(game_array, 1):
            exit()


def creat_button():  # создаём 100 кнопок
    i = 0
    while i < 10:
        j = 0
        listbuttontemp = []
        while j < 10:
            b1 = Button(MainWindow, text="", width=2)
            b1.bind("<Button-1>", lambda event, b1=b1: handlerbutton(event, b1))
            b1.place(x=10 + j * 20, y=10 + i * 25)
            listbuttontemp.append(b1)
            j += 1
        game_array.append(listbuttontemp)
        i += 1


MainWindow = Tk()
MainWindow.geometry("225x270")
MainWindow.title("Крестики нолики")
creat_button()
MainWindow.mainloop()
