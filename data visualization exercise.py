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
     steps_total=0
     for row in reader:
        if current_date==datetime.strptime(row[1], "%Y-%m-%d"):
            try:
                number_of_steps=int(row[0])
            except ValueError:
                continue
            else:
                steps_total+=number_of_steps
        else:
            steps_per_day.append(steps_total)
            day.append(current_date)
            steps_total=0
            current_date=datetime.strptime(row[1], "%Y-%m-%d")
            try:
                number_of_steps=int(row[0])
            except ValueError:
                continue
            else:
                steps_total+=number_of_steps

steps_per_day.append(steps_total)
day.append(current_date)
hist = pygal.Bar()
hist.title = "Steps per day"
hist.x_title = "date"
hist.y_title = "Number of steps per day"
hist.add('Steps per day', steps_per_day)
hist.render_to_file('die_visual.svg')
sum=0
lenght=day.__len__()
print(lenght)
for i in steps_per_day:
    sum+=int(i)
print(sum)
mean=sum/(lenght)
print("the mean"+" "+str(mean))
newlist=[]
for j in sorted(steps_per_day):
    newlist.append(j)
print(newlist[30])






































































































































































































































































































































































































































