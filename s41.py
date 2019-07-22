n1=int(input("Enter the num:"))
m1=int(input("Enter the num:"))
a=1
for i in range(1,100):
    if(pow(m1,i)==n1):
        print("yes")
        a=0
        if(a==1):
            print("no")
