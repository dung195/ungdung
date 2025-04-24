import csv

# Dữ liệu cần ghi vào file
du_lieu = [
    ['HoTen', 'Tuoi', 'Lop'],
    ['Nguyen Van A', 17, '12A1'],
    ['Tran Thi B', 18, '12A2'],
    ['Le Van C', 17, '12A1']
]

# Ghi vào file CSV
with open('sinhvien.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(du_lieu)

print("Đã tạo file sinhvien.csv thành công!")
