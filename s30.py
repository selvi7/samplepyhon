l1=[str(i) for i in input("Enter the num:")]
s1=l1[0]
s2=l1[1]
k=l1[2]
c=0
for i in range(0,len(s1)):
    if(s1[i]!=s2[i]):
        c=c+1
if(c==int(k)):
    print("yes")
else:
    print("no")
