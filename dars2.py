ls = [1, 2, "abcd",2,3,5,"weq",7, "wqsa", "asd"]
son =0
mx = 0
for i in ls:
    if  isinstance(i,int) == True:
        if mx < i:
            mx = i
print(mx)