import csv

du_lieu = [
    ['Ten', 'Tuoi', 'KinhNghiem', 'KyNang'],
    ['Nguyen Van A', 21, 2, 'Lap trinh Python'],
    ['Tran Thi B', 23, 1, 'Thiet ke do hoa'],
    ['Le Van C', 25, 4, 'Quan tri']
]

with open('hosoxinviec.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(du_lieu)

print("Đã tạo file hosoxinviec.csv!")
