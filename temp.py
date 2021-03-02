import plotly.figure_factory as ff 
import statistics 
import random
import csv
import pandas as pd
df=pd.read_csv("temp.csv")
temp = df['temp'].to_list()
populationmean = statistics.mean(temp)
standarddeviation = statistics.stdev(temp)
print(standarddeviation)
print(populationmean)
#fig = ff.create_distplot([temp],["temp"],show_hist = False)
#fig.show()
def randomsetofmean (counter):
    dataset = []
    for i in range(0,counter):
        randomindex  = random.randint (0,len(temp)-1)
        value  = temp[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)     
def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist = False)
    fig.show()
def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    sd=statistics.stdev(meanlist)
    print(mean,sd)
setup()        
