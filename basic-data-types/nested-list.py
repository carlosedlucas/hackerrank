
lista = [[37.21, 'Harry'], [37.21, 'Berry'], [37.21, 'Tina'], [41.0, 'Akriti'], [39.0, 'Harsh'], [39.0, 'Harsh2'], [39.0, 'Harsh3'] ]

lista_sorted = sorted(lista)
minimo = min(lista_sorted)

nova_lista = []
for x, y in lista_sorted:
    if x != minimo[0]:
        nova_lista.append([x, y])

minimo2 = min(nova_lista)
for x, y in nova_lista:
    if x == minimo2[0]:
        print(y)
