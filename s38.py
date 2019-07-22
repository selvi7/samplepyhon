N=int(input("Enter the num:"))
for i in range(2,N+1,2):
    if N%i==0:
        print(i,end=" ")
