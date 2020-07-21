import numpy as np
import os
import time
import pandas as pd
import statistics
import xlrd
from collections import Counter
from flask import *
from datetime import datetime
from pytz import timezone

df = pd.read_excel('data.xlsx')
a = df['marks'].tolist()
com = df['comments'].tolist()
app = Flask(__name__)
path = os.path.getmtime('Book1.xlsx')
last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(path))

com = [i for i in com if len(str(i))>3]

def mean(data=a):  
    return float(sum(data)/len(data))

def standard_deviation(data=a): 
    return statistics.stdev(data)
    
def median(data=a): 
    new_data = sorted(data)
    return statistics.median(new_data)

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


score_wise = [0,0,0,0,0,0,0,0]

for i in a:
    if int(i) in range(0,10):
        score_wise[0]+=1
    elif int(i) in range(10,20): 
        score_wise[1]+=1
    elif int(i) in range(20,30): 
        score_wise[2]+=1
    elif int(i) in range(30,40): 
        score_wise[3]+=1
    elif int(i) in range(40,50): 
        score_wise[4]+=1
    elif int(i) in range(50,60): 
        score_wise[5]+=1
    elif int(i) in range(60,70):
        score_wise[6]+=1
    elif int(i) in range(70,100): 
        score_wise[7]+=1


@app.route('/')
def index(): 
    return render_template('index.html', comments=com, mean=(round(mean(),2)), median=(round(median(),2)), mode=mode(), std=(round(standard_deviation(),2)), a=sorted(a), last=last_time, total=len(a), hi=max(a), lo=min(a), std_plus=dict(zip(plus, std_plus())), std_minus=dict(zip(minus, std_minus())), thresholds=[i for i in score_wise], numbers=score_wise)

# Driver code
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)