a,b = list(map(int,input("enter the num:")))
c,d = list(map(int,input("enter the num:")))
e,f = list(map(int,input("enter the num:")))
if a==b or c==d or e==f or a==b==e or b==d==f:
    print('yes')
else:
    print('no')
