ls1 = ['S001', 'S002', 'S003', 'S004']
ls2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
ls3 = [85, 98, 89, 92]
ds = dict()
for i in range(len(ls1)):
    ds[ls1[i]] = {ls2[i] : ls3[i]}

print(ds)