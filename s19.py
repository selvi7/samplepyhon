A=int(input("Enter the num:")) 
B=[] 
for i in range (2,A+1): 	
     if(A%i)==0:
         B.append(i)
         A=A//i 
C=sorted(B) 
print(*C)
