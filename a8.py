def hasArrayTwoCandidates(a,arr_size,sum): 
      
    # sort the array 
    quickSort(a,0,arr_size-1) 
    l = 0
    r = arr_size-1
      
    # traverse the array for the two elements 
    while l<r: 
        if (a[l] + a[r] == sum): 
            return 1
        elif (a[l] + a[r] < sum): 
            l += 1
        else: 
            r -= 1
    return 0
  
# Implementation of Quick Sort 
# A[] --> Array to be sorted 
# si  --> Starting index 
# ei  --> Ending index 
def quickSort(a, si, ei): 
    if si < ei: 
        pi=partition(a,si,ei) 
        quickSort(a,si,pi-1) 
        quickSort(a,pi+1,ei) 
  
# Utility function for partitioning the array(used in quick sort) 
def partition(a, si, ei): 
    x = a[ei] 
    i = (si-1) 
    for j in range(si,ei): 
        if a[j] <= x: 
            i += 1
              
            # This operation is used to swap two variables is python 
            a[i], a[j] = a[j], a[i] 
  
        a[i+1], a[ei] = a[ei], a[i+1] 
          
    return i+1
      
  
# Driver program to test the functions 
a = [1,4,45,6,10,-8] 
n = 16
if (hasArrayTwoCandidates(a, len(a), n)): 
    print("Array has two elements with the given sum") 
else: 
    print("Array doesn't have two elements with the given sum") 
  
## This code is contributed by __Devesh Agrawal__ 
