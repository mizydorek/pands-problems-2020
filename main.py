try:
    b = 2
    a = b

    b[10] = 'this is not good'
except NameError as ne:
    print('a Name error occured')
    print(ne)
except Exception as e:
    print(e)