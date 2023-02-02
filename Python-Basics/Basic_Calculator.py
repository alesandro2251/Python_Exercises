import math

list = {1: 'Addition',
        2: 'Subtraction',
        3: 'Multiplication',
        4: 'Division',
        5: 'Rooting',
        6: 'Grading',
        7: 'Reciprocity',
        8: 'Percent'}

for a, b in list.items():
    print(a, ':', b)

print()
count = input('Choose action :\n')

if count.isnumeric() in range(1, 8):
    if count == '1':
        x = float(input('Enter X:\n'))
        y = float(input('Enter Y:\n'))
        add = float(float(x) + float(y))
        print('Result is :', add)
    elif count == '2':
        x = float(input('Enter X:\n'))
        y = float(input('Enter Y:\n'))
        subs = float(float(x) - float(y))
        print('Result is :', subs)
    elif count == '3':
        x = float(input('Enter X:\n'))
        y = float(input('Enter Y:\n'))
        mul = float(float(x) * float(y))
        print('Result is :', mul)
    elif count == '4':
        x = float(input('Enter X:\n'))
        y = float(input('Enter Y:\n'))
        div = float(float(x) / float(y))
        print('Result is :', div)
    elif count == '5':
        x = float(input('Enter X:\n'))
        root = float(math.sqrt(float(x)))
        print('Result is :', root)
    elif count == '6':
        x = float(input('Enter X:\n'))
        grading = float(float(x) * float(x))
        print('Result is :', grading)
    elif count == '7':
        x = float(input('Enter X:\n'))
        rec = float(1 / float(x))
        print('Result is :', rec)
    elif count == '8':
        y = float(input('Enter a number:\n'))
        x = float(input('Enter a part:\n'))
        percent = float((float(x) / float(y)) * 100)
        print('Result is :', percent, "%")
else:
    print('Try again! Use numbers!')
