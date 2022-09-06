import numbers


def read():
    numbers = []

    with open('Files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)


def write():
    names = ['David', 'Katy', 'Lana']
    with open('Files/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

        print('Jobs done!')


def select_option():
    
    option = input('1. Read\n2. Write\n')

    if option == '1':
        read()
    elif option == '2':
        write()


def main():
    select_option()


if __name__ == '__main__':
    main()