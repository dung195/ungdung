import csv

with open('hosoxinviec.csv', mode='r', encoding='utf-8') as file_in, \
     open('ungvien_tiemnang.csv', mode='w', newline='', encoding='utf-8') as file_out:

    reader = csv.DictReader(file_in)
    fieldnames = ['Ten', 'Tuoi', 'KinhNghiem', 'KyNang']
    writer = csv.DictWriter(file_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        kinh_nghiem = int(row['KinhNghiem'])
        kynang = row['KyNang'].lower()

        if kinh_nghiem >= 2 and 'lap trinh' in kynang:
            writer.writerow(row)

print("Đã lọc và tạo file ungvien_tiemnang.csv!")
