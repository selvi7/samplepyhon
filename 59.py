num = int(input("Enter a number:"))
count = 0
while(num>0):
    num=num//10
    count=count+1
print("The num of digits is:",count)    
