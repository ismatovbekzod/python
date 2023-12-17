import os
os.system("cls")
import math
#1-misol
# def  juft(son):
#     if son % 2 ==0:
#         print(True)
#     else:
#         print(False)
    
# juft(int(input("Son kiriting : ")))

#2-misol
# def  manfiy(son):
#     if son > 0:
#         print(True)
#     else:
#         print(False)
    
# manfiy(int(input("Son kiriting : ")))

#3misol
def tub(son):
    if son < 2:
        return False    
    for i in range(2, int(math.sqrt(son)) + 1):
        if son % i == 0:
            return False
    
    return i

n = int(input("Son kiriting : "))
print(tub(n))

#4-misol

# def tip(son):
#     if type(son) == list or type(son) == tuple or type(son) == set or type(son) == dict:
#         print(True)
#     else:
#         print(False)

# x = [2,4,3,2] 
# tip(x)

#5-misol
# def ls(son):
    
#     x.sort(reverse=True)
#     return tuple(x)
# x = [2,4,3,2,5,3,7]    
# print(ls(x))

#6-misol

# def tortbur(a,b):
#     per = 2*(a+b)
#     yuza = a*b
#     ls = tuple([per,yuza])
#     return (ls)

# x = 5
# y = 6
# print(tortbur(x,y))

# 7-misol

# def daraja(x):
#     return list(map(lambda x: x*x,x)) 


# n = 5
# x =[]
# for i in range(5):
#     x.append(int(input(f"{i}-soni kiriting : ")))
# print(daraja(x))

# 8-misol
# def text(a,b):
    
#     ind = txt.rfind(belgi)    
#     print(ind)
# txt = "Hello, welcome to my world"
# belgi = 'o'    
# text(txt,belgi)

#9-misol
# def text(a):
#     katta = 0
#     kichik =0
#     for i in txt:
#         if i.isupper():
#             katta += 1
#         elif i.islower():
#             kichik += 1
#     print(katta,kichik)    
                
# txt = "Good Luck"
# text(txt)

#10-misol
# def daraja(n,dc):
#     for i in range(1,n+1):
#         dc[i] = i*i
        
#     return dc
# n=5
# dc = dict()
# print(daraja(n,dc))

#11-misol
# def daraja(a,b):
#     ls = []
#     for i in range(b):
#         if i*i > a and i*i < b:
#             ls.append(i)
#     return ls
# q = 15
# w = 40
# print(daraja(q,w))

# def tub(son):
#     if son < 2:
#         return False    
#     for i in range(2, int(math.sqrt(son)) + 1):
#         if son % i == 0:
#             return False
#         else:
#             print(i)
# n = 10
# tub(10)
