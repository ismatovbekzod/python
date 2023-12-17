n = int(input("N kiriting : "))
arr = []
for i in range(n):
    arr.append(int(input(f"{i}- soni kiriting ")))
    
print(arr)
for i in n:
    for j in n:
        if arr[i] == arr[j]:
            arr.remove(arr[j])
print(arr)