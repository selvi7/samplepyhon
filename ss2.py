n=int(input("enter the num:"))
y=int(input("enter the num:"))
n,y.sort()
if __name__=='__main__': 
    arr = [n,y] 
    n = len(arr) 
    y = 2
    print("y'th smallest element is", 
          ythSmallest(arr, n, y)) 
