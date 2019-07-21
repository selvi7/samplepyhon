a23=int(input("enter the num:"))
li=list(map(str,input("enter the num:")[:a23]))
li.sort()
li.sort(key=len)
for i in li:
        print(i,end=" ")
