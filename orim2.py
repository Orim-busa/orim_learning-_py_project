import json
import csv

x = [2, 5, 3, 7, 4]
y = [4, 6, 2, 8, 1]
z = []

for i in range(len(x)):
    resoult (2 * x[i] * 5 * y[i]) / y[i]
    z.append(result)

with open("orim2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for i in range(x)
    writer.writerow([x[i],  y[i],  z[i]])

data = []

with open("orim2.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

with open("orim2.json" "w") as file:
    json.dump(data, file)
    
