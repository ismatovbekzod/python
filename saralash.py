n = int(input("N kiriting : "))
arr = []
for i in range(n):
    arr.append(int(input(f"{i}- soni kiriting ")))
    
print(arr)
new = list(set(arr))
print(new)
#for i in range(len(arr)):
 #   for j in range(i+1,len(arr)):
  #      if arr[i] == arr[j]:
   #         arr.remove(arr[j])
#print(arr)