print('enter a number:')
try:
    x = int(input())
    if x > 0:
        print('given number is positive')
    elif x < 0:
        print('given number is negative')
    else:
        print('number is zero')
except:
    print('Invalid input')