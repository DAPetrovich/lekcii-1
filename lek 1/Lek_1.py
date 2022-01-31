graf=[(0, 2), (2, 5), (5, 2), (6, 6), (8, 3) ]
path =  [0,0,0,0,0]

def length_AtoB(x, y):
    return ((graf[y][0] - graf[x][0]) ** 2 + (graf[y][1] - graf[x][1]) ** 2)  ** 0.5

def vivod(path):
    string = str(graf[0])  
    i=1
    length = 0
    while i < 5:
        length += length_AtoB(path[i-1], path[i])
        string += ' -> ' + str(graf[path[i]]) + '[' +str(length) + ']'
        i += 1
    length += length_AtoB(path[i-1], path[0]) 
    string += ' ->' + str(graf[path[0]]) + '[' + str(length) + ']' + ' = ' + str(length)
    return string

def calculate():
    min_pyt = 1000 # начальный путь космический
    for i in range(5): # перебираем все возможные пути
        for j in range(5):
            for x in range(5):
                for y in range(5):
                    if (i != j) and (i != x) and (i !=y) and (j != x) and (j != y) and (x != y) and (i!=0)and (j!=0)and (x!=0)and (y!=0): # если не посещаем отну вершину дважды то считаем
                        min_pyt_temp = length_AtoB(0,i) + length_AtoB(i,j) + length_AtoB(j,x) + length_AtoB(x,y) + length_AtoB(y,0)
                        if min_pyt  > min_pyt_temp: # если новый путь короче старого то пересохраняемся
                            min_pyt = min_pyt_temp                
                            path[1], path[2], path[3], path[4] = i, j, x ,y
    return path

print(vivod(calculate()))