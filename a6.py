# Python 3 program to 
# find maximum triplet sum 
  
# Function to calculate 
# maximum triplet sum 
def maxTripletSum(arr, m) : 
  
    # Initialize the answer 
    ans = 0
   
    for i in range(1, (m - 1)) : 
        max1 = 0
        max2 = 0
   
        # find maximum value(less than arr[i]) 
        # from i + 1 to n-1 
        for j in range(0, i) : 
            if (arr[j] < arr[i]) : 
                max1 = max(max1, arr[j]) 
   
        # find maximum value(greater than arr[i]) 
        # from i + 1 to n-1 
        for j in range((i + 1), m) : 
            if (arr[j] > arr[i]) : 
                max2 = max(max2, arr[j]) 
   
        # store maximum answer 
        ans = max(ans, max1 + arr[i] + max2) 
   
    return ans 
  
  
# Driver code 
  
arr = [ 2, 5, 3, 1, 4, 9 ] 
m = len(arr) 
print(maxTripletSum(arr, m)) 
  
  
# This code is contributed 
# by Nikita Tiwari. 
