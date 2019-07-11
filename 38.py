a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))

print("Before Swapping two Number: a = {0} and b = {1}".format(a, b))

a = a ^ b
b = a ^ b
a = a ^ b

print("After Swapping two Number: a = {0} and b = {1}".format(a, b))