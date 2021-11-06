graf = ((0,2),(2,5),(5,2),(6,6),(8,3))
graf_len = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

def length_AtoB(x, y):
    km = ((graf[y][0] - graf[x][0]) ** 2 + (graf[y][1] - graf[x][1]) ** 2)  ** 0.5
    return(km)

for x in range(5):
    for y in range(5) :
        graf_len[x][y] = length_AtoB(x, y)

otvet = str(graf[0])
length = 0
stroka = 0
for i in range(4):
    my_min=10000
    for j in range(5):
        if (graf_len[stroka][j] < my_min) and (stroka != j):
            my_min = graf_len[stroka][j] # сохраняем длину минимального пути
            ii=stroka # сохраняем индексы
            jj=j      # сохраняем индексы
    length = length + my_min
    otvet = otvet + ' -> ' + str(graf[jj]) + '[' + str(length) + ']'
    for z in range(5): graf_len[z][stroka] = 10000 # помечаем вершину чтобы не зайти в неё второй раз
    stroka = jj # переходим на соседнюю вершину с минималным расстоянием

length = length + length_AtoB(jj,0) 
otvet = otvet + '-> ' + str(graf[0]) + '[' + str(length) + ']'
print(otvet + ' = ' + str(length))