import numpy as np
import pandas as pd
s1=pd.Series([1,2,3,4])
s2=pd.Series([1,2,3,4],index=['a','b','c','d'])

s2.reindex(index=range(15))
print(s2.index)
df1=pd.DataFrame([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(df1.head())

print(np.random.rand(25).reshape(5,5))

data={'name':['Sara', 'Ben'],

'Age':[23,34]}
df2=pd.DataFrame(data)
print(df2)

data1=[[1,2,3],[4,5,6]]
index1=["a","b"]
columns1=["c","d","e"]
df3=pd.DataFrame(data=data1,index=index1,columns=columns1)
print(df3.loc["a"])

df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],
                 'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],
                 'data2':range(3)})
print(df1)
print(df2)

#实现DataFrame的合并（默认情况下）
merge1=pd.merge(df1,df2)
print(merge1)

merge2=pd.merge(df1,df2,on='key')
