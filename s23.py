a=list(map(int,input("enter the num:")))
b=list(map(int,input("enter the num:")))
c=[]
for i in range(len(b)):
  a.append(b[i])
  c.append(max(a))
print(*c,sep=' ')
