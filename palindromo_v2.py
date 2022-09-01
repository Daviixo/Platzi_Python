def main():
    
    word = input('Que palabra o frase deseas comprobar si es o no es un palindromo?\n')
    palindromo = lambda string: string == string[::-1]
    print(palindromo(word.lower().replace(' ', "")))

if __name__ == '__main__':
    main()