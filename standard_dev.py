import math
import csv

with open("data.csv",newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)

    mean=total/n
    return mean

squared_list=[]
for number in data :
    y=int(number)-mean(data)
    y=y**2
    squared_list.append(y)

sum=0
for i in squared_list:
    sum=sum+1

result=sum/(len(data)-1)

standard_dev=math.sqrt(result)
print(standard_dev)
