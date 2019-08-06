# Python3 program to find maximum
# occured of a string

# function to return maximum occurred
# substring of a string
def MaxFreq(s):
    n = len(s)
    m = dict()

for i in range(n):
    strng = ""
for j in range(i, n):
    strng += s[j]
if strng in m.keys():
    m[strng] += 1
else:
    m[strng] = 1
    maxi = 0
    maxi_str = ""

for i in m:
    if m[i] > maxi:
        maxi = m[i]
        maxi_str = i
    elif m[i] == maxi:
        ss = i
    if len(ss) > len(maxi_str):
        maxi_str = ss
        return maxi_str
        strng = ""
        print(MaxFreq(strng))

# This code is contributed by Mohit kumar 29
