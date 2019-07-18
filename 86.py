#a
n=list(input("Enter the num:"))
a=[]
for i in n:
    if i not in a:
        a.append(i)
if(n==a):
    print("Yes")
else:
    print("No")
