#!/bin/python3

import os
import sys
import numpy as np
import pandas as pd
from sklearn import linear_model

def battery_life(t):
    df = pd.read_csv('trainingdata.txt', header=None)
    # df = df[df.iloc[:, 0] < 8]
    X = np.asarray(df.ix[:,0]).reshape(-1,1)
    Y = df.ix[:,1]
    
    lm = linear_model.LinearRegression()
    lm.fit(X,Y)
    pred = lm.predict(t)
    return pred[0]

if __name__ == '__main__':
    timeCharged = float(input())
    print(round(battery_life(timeCharged), 2))
