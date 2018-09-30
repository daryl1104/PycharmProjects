# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

agentDataFrame=pd.read_csv("data/agent-0919-3.csv")
skill7054DataFrame=agentDataFrame[agentDataFrame["skill"]==7054]
#print(skill7062DataFrame)

skill7054DataFrame["busy"]=skill7054DataFrame["queue"]+skill7054DataFrame["dialing"]+skill7054DataFrame["acw"]

outboundDataFrame=pd.read_csv("data/outbound.csv")
outbound7054DataFrame=outboundDataFrame[outboundDataFrame["skill"]==7054]
#print(outbound7020DataFrame["call_time"])

timeindexList=[]
indexList=skill7054DataFrame["time"].index.tolist()
timebooleanList=[]
timeList=(outbound7054DataFrame["call_time"]>skill7054DataFrame["time"][indexList[900]]).tolist()

#print(outbound7054DataFrame.iloc[:,0].size)


#----输出y_train:  11569
labelList=[]
labelList=skill7054DataFrame["busy"].tolist()

y=np.array(labelList,float)


#print(labelList)
