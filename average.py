import plotly.figure_factory as ff
import statistics
import random
import pandas as pd 
import csv
df = pd.read_csv("average.csv")
avg = df['average'].tolist()
avgmean = statistics.mean(avg)
standarddeviation = statistics.stdev(avg)
print(standarddeviation)
print(avgmean)
def randomsetofmean(counter):
    dataset  =[]
    for i in range(0,counter):
        randomindex = random.randint(0,len(avg)-1)
        value = avg[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)
def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["avg"],show_hist = False)
    fig.show()
def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    sd = statistics.stdev(meanlist)
    print(mean,sd)
setup()                    