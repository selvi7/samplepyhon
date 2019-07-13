x=0
a,b=map(int,input().split())
y=list(map(int,input().split()))[:a]
for s in y:
  if s==b:
    x+=1
if(x!=0):
  print("yes")
else:
  print("no")
