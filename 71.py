num=int(input("Enter the num:"))
try:
    val=int(num)
    if num==str(num):
        print("The given num is palndrom")
    else:
        print("The given num is not a palinrom")
except:
    print(" Thats not a valid num  try again")
