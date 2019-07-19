a = int(input("Please Enter the First Num of an A.P Series: : "))
n = int(input("Please Enter the Total Num in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

sum = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of the Arithmetic Progression Series = " , sum)
print("The tn Term of the Arithmetic Progression Series = " , tn)
