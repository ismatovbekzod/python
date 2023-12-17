# Ma'lumotlar ro'yxatlari
l1 = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]

# Bo'sh list yaratish
natija = []

# Har bir o'quvchi raqami, ismi va baho ma'lumotlarini alohida lug'atga o'zlashtirib qo'shish
for i, j, k in zip(l1, l2, l3):
    natija.append({i: {j: k}})

print(natija)
