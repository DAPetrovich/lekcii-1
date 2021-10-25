from typing import Match

graf = ([0,2],[2,5],[5,2],[6,6],[8,3])
graf_len = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

x = 0
while x <= 4:
    y = 0
    while y <=4 :
        xx = (graf[y][0] - graf[x][0]) ** 2
        yy = (graf[y][1] - graf[x][1]) ** 2
        temp = ( xx + yy ) ** 0.5
        graf_len[x][y] = temp
        y = y + 1
    x = x + 1
#Вашу блин мать a=1200

otvet = '(0,2) '
length = 0
i=0
stroka = 0
while i <4:
    j=0 
    my_min=10000
    while j<=4:
        if graf_len[stroka][j] < my_min and stroka != j:
            my_min = graf_len[stroka][j] # сохраняем длину минимального пути
            ii=stroka # сохраняем индексы
            jj=j # сохраняем индексы
        j = j + 1
    length = length + my_min
    otvet = otvet + '-> ('+ str(graf[jj][0]) + ','+ str(graf[jj][1]) + ')' + '[' + str(length) + ']'
    graf_len[jj][ii] = 10000
    stroka = jj # переходим на соседнюю вершину с минималным расстоянием
    i = i + 1
print(otvet + ' = ' + str(length))