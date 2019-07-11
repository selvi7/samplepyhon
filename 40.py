n = int(input("Enter a number:"))
fab=1
for i in range(1,n+1):
    fab=fab*i
print("The fact of",n,"is",end=" ")
print(fab)     
