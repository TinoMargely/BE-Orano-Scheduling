from datetime import datetime, timedelta
import pandas as pd
import numpy as np

#Get Values - Récupère les valeurs du problème une fois la résolution terminée
def getValues(var,M, disp):
    
    Tasks=range(len(disp))  
  
    varsdict = {}
    for v in var:
        varsdict[v.name] = v.varValue

    dem=["dem_{}".format(i) for i in range(len(Tasks))]
    demVal=[varsdict[dem[i]] for i in range(len(dem))]
    deb=["deb_{}".format(i) for i in range(len(Tasks))]
    debVal=[varsdict[deb[i]] for i in range(len(dem))]
    liv=["liv_{}".format(i) for i in range(len(Tasks))]
    livVal=[varsdict[liv[i]] for i in range(len(dem))]
    marge=["marge_{}".format(i) for i in range(len(Tasks))]
    margeVal=[varsdict[marge[i]] for i in range(len(dem))]
    real=["real_{}".format(i) for i in range(len(Tasks))]
    realVal=[varsdict[real[i]] for i in range(len(dem))]
    y=[('y_('+str(i)+',_'+str(j)+')') for i in range(len(Tasks)) for j in range(M)]

    machine=[[] for m in range(M)]
    real2=[[] for m in range(M)]
    dem2=[[] for m in range(M)]
    deb2=[[] for m in range(M)]
    liv2=[[] for m in range(M)]

    for task in range(len(Tasks)):
        for m in range(M): 
            if(varsdict[('y_('+str(task)+',_'+str(m)+')')]==1):
                machine[m].append(task)
                real2[m].append(realVal[task])
                dem2[m].append(demVal[task])
                deb2[m].append(debVal[task])
                liv2[m].append(livVal[task])
                break
                
    return(demVal,debVal,livVal,realVal,real2,dem2,deb2,liv2,machine)

#Dataframe to List - Transforme en problème au format "jour"(12/02/2021 par ex) en format compréhensible par le modèle (t=1.3 <=> 1.3 jours après la première date)
SECONDS_PER_DAY = 24*60*60

def dataframe_to_list(data):
    dataframe = data.copy()
    min_date = dataframe['disp'].min().to_pydatetime()
    dataframe['disp'] = dataframe['disp'].apply(lambda x: (x.to_pydatetime()- min_date).total_seconds()/SECONDS_PER_DAY)
    dataframe['max'] = dataframe['max'].apply(lambda x: (x.to_pydatetime()-min_date).total_seconds()/SECONDS_PER_DAY)
    dataframe['durée'] = dataframe['durée']
    
    return(list(dataframe['disp']),list(dataframe['max']),list(dataframe['durée']))

#perfs- Récupère les données des performances de chaque machine pour des teneurs données, puis rend les courbes exploitables en y fittant une fonction polynomiale
def perfs():
    data=pd.read_excel("data/raw/Orano-données_2.xlsx", sheet_name="Matrice perf",header=2,usecols=range(2,17), nrows=15)
    data=np.array(data)
    x=data[0]
    y=data[1:15]
    predictor=[]
    for i in range(14):
        predictor.append(np.poly1d(np.polyfit(x,y[i],4)))
    return(predictor)


#risqueMarges - Renvoie un dictionnaire qui calcule le risque associé à chaque marge comprise entre 20 et 366 jours
#	      - alpha et beta : parametres de la loi gamma utilisée pour modéliser le risque
def risqueMarges(alpha,beta):
    marges = range(20,366)
    risque = [(1-stats.gamma.cdf(marges[i],a=alpha,scale=beta)) for i in range(len(marges))]
    return dict(zip(marges,risque))
