a = int(input("A ni kiriting : "))
b = int(input("B ni kiriting : "))
arr = []

if a % 2 == 1:
    a += 1

for i in range(a,b,1):
    if i % 2 == 0:
        arr.append(i)
        
print(arr)