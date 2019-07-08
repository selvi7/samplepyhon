x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
for num in range(x,y+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num,"is an amstorng number")
    else:
        print(num,"is not an amstong number")    

