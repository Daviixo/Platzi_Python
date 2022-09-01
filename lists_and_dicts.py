def main():

    my_list = [1, 'Hello world', 5.6]
    my_dict = {'First Name': 'David', 'Last Name': 'Veras'}

    super_list = [
        {'First Name': 'David', 'Last Name': 'Veras'},
        {'First Name': 'Armando', 'Last Name': 'Santos'},
        {'First Name': 'Kevyn', 'Last Name': 'Tote'}
    ]

    super_dict = {
        'Natural Numbers' : [1, 2, 3],
        'Integer Numbers' : [-1, -2, -3],
        'Floating Numbers' : [1.2, 1.3, 2.5]
    }

    print('----- Printing SUPERs -----\n')

    for key, value in super_dict.items():
        print(key, '-', value)

    print('\n-----\n')

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

    print('\n-----\n')
    
    for i in super_list:
        print(i.items())

    print('\n----- Printing No-SUPERs -----\n')

    for i in my_dict:
        print(my_dict.keys())

    print('\n-----Using MAP-----\n')

    print('\n'.join(map(str, my_list)))

    print('\n-----Using FOR-----\n')

    for i in my_list:
        print(i)

if __name__ == '__main__':
    main()