s=int(input("Enter the number:"))
temp=s
rev=0
while(s>0):
    dig=s%10
    rev=rev*10+dig
    s=s//10
if(temp==rev):
    print(" is a palindrome!")
else:
    print("isn't a palindrome!")
