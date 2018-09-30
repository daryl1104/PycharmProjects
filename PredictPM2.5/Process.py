# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mtl
import matplotlib.pyplot as plt

originDataFram=pd.read_csv("data/train.csv")
pm2_5=originDataFram[originDataFram['obvservations']=='PM2.5'].ix[:,3:]
#print(pm2_5)

trainList=[]
labelList=[]
for i in range(15):
    trainDataFrame=pm2_5.ix[:,i:i+9]
    trainDataFrame.columns=np.array(range(9))
    labelDataFrame=pm2_5.ix[:,i+9]
    labelDataFrame.columns=["1"]
    trainList.append(trainDataFrame)
    labelList.append(labelDataFrame)

xdata=pd.concat(trainList)
ydata=pd.concat(labelList)
x=np.array(xdata,float)
y=np.array(ydata,float)

# 使用gradient descent训练数据，learning rate:adagrade


x=np.concatenate((np.ones((x.shape[0],1)),x),axis=1)   #feature加入bias
print(x[0])

w=np.zeros((len(x[0])))

lr=10
iteration=10000
s_grad=np.zeros(len(x[0]))

for i in range(iteration):
    tem=np.dot(x,w)  #预测值
    loss=y-tem
    grad=np.dot(x.transpose(),loss)*(-2)
    s_grad+=grad**2
    ada=np.sqrt(s_grad)
    w=w-lr*grad/ada

print(w)

#----------------------- 预测验证 --------------------------
testDataFrame=pd.read_csv("data/test.csv")
pm2_5=testDataFrame[ testDataFrame["obvservations"]=="PM2.5" ]
x_test=pm2_5.ix[:,2:]
x_test=np.array(x_test,float)
x_test_b=np.concatenate( (np.ones((x_test.shape[0],1)),x_test),axis=1 )
y_star=np.dot(x_test_b,w)
y_pre=pd.read_csv("data/sampleSubmission.csv")
y_pre.value=y_star
y_real=pd.read_csv("data/ans.csv")
error=abs(y_pre.value-y_real.value).sum()/len(y_real.value)
print(error)

#x_plot=y_pre.ix[:,0]
x_plot=range(len(y_pre.ix[:,0]))
y_plot=y_pre.ix[:,1]
y_real_plot=y_real.ix[:,1]
plt.plot(x_plot,y_plot,color="red")
plt.plot(x_plot,y_real_plot,color="blue")
plt.show()