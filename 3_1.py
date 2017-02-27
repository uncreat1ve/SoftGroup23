def func(word):
    word = word.lower().replace(' ', '')
    a = word[::-1]
    if word == a:
        return True
    else:
        return False


print func('Abc b   a')
