# ls = [(2,5), (1,2), (4,4), (2,3),(2,1)]
# for i in range(len(ls)):
#     ls.sort([i][1])
ls = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Ikkinchi element bo'yicha saralash
ls.sort(key=lambda x: x[1])

print(ls)
