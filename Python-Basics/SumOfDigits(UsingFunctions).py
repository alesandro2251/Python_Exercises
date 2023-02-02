# The user enters an integer (e.g. 123).
# Output the sum of all digits (6).


def SumOfDigits(n):
    sum1 = 0
    while n != 0:
        sum1 = int(sum1 + int(n % 10))
        n = int(n / 10)
    return sum1


n = int(input('Enter the number :\n'))
print('Sum of numbers is :', SumOfDigits(n))
