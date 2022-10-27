if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([score, name])

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