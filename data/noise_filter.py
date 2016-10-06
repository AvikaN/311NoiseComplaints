import csv
count = 0 
csvfile = open('filtered_311.csv', newline='', encoding='utf-8')
noise = open('noise_filter.csv', 'w')
reader = csv.reader(csvfile, delimiter = ",")
header = reader.__next__()
columns = ",".join(header) + "\n"
noise.write(columns)
for row in reader:
    if 'Noise' in row[4]:
        new_row = ",".join(row) + "\n"
        noise.write(new_row)

noise.close()
        
          

