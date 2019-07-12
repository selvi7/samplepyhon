x = int(input('How many numbers: '))
total_sum = 0
for n in range(x):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/x
print('Average a ', x, ' numbers is :', avg)
