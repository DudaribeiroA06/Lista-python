lista1 = [1,2,3,4,5]
lista2 = [5,2,3,8,6]
lista3 = []
for x in lista1:
    for y in lista2:
        if y ==x:
            lista3.append(y)
            print(lista3)