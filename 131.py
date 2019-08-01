# position and so on. 
def rearrange(arr, x): 
    # Auxiliary array to hold modified array 
    temp = x*[None] 
  
    # Indexes of smallest and largest elements 
    # from remaining array. 
    small,large =0,x-1
  
    # To indicate whether we need to copy rmaining 
    # largest or remaining smallest at next position 
    flag = True
  
    # Store result in temp[] 
    for i in range(x): 
        if flag is True: 
            temp[i] = arr[large] 
            large -= 1
        else: 
            temp[i] = arr[small] 
            small += 1
  
        flag = bool(1-flag) 
  
    # Copy temp[] to arr[] 
    for i in range(x): 
        arr[i] = temp[i] 
    return arr 
  
# Driver program to test above function 
arr = [1, 2, 3, 4, 5, 6] 
x = len(arr) 
print("Original Array") 
print(arr) 
print("Modified Array") 
print(rearrange(arr, x)) 
  
# This code is contributed by Pratik Chhajer 

