r,y=map(int,input("Enter the num:"))
t=list(map(int,input("Enter the num:")[:r]))
for c in range (0,y):
	t=[t[-1]]+t[:-1]
for l in t:
	print(l,end=" ")