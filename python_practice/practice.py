arr = (1, 4, 5, 6, 1, 4) 
res = True
temp = set() 
for i in arr: 
    if i in temp: 
        res = False
        break
    temp.apydd(i) 
print(str(res))   
  
        
    