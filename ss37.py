# Python 3 program to find minimum 
# step to delete a string 
  
# method returns minimum step for  
# deleting the string, where in one  
# step a palindrome is removed  
def minStepToDeleteString(str): 
  
    N = len(str) 
  
    # declare dp array and initialize  
    # it with 0s 
    ds = [[0 for x in range(N + 1)] 
             for y in range(N + 1)] 
  
    # loop for substring length 
    # we are considering 
    for l in range(1, N + 1): 
          
        # loop with two variables i and j, denoting 
        # starting and ending of substrings 
        i = 0
        j = l - 1
        while j < N: 
          
            # If substring length is 1,  
            # then 1 step will be needed 
            if (l == 1): 
                ds[i][j] = 1
            else: 
              
                # delete the ith char individually 
                # and assign result for subproblem (i+1,j) 
                ds[i][j] = 1 + ds[i + 1][j] 
  
                # if current and next char are  
                # same, choose min from current  
                # and subproblem (i+2,j) 
                if (str[i] == str[i + 1]): 
                    ds[i][j] = min(1 + ds[i + 2][j], ds[i][j]) 
  
                ''' loop over all right characters and suppose 
                    Kth char is same as ith character then 
                    choose minimum from current and two 
                    substring after ignoring ith and Kth char '''
                for K in range(i + 2, j + 1): 
                    if (str[i] == str[K]): 
                        ds[i][j] = min(ds[i + 1][K - 1] + 
                                       ds[K + 1][j], ds[i][j]) 
                          
            i += 1
            j += 1
  
    # Uncomment below snippet to print  
    # actual dp tablex  
    # for (int i = 0; i < N; i++, cout << endl) 
    # for (int j = 0; j < N; j++) 
    #     cout << dp[i][j] << " ";  
  
    return ds[0][N - 1] 
  
# Driver Code 
if __name__ == "__main__": 
    str = "2553432"
    print( minStepToDeleteString(str)) 
  
# This code is contributed by ChitraNayal 

