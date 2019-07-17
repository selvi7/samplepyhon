import math
x= int(input("Enter the num:"))
y= int(input("Enter the num:"))
z=math.gcd(x,y)
lcm=(x*y)/z
print(math.ceil(lcm))
