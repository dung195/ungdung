import csv

with open('diem.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Bỏ qua dòng tiêu đề

    for row in reader:
        ten = row[0]
        toan = float(row[1])
        ly = float(row[2])
        hoa = float(row[3])
        dtb = (toan + ly + hoa) / 3
        print(f"{ten} - ĐTB: {dtb:.2f}")