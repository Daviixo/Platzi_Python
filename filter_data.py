from data_db import DATA

def main():
    all_python_devs = [worker['name'] for worker in DATA if worker ['language'] == 'python']
    all_platzi_devs = [worker['name'] for worker in DATA if worker ['organization'] == 'Platzi']

    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults_two = list(map(lambda worker: worker ['name'], adults))

    old_people = list(map(lambda worker: worker | {"old": worker ['age'] > 70}, DATA))

    print('\nAll Python Devs')
    print(all_python_devs)

    print('\n\n')

    print('All Platzi Devs')
    print(all_platzi_devs)

    print('\n\n')

    print('Adults')
    print(adults)

    print('\n\n')

    print('Adults II')
    print(adults_two)

    print('\n\n')

    print('Old People')
    print(old_people)


if __name__ == '__main__':
    main()