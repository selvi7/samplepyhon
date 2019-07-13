num=int(input("Enter the num:"))
sum=0

while (num>0):
    Remainder = num%10
    sum=sum+Remainder
    num=num//10
print("sum of the sum num is= ",sum)    
