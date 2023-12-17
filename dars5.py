ls= [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2,4,4,4,4]
sanoq = ls[0]

for i in ls:
    if ls.count(sanoq) < ls.count(i):
        sanoq = i
print(sanoq)