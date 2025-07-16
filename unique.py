str="dhavileswarapu"
frq=[0]*26

for i in str:
        ind=ord(i)-ord('a')
        frq[ind]+=1

for i in range(len(frq)):
    if(frq[i]>0):
        print((frq[i]) ,":",chr(ord('a')+i), sep="")
                       



