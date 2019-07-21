import math
a=int(input("Enter the num:"))
b=int(input("Enter the num:"))
count=0
for i in range(a,b+1):
    s=math.sqrt(i)
    if math.sqrt(i)==int(s):
        count+=1
print(count)
