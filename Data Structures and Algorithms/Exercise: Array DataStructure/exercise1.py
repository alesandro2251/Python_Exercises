month_expenses = [2200, 2350, 2600, 2130, 2190]


def month_compare(x, y):
    return x - y


def q1_expenses(arr, result=0):
    for i in range(3):
        x = arr[i]
        result += x
    return result


def equal_calc(arr):
    for i in arr:
        if i == 2000:
            return i


def add_month(x):
    month_expenses.append(x)
    return month_expenses


def make_correction(arr, x, y):
    arr[x] -= y
    return arr


print(month_compare(month_expenses[1], month_expenses[0]))
print(q1_expenses(month_expenses))
print(equal_calc(month_expenses))
print(add_month(1980))
print(make_correction(month_expenses, 3, 200))
