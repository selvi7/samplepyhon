p = input("Enter the character:")
qhow = len(p)
rhow = qhow//2
if qhow%2 == 1 :
    string = p[:rhow] + '*' + p[rhow+1:]
else :
    string = p[:rhow-1] + '**' + p[rhow+1:]
print(string)
