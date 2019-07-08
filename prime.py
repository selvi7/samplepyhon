x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
for i in range(x,y+1):
   if(i>1):
       for n in range(2,i):
           if(i%n)==0:
               break
           else:
               print(i)