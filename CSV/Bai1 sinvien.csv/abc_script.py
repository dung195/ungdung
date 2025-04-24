import csv
import random

import os

if os.path.exists("sinhvien.csv") and os.path.getsize("sinhvien.csv") > 0:
    with open("sinhvien.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            #print(row)
            if(row[0]=='HoTen'):
                continue
            else:
                print("Họ tên: "+row[0],end=" | ")
                print("Tuổi: "+row[1],end=" | ")
                print("Lớp: "+row[2])
#print("The file 'sinhvien.csv' does not exist or is empty.")