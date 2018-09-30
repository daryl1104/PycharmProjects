import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df4=pd.read_csv("data/agent-0919-1.csv")
df2=pd.read_csv("data/outbound.csv")
df4=pd.read_csv("data/agent-0919-3.csv")
#df4=pd.read_csv("data/agent-0919-2.csv")
#df4=pd.read_csv("data/agent-0919-3.csv")
#df4=pd.read_csv("data/agent-0919-4.csv")

#print(df4)
df4=df4[df4["skill"]==7054]
# 获取数据中的技能组
skillList=[]
#print(df4["skill"].get_values())
skillList=list(set(df4["skill"].get_values()))
print((skillList))

df4["busy"]=df4["queue"]+df4["dialing"]+df4["acw"]
print(df4)
#print(list(set(df4["busy"].get_values())))
df4listx=list(range( len(df4.ix[:,0]) ))
df4listy=df4["busy"].tolist()

df2=df2[df2["skill"]==7054]
df2listx=list(range( len(df2.ix[:,0])))
df2listy=df2["count(*)"].tolist()


plt.plot(df2listx,df2listy,color="blue")
plt.plot(df4listx,df4listy,color="red")
plt.show()