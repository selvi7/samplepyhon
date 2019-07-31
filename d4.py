def findDuplicate(arr, y, s): 
      
    arr.sort() 
    i = 0
    while (i < y): 
        j, count = i + 1, 1
        while (j < y and arr[j] == arr[i]): 
            count += 1
            j += 1
   
        if (count == s): 
            return arr[i] 
   
        i = j 
          
    return -1
arr = [ 1,2,1,3,2 ]; 
s = 1
y = len(arr) 
print (findDuplicate(arr, y, s) )
  
