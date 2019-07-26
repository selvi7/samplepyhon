x = int(input("Enter the num:"))
y = int(input("Enter the num:"))
for i in range(1,min(x,y)+1):
    if (x%i==0)and(y%i==0):
        x=i
        print(x)
