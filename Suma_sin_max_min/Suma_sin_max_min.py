def suma_sin_eso_facil():
    lista = [8, 2, 14, 9, 1, 0, 40, 200]
    lista.sort()
    lista.pop(0)
    lista.pop(-1)
    res = sum(lista)
    print(res)

def suma_sin_eso_medio():
    lista = [8, 2, 14, 9, 1, 0, 40, 200]
    mayor = lista[0]
    menor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    lista.remove(mayor)
    for num in lista:
        if num < menor:
            menor = num
    lista.remove(menor)
    print(sum(lista))


suma_sin_eso_facil()
suma_sin_eso_medio()