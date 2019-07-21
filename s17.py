l = int(input("Enter the num:"))
r = int(input("Enter the num:"))
num = 1
while(num>0):
    if((num%l)==0 and (num%r)==0):
        print(num)
        num = 0
    else:
        num+=1    

