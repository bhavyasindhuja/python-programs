str="abceeabcdfbba"
res=""
str1=""  
for i in range(len(str)):
    if(str[i] not in str1):
        str1+=str[i]
    else:
        if(len(res)<len(str1)):
            res=str1
            str1=""
       
print(res)

        
