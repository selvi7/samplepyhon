def findDuplicate(arr, n, k): 
      
    arr.sort() 
    i = 0
    while (i < n): 
        j, count = i + 1, 1
        while (j < n and arr[j] == arr[i]): 
            count += 1
            j += 1
   
        if (count == k): 
            return arr[i] 
   
        i = j 
          
    return -1
arr = [ 2, 5, 5, 3, 2 ]; 
k = 2
n = len(arr) 
print (findDuplicate(arr, n, k) )
