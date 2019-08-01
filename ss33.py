def longestAlternating(arr, x) : 
    count = [None] * x 
  
    # Fill count[] from end.  
    count[x - 1] = 1
    i = x - 2
      
    while i >= 0 : 
        if (arr[i] * arr[i + 1] < 0) : 
            count[i] = count[i + 1] + 1
        else : 
            count[i] = 1; 
        i = i - 1
  
    i = 0
      
    # Print result 
    while i < x : 
        print (count[i], end = " ") 
        i = i + 1
  
# Driver Code 
a = [ -5, -1, -1, 2, -2, -3 ] 
x = len(a) 
longestAlternating(a, x); 
  
  
# This code is contributed by rishabh_jain  

