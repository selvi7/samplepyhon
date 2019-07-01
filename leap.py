print("enter the number")
try:
    x=int(input())
    if x % 4:
       print("the given year is",x,"leap year")
    else:
       print("the given year is",x,"not leape year")    
except:
       print("invalid input")