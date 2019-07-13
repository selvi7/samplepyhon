num = int(input("Enter a num:"))
if num<0:
    print("pls enter a true num")
else:
    sum=0
while(num>0):
    sum+=num
    num-=1
print("The sum is",sum)