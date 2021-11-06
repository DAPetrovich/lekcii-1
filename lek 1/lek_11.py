point_0=(0, 2) # отделение почты
point_1=(2, 5)
point_2=(5, 2)
point_3=(6, 6)
point_4=(8, 3)
graf=[]
graf.append(point_0)
graf.append(point_1)
graf.append(point_2)
graf.append(point_3)
graf.append(point_4)

# graf = ((0,2),(2,5),(5,2),(6,6),(8,3))
pyt =  [0,0,0,0,0]

def length_AtoB(x, y):
    km = ((graf[y][0] - graf[x][0]) ** 2 + (graf[y][1] - graf[x][1]) ** 2)  ** 0.5
    return(km)

def vivod(pyt):
    string = str(graf[0])  
    i=1
    length = 0
    while i < 5:
        length = length + length_AtoB(pyt[i-1], pyt[i])
        string = string + ' -> ' + str(graf[pyt[i]]) + '[' +str(length) + ']'
        i += 1
    length = length + length_AtoB(pyt[i-1], pyt[0]) 
    string = string + ' ->' + str(graf[pyt[0]]) + '[' + str(length) + ']'
    string = string + ' = ' + str(length)
    return string

min_pyt = 1000 # начальный путь космический
for i in range(5): # перебираем все возможные пути
    for j in range(5):
        for x in range(5):
            for y in range(5):
                if (i != j) and (i != x) and (i !=y) and (j != x) and (j != y) and (x != y) and (i!=0)and (j!=0)and (x!=0)and (y!=0): # если не посещаем отну вершину дважды то считаем
                    min_pyt_temp = length_AtoB(0,i) + length_AtoB(i,j) + length_AtoB(j,x) + length_AtoB(x,y) + length_AtoB(y,0)
                    if min_pyt  > min_pyt_temp: # если новый путь короче старого то пересохраняемся
                        min_pyt = min_pyt_temp                
                        pyt[1] = i
                        pyt[2] = j
                        pyt[3] = x
                        pyt[4] = y
print(vivod(pyt))