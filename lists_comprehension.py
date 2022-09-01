
def main():

    temp_list = []

    for i in range(1, 101):
        temp = i**2

        if temp % 3 != 0:
            temp_list.append(temp)

    square_list = [i**2 for i in range (1, 101) if i % 3 != 0]

    print('\n--Temp List--\n')
    print(temp_list)

    print('\n--Square List--\n')
    for i in square_list:
        print(i)

    # Challenge

    print('\n--Challenge List--\n')

    challenge_squares = [i**2 for i in range (1, 10000) if i % 36 == 0]

    for i in challenge_squares:
        print(i)

if __name__ == '__main__':
    main()