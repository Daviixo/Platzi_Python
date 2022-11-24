import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':

    tamano_de_lista = int(input('De que tamano sera la lista?\n'))
    objetivo = int(input('Que numero quieres encontrar?\n'))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    lista_ordenada = sorted(lista)

    print(f'Lista original: {lista}\n')
    print(f'Lista ordenada: {lista_ordenada}\n')

    print(f'El numero {objetivo} {"esta" if encontrado else "no esta"} en la lista')