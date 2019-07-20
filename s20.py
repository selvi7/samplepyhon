#N

s11=input("Enter the chracter:")


b=[]

for i in s11:

    if(i>='A' and i<='V'):
    
        d=chr(ord(i)+3)
        
        b.append(d)
        
    else:
    
        c=chr(ord(i)-23)
        
        b.append(c)   
        
for i in b:

    print(i,end="")
