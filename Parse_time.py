import csv

# Make a csv file.
out_csv = csv.writer(open('OutPut.csv', 'wb'))

# Write header for csv file.
out_csv.writerow(['year', 'month', 'date', 'hour', 'minute', 'second'])

text_file = open("data.txt", "r")
lines = text_file.readlines()
text_file.close()

n = 0
for line in lines: 
    n = n + 1
n = 0
for line in lines: 
    n = n + 1
    if "2013" in line:
        if "[" in line:
            date_time = line.split("[")[0]
            year = date_time.split(" ")[0]
            month = date_time.split(" ")[1]
            day = date_time.split(" ")[2]
            time = date_time.split(" ")[3]
            hour = time.split(":")[0]
            minute = time.split(":")[1]
            second = time.split(":")[2]            

# At the end we save all information for that specific date and then going for other date.             
        out_csv.writerow([year, month, day, hour, minute, second])
