import os as os
import pandas as pd
os.chdir("/Users/xinzhang/Documents/MachineLearningCompetitions/Kaggle_Geek/bikeDemand")
data = pd.read_csv("train_1.csv")
#data = pd.read_csv("finaldata.csv")
temp = data[['date','holiday']].copy()
temp1 = temp.dropna()
temp2 = temp1.drop_duplicates()
data1 = pd.merge(data, temp2, on = 'date', how = 'left')
g = data1.groupby(['month','weekday','hour','workingday'])
avgCounts = g[['count']].mean()

testData = pd.read_csv("test.csv")
avgCounts1 = avgCounts.reset_index()
result = pd.merge(testData, avgCounts1, on = ['month','weekday','hour','workingday'], how = 'left')
result.to_csv('testResult1.csv')

g2 = data1.groupby(['month','workingday','hour'])
avgCountsNonwork = g2[['count']].mean()
avgCountsNonwork1 = avgCountsNonwork.reset_index()

result2 = pd.merge(result, avgCountsNonwork1, on = ['month','workingday','hour'], how = 'left')
result2.to_csv('testResult2.csv')

dataNew = pd.merge(data, avgCounts1, on = ['month','weekday','hour','workingday'])
dataNew['dif']=dataNew.count_x-dataNew.count_y

dataNew1 = dataNew[dataNew['dif']!=0]
dataNew1.to_csv('trainNew.csv')
