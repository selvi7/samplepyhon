# A utility function that returns  
# true if there is a subset of 
# arr[] with sun equal to given sum 
def isSubsetSum (arr, m, sum): 
    # Base Cases 
    if sum == 0: 
        return True
    if m == 0 and sum != 0: 
        return False
  
    # If last element is greater than sum, then  
    # ignore it 
    if arr[m-1] > sum: 
        return isSubsetSum (arr, m-1, sum) 
  
    ''' else, check if sum can be obtained by any of  
    the following 
    (a) including the last element 
    (b) excluding the last element'''
      
    return isSubsetSum (arr, m-1, sum) or isSubsetSum (arr, m-1, sum-arr[m-1]) 
  
# Returns true if arr[] can be partitioned in two 
# subsets of equal sum, otherwise false 
def findPartion (arr, m): 
    # Calculate sum of the elements in array 
    sum = 0
    for i in range(0, m): 
        sum += arr[i] 
    # If sum is odd, there cannot be two subsets  
    # with equal sum 
    if sum % 2 != 0: 
        return false 
  
    # Find if there is subset with sum equal to 
    # half of total sum 
    return isSubsetSum (arr, m, sum // 2) 
  
# Driver program to test above function 
arr = [3, 1, 5, 9, 12] 
m = len(arr) 
if findPartion(arr, m) == True: 
    print ("Can be divided into two subsets of equal sum") 
else: 
    print ("Can not be divided into two subsets of equal sum") 
      
# This code is contributed by shreyanshi_arun.      