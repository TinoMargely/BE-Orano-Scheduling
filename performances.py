import pandas as pd
import numpy as np

def perfs():
    data=pd.read_excel("data/raw/Orano-données_2.xlsx", sheet_name="Matrice perf",header=2,usecols=range(2,17), nrows=15)
    data=np.array(data)
    x=data[0]
    y=data[1:15]
    predictor=[]
    for i in range(14):
        predictor.append(np.poly1d(np.polyfit(x,y[i],4)))
    return(predictor)