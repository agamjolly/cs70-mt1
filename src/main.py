import numpy as np
import os
import time
import pandas as pd
import statistics
import xlrd
from collections import Counter
from flask import *

"""
cs70 midterm 1 stats<br>
last modified: {{ last }}<br>
<br>
mean: {{ mean }}<br>
median: {{ median }}<br>
standard deviation: {{ std }}<br>
"""

df = pd.read_excel('Book1.xlsx')
a = df['marks'].tolist()
app = Flask(__name__)
path = os.path.getmtime('Book1.xlsx')
last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(path))

def mean(data=a):  
    return float(sum(data)/len(data))

def standard_deviation(data=a): 
    return statistics.stdev(data)
    
def median(data=a): 
    new_data = sorted(data)
    med1 = new_data[len(new_data)//2]
    if not len(data)%2: 
        med2 = new_data[(len(data)//2)-1]
        return float((med1+med2))/2
    return med1

def std_minus(data=a): 
    return [(round((median()-i*standard_deviation()),2)) for i in np.arange(0.5, 2.0, 0.5)]

def std_plus(data=a): 
    return [(round((median()+i*standard_deviation()),2)) for i in np.arange(0.5, 2.0, 0.5)]

def mode(data=a):
    counter_a = Counter(a)
    highest = max([counter_a[i] for i in counter_a])
    freq = [i for i in counter_a if counter_a[i]==highest]
    return mean(freq)

plus = ["+0.5 STD: ", "+1.0 STD: ", "+1.5 STD: "]
minus = ["-0.5 STD: ", "-1.0 STD: ", "-1.5 STD: "]


score_wise = [0, 0, 0, 0, 0, 0, 0]

for i in a: 
    if i in range(10,20): 
        score_wise[0]+=1
    elif i in range(20,30): 
        score_wise[1]+=1
    elif i in range(30,40): 
        score_wise[2]+=1
    elif i in range(40,50): 
        score_wise[3]+=1
    elif i in range(50,60): 
        score_wise[4]+=1
    elif i in range(60,70): 
        score_wise[5]+=1
    else: 
        score_wise[6]+=1


@app.route('/')
def index(): 
    return render_template('index.html', mean=(round(mean(),2)), median=(round(median(),2)), mode=mode(), std=(round(standard_deviation(),2)), a=sorted(a), last=last_time, total=len(a), hi=max(a), lo=min(a), std_plus=dict(zip(plus, std_plus())), std_minus=dict(zip(minus, std_minus())), thresholds=[i for i in score_wise], numbers=score_wise)

# Driver code
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    """
    print("------------------------------"+ "\nCS70 Midterm 1 Stats")
    print("Last modified: " + str(last_time))
    print("------------------------------")
    print("Total entries: " + str(len(a)))  
    print("Median: "+ str(round(median(),2)))
    print("Mean: "+ str(round(mean(),2)))
    print("Standard Deviation: "+ str(round(standard_deviation(),2)))
    print("Highest Score: " + str(max(a))) 
    print("Lowest Score: " + str(min(a)))
    print("------------------------------")
    for i in np.arange(0.5, 2.0, 0.5):
        print("-" + str(i) + " STD: " + str(round((median()-i*standard_deviation()),2)))
    print("------------------------------")
    for i in np.arange(0.5, 2.0, 0.5):
        print("+" + str(i) + " STD: " + str(round((median()+i*standard_deviation()),2)))
    print()
    """