p11=int(input("Enter the num:"))
q11=int(input("Enter the num:"))
for i in range(1,min(p11,q11)+1):
    if((p11%i==0) and (q11%i==0)):
        x=i
print(x)
