import csv

du_lieu = [
    ['HoTen', 'Toan', 'Ly', 'Hoa'],
    ['Nguyen Van A', 8, 7, 9],
    ['Tran Thi B', 6, 5, 7],
    ['Le Van C', 9, 8, 10]
]

with open('diem.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(du_lieu)

print("Đã tạo file diem.csv thành công!")
