Number=int(input("please enter any number:"))
Count=0
while(Number > 0):
    Number = Number //10
    Count = Count + 1
print("\n number of digits in a given number=%d" %Count)    