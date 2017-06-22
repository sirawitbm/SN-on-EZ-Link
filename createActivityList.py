# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:55:49 2017

@author: SIRAWITBUTMARATTHAYA
"""
import pandas as pd

#==============================================================================
# Convert time string to integer as number of seconds
#==============================================================================
def to_seconds(line):
    hh, mm, ss = [int(x) for x in line.split(':')]
    return hh*3600 + mm*60 + ss

def to_agentNo(cardID):
    agentNo = agentDf[agentDf['cardID'] == cardID]['agentNo']
    return agentNo


#==============================================================================
# Reading input file and manipulate dataset
#==============================================================================
print("reading file...") # 2015-12-25, ezLarge
df = pd.read_csv("./2015-12-25.csv")
df = df[(df['travelMode'] == "Bus") & (df['endDate'] != '0000-00-00')]
df = df[['cardID','busRegNum','busTripNum','startTime','endTime']]
df['busTripNum'] = df['busTripNum'].map(int)
df['startTime'] = df['startTime'].map(to_seconds)
df['endTime'] = df['endTime'].map(to_seconds)
df.sort_values(['cardID', 'startTime'], ascending=[True, True], inplace=True)

print("creating agent list")
agentList = list(df.cardID.unique())
agentList.sort()

print("creating location list")
locationList = list(set(zip(df.busRegNum, df.busTripNum)))
locationList.sort()

global agentDf
agentDf = pd.read_csv("./agentList.csv")

df['agentNo'] = df['cardID'].map(to_agentNo)