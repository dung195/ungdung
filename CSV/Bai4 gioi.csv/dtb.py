import csv
with open("diem_trungbinh.csv") as file,\
     open("gioi.csv",'w') as out:
    reader=csv.reader(file)
    ans=[]
    for row in reader:
        if(row[0]=='HoTen'):
            continue
        else:
            if float(row[1]) >= 8.0:
                ans.append(row)
            
    writer=csv.writer(out)
    writer.writerows(ans)

    file.close()
    out.close()