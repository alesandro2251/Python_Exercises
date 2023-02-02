# This is a calculator with which you can see the real rate of return earned on an investment,
# taking into account the effect of compounding interest.

start_sum = float(input('Enter the starting sum :\n'))
period = int(input('Enter the period in years :\n'))
yield1 = float(input('Enter the yield :\n'))
x = float()
i = 0

for i in range(period):
    i += 1
    x = float(start_sum + (start_sum * (yield1 / 100)))
    start_sum = x

print('Total earned :', x)
