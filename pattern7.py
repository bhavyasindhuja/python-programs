for i in range(4):
    n=1
    for j in range(4-1-i+1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print(n,end=" ")
        n+=1
    print()    
