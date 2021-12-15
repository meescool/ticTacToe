def grid(marks):
    # row1 = marks| 2 | 3 '
    # row2 = ' 6 | 5 | 4 '
    # row3 = ' 7 | 8 | 9  '

    hv = '|'
    hr = '=' 

    i = 1
    print()
    for mark in marks:
        if i%3 == 0:
            print(mark)
            print(hr * 11)
        else:
            print(mark,end ='|')
        i+=1
    print()