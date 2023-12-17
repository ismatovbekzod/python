a = int(input("A ni kiriting : "))
b = int(input("B ni kiriting : "))
arr = []

if a % 2 == 0:
    a += 1

for i in range(b, a-1, -1):
    if i % 2 == 1:
        arr.append(i)
        
print(arr)