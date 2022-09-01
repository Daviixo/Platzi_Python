def main():
    
    my_dict = {}

    for i in range (1, 101):
        if i % 3 != 0:
            my_dict[i] = i**3

    print('\n--Print normal dict--')
    print(my_dict)

    challenge_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print('\n--Print as Dict. Comprehension--')
    print(challenge_dict)

    print('\n--Print as Dict. Comprehension with Key, Value--')

    for key, value in challenge_dict:
        print(f'{key} - {value}')

if __name__ == '__main__':
    main()