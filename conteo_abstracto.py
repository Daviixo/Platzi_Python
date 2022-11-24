def f(x):

    respuesta = 0

    for i in range(x + 6):
        print(f'i => {i}')
        respuesta += 1

    print('\n-- XXXX --\n')

    for i in range(x + 1):
        print(f'i => {i}')
        respuesta += x

    print('\n-- XXXX --\n')

    for i in range(x + 1):
        for j in range(x + 1):
            print(f'i => {i}')
            print(f'j => {j}')
            respuesta += 1
            respuesta += 1

    return respuesta

if __name__ == '__main__':
    f(10)