import pygal
import csv
from datetime import datetime
from  matplotlib import pyplot as plt
filename='activity.csv'
with open(filename) as f:
     reader=csv.reader(f)
     header_row=next(reader)
     current_date = datetime.strptime("2012-10-01", "%Y-%m-%d")
     steps=[]
     date=[]
     interval=[]
     steps_total=0
     steps_weekday=0
     steps_weekend=0
     b=0
     rows=0
     count=0
     weekdy=[]
     weeknd=[]
     newweekdy=[]
     newweeknd=[]
     day=[]
     for row in reader:
         date.append(row[1])

         current_dates=datetime.strptime(row[1], "%Y-%m-%d")
         if current_dates==current_date:
             try:
                 intervals=int(row[2])
                 interval.append(intervals)
             except ValueError:
                 continue
         else:
             break
     print(interval)
     date=list(set(date))
     for x in interval:
         f.seek(0)
         next(f)
         for row in reader:
             checker=int(row[2])
             try:
                 if int(x)==int(row[2]):
                     for b in date:
                         current_date=datetime.strptime(row[1], "%Y-%m-%d")
                         if current_date==b:
                             if count%7<5:
                                 steps_weekday+=(int(row[0]))
                             elif count%7>4:
                                 steps_weekend+=(int(row[0]))
                         else:
                             if count%7<5:
                                 steps_weekday+=(int(row[0]))
                             elif count%7>4:
                                 steps_weekend+=(int(row[0]))
                             count+=1
                 else:
                     continue
             except ValueError:
                 continue
         weekdy.append(steps_weekday)
         weeknd.append(steps_weekend)
         steps_weekday=0
         steps_weekend=0

     count=len(weeknd)
     count1=len(weekdy)

     for z in weekdy:
         newval=z/count
         newweekdy.append(newval)
     for z in weeknd:
         newval=z/count
         newweeknd.append(newval)

print(newweekdy)
print(newweeknd)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(interval, newweekdy, c='red',alpha=0.5)
plt.plot(interval, newweeknd, c='blue',alpha=0.5)
plt.title("Average of steps per interval", fontsize=24)
plt.legend(["Weekday","Weekend"])
plt.xlabel('Interval', fontsize=16)
plt.ylabel("Number of steps", fontsize=16)
plt.axis([0,2500,0,70])
plt.show()
