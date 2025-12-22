import csv


filename = "writing_get.csv"
field_names = ['year','avg grade']

data = [{field_names[0]:0 ,field_names[1]:80},
        {field_names[0]:0 ,field_names[1]:85},
        {field_names[0]:0 ,field_names[1]:90},
        {field_names[0]:0 ,field_names[1]:70},
        {field_names[0]:0 ,field_names[1]:89},]

counter = 0
max_year = 2000 + len(data)
for year in range(2000,max_year):
    data [counter][field_names[0]] = year
    counter +=1

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

with open(filename, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    index = 0
    for row in csv_reader:
        print(row[1])
        if row[1] == "90":
            print(f"{row[1]} found in {index}")
            year = row[0]
            print(f"year : {year}")
        index += 1




