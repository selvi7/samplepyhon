def hasArrayTwoCandidates(B,arr_size,sum): 
      
    # sort the array 
    quickSort(B,0,arr_size-1) 
    l = 0
    r = arr_size-1
      
    # traverse the array for the two elements 
    while l<r: 
        if (B[l] + B[r] == sum): 
            return 1
        elif (B[l] + B[r] < sum): 
            l += 1
        else: 
            r -= 1
    return 0
  
# Implementation of Quick Sort 
# A[] --> Array to be sorted 
# si  --> Starting index 
# ei  --> Ending index 
def quickSort(B, si, ei): 
    if si < ei: 
        pi=partition(B,si,ei) 
        quickSort(B,si,pi-1) 
        quickSort(B,pi+1,ei) 
  
# Utility function for partitioning the array(used in quick sort) 
def partition(B, si, ei): 
    x = B[ei] 
    i = (si-1) 
    for j in range(si,ei): 
        if B[j] <= x: 
            i += 1
              
            # This operation is used to swap two variables is python 
            B[i], B[j] = B[j], B[i] 
  
        B[i+1], B[ei] = B[ei], B[i+1] 
          
    return i+1
      
  
# Driver program to test the functions 
B = [1,4,45,6,10,-8] 
n = 16
if (hasArrayTwoCandidates(B, len(B), n)): 
    print("Array has two elements with the given sum") 
else: 
    print("Array doesn't have two elements with the given sum") 
  
## This code is contributed by __Devesh Agrawal__ 
