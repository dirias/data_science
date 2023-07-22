lista = []

for i in range(1, 9):
    lista.append([])
    for j in range(1, 10):
        lista[i - 1].append(j)
for element in lista:
    print(element)
