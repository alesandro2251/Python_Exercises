# User enters n numbers, find largest of these (n entered by user)

x = int(input('How many numbers ? :'))
y = int(0)

for i in range(0, x):
    n = int(input())
    if n > y:
        y = n

print('Largest number is :', y)
