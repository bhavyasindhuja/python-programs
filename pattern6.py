n=5
k=1
for i in range(n):
    for j in range(n-1-i+1):
      print(k,end=" ")
      k+=1
    print()