tub = (121, 12, 13, 1, 4, 5, 6, 7, 8, 97, 10)
arr = []
for i in range(len(tub)):
    sanoq = 0
    for j in range(2,len(tub)//2):
        if tub[i] % 2 == 0:
            sanoq += 1
    if sanoq == 0 and tub[i] != 1:
        arr.append(tub[i])
            
print(arr)
mx = max(arr)
mn = min(arr)
print(mx)
print(mn)
        
    
        