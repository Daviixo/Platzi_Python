def main():

    rows = int(input('Enter ROWS:\n'))
    
    for i in range(1, rows + 1):
        for j in range(i, rows + 1):
            print(j, end = ' ')
        for k in range(1, i):
            print(k, end = ' ')
        print()


if __name__ == '__main__':
    main()