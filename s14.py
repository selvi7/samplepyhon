d=(input("Enter the num:"))
s=list(d)
for i in s:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		s.remove(i)
k=s[::-1]
print("".join(k))
