# The user enters an integer (e.g. 123).
# Output the sum of all digits (6).

n = int(input('Enter the number :\n'))
sum1 = int(0)

while n != 0:
    sum1 = int(sum1 + int(n % 10))
    n = int(n / 10)

print('Sum of numbers is :', sum1)
