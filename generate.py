import csv
with open('/Users/cngde/Desktop/class.csv',mode='r') as read_file:
    print(read_file.readlines()) 
with open('/Users/cngde/Desktop/class.csv',mode='r', newline='') as csv_file:
    csv_content=csv.reader(csv_file)

    for c in csv_content:
        print(c)
