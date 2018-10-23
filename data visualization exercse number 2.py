import pygal
import csv
from datetime import datetime
from  matplotlib import pyplot as plt
filename='activity.csv'
with open(filename) as f:
     reader=csv.reader(f)
     header_row=next(reader)
     current_date = datetime.strptime("2012-10-01", "%Y-%m-%d")
     day=[]
     steps_per_day=[]
     value_of_steps=[]
     steps_total=0
     interval=[]
     average=[]

     for i in range(0,2360,5):
         interval.append(i)
         i+=5

     for x in interval:
         f.seek(0)
         next(f)
         for row in reader:
            if int(row[2])==int(x):
                try:
                    number_of_steps=int(row[0])
                    steps_total+=int(row[0])
                except ValueError:
                    continue
         steps_per_day.append(steps_total)
         steps_total = 0

for i in steps_per_day:
    x=(int(i)/53)
    average.append(x)

maximum=max(average)
ind=average.index(maximum)
print(interval[ind])
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(interval, steps_per_day, c='red',alpha=0.5)
plt.title("Average of steps per interval", fontsize=24)
plt.xlabel('Interval', fontsize=16)
plt.ylabel("Number of steps", fontsize=16)
plt.show()






