# A Naive recursive Python program to fin minimum number 
# operations to convert str1 to str2 
def editDistance(str1, str2, A, b): 
  
    # If first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m==0: 
         return b 
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if b==0: 
        return A
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[A-1]==str2[b-1]: 
        return editDistance(str1,str2,A-1,b-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(editDistance(str1, str2, A, b-1),    # Insert 
                   editDistance(str1, str2, A-1, b),    # Remove 
                   editDistance(str1, str2, A-1, b-1)    # Replace 
                   ) 
  
# Driver program to test the above function 
str1 = "sunday"
str2 = "saturday"
print (str1, str2, len(str1), len(str2)) 
  
# This code is contributed by Bhavya Jain 
