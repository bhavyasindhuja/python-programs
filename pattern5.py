n=5

for i in range(n):
    k='E'
    for j in range(n-1-i+1):
     print(k,end=" ")
     k=chr(ord(k)- 1)
    print()