s,r=list(map(int,input("enter the num:")))
t,o=list(map(int,input("enter the num:")))
p,q=list(map(int,input("enter the num:")))
if s==r or t==o or p==q or s==t==p or r==o==q:
    print('yes')
else:
    print('no')
