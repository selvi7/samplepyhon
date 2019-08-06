# Python3 Program to find minimum K such  
# that every substring of length atleast  
# K contains some character c  
  
# This function checks if there exists  
# some character which appears in all  
# K length substrings  
def check(S, K):  
  
    # Iterate over all possible characters  
    for ch in range(0, 26):  
        c = chr(97 + ch) # Ascii value of 'a' => 97 
  
        # stores the last occurrence  
        last = -1
  
        # set answer as true  
        found = True
        for i in range(0, K):  
            if S[i] == c:  
                last = i  
  
        # No occurrence found of current character  
        # in first substring of length K  
        if last == -1:  
            continue
  
        # Check for every last substring  
        # of length K where last occurr-  
        # ence exists in substring  
        for i in range(K, len(S)): 
            if S[i] == c:  
                last = i  
  
            # If last occ is not  
            # present in substring  
            if last <= (i - K):  
                found = False
                break
              
        # current character is K amazing  
        if found:  
            return 1
      
    return 0
  
# This function performs binary search  
# over the answer to minimise it  
def binarySearch(s):  
  
    low, high, ans = 1, len(s), None
      
    while low <= high:  
        mid = (high + low) >> 1
  
        # Check if answer is found  
        # try to minimise it  
        if check(s, mid):  
            ans, high = mid, mid - 1
          
        else: 
            low = mid + 1
      
    return ans  
  
# Driver Code 
if __name__ == "__main__":  
  
    s = "abcde"
    print(binarySearch(s))  
  
    s = "aaaa"
    print(binarySearch(s))  
  
