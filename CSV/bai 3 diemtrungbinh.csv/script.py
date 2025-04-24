import csv

with open('diem.csv', mode='r', encoding='utf-8') as file_in, \
     open('diem_trungbinh.csv', mode='w', newline='', encoding='utf-8') as file_out:
    
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    header = ['HoTen', 'DTB']
    writer.writerow(header)
    next(reader)  # Bỏ dòng tiêu đề

    for row in reader:
        ten = row[0]
        dtb = (float(row[1]) + float(row[2]) + float(row[3])) / 3
        writer.writerow([ten, round(dtb, 2)])

print("Đã tạo file diem_trungbinh.csv!")
