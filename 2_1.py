def func():
    number = input('Type a number: ')
    return not(number) % 2 != 0


if func():
    print('Number you typed is an even number')
else:
    print('Number you typed is an odd number')
