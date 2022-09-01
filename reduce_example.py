from functools import reduce

def main():
    
    my_list = [2,2,2,2,2]

    all_mult = reduce(lambda a, b: a * b, my_list)

    print(all_mult)


if __name__ == '__main__':
    main()


# To understand better https://miro.medium.com/max/1200/1*DreeF8a4h2pvxRly39HjAA.jpeg