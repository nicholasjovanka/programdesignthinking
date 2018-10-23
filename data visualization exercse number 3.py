import pygal
import csv
from datetime import datetime
from  matplotlib import pyplot as plt
filename='activity.csv'
newfile='newfile.csv'
with open(filename) as f:
     reader=csv.reader(f)
     header_row=next(reader)
     current_date = datetime.strptime("2012-10-01", "%Y-%m-%d")
     database=[]
     steps_total=0
     steps_per_day=[]
     b=0
     for row in reader:
         if row[0]=="NA":
             database.append('0')
         else:
             database.append(row[0])
         if current_date==datetime.strptime(row[1], "%Y-%m-%d"):
             steps_total+=int((database[b]))
             b+=1
         else:
             steps_per_day.append(steps_total)
             steps_total=0
             current_date=datetime.strptime(row[1], "%Y-%m-%d")
             steps_total+=int((database[b]))
             b+=1
steps_per_day.append(steps_total)
print(len(steps_per_day))
hist = pygal.Bar()
hist.title = "Steps per day"
hist.x_title = "date"
hist.y_title = "Number of steps per day"
hist.add('Steps per day', steps_per_day)
hist.render_to_file('no3_visual.svg')
sum=0
lenght=len(steps_per_day)
print(lenght)
for i in steps_per_day:
    sum+=int(i)
print(sum)
mean=sum/(lenght)
print("the mean"+" "+str(mean))
newlist=[]
for j in sorted(steps_per_day):
    newlist.append(j)
print(newlist[int(len(newlist)/2)])

