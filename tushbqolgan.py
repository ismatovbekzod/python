n = int(input("N kiriting : "))
arr = []
for i in range(n):
    arr.append(int(input(f"{i}- soni kiriting ")))
arr = set(arr) 
mx = max(arr)
mn = min(arr)
new = []
for i in range(mn,mx):
    if i != arr:
        new.append(arr)    
print(arr)

