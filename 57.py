y=[]
x=int(input("Enter number of elements:"))
for i in range(1,x+1):
    b=int(input("Enter element:"))
    y.append(b)
k=0
num=int(input("Enter the number to be counted:"))
for j in y:
    if(j==num):
        k=k+1
print("Number of times",num,"appears is",k)