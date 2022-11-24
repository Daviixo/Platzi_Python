user_option = int(input('Numero?\n'))

try:
    print(10 / user_option)

except ZeroDivisionError as error:
    print(error)

