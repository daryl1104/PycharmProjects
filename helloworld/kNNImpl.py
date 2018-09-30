from unittest.mock import inplace

import numpy as np
import pandas as pd
import collections as cl
import random
from matplotlib import pyplot

def k_nearest_neighbors(data,predict,k):
    distances=[]
    for group in data:
        for features in data[group]:
            pass
            #欧式距离
            eulr_distance=np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([eulr_distance,group])

    #print(distances)
    sorted_distances=[i[1] for i in sorted(distances)]
    #print(sorted_distances)
    top_neareatn=sorted_distances[:k]
    #print(top_neareatn)
    group_res=cl.Counter(top_neareatn).most_common(1)[0][0]
    #print(group_res)
    return group_res

if __name__=='__main__':
    """dataset = {'black':[ [1,2], [2,3], [3,1] ], 'red':[ [6,5], [7,7], [8,6] ]}
    new_features = [3.5,5.2]  # 判断这个样本属于哪个组
    which_group=k_nearest_neighbors(dataset,new_features,2)"""
    dataset=pd.read_csv("F:\\breast-cancer-wisconsin.data.txt")
    print(dataset.shape)
    #print(dataset.head())
    dataset.replace('?',np.nan,inplace=True)
    dataset.dropna(inplace=True)
    print(dataset.shape)

    full_data=dataset.astype(float).values.tolist()
    random.shuffle(full_data)
    test_size=0.2
    train_data=full_data[:-int(test_size*len(full_data))]
    test_data=full_data[-int(test_size*len(full_data)):]

    train_set={2:[],4:[]}
    test_set={2:[],4:[]}
    for i in train_data:
        train_set[i[-1]].append(i[:-1])
    for i in test_data:
        test_set[i[-1]].append(i[:-1])

    correct=0
    total=0
    for i in test_set:
        for group in test_set[i]:
            res=k_nearest_neighbors(train_set,group,5)
            if res==i:
                correct+=1
            total+=1


    print(correct/total)
