try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print( x / y)
except (ZeroDivisionError,TypeError) as e:
    print('Not Good!')