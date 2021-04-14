from pulp import *
from os import dup, dup2, close
import time
import numpy as np

def solvePLNEMultiMachines(disp, dmax, duree,M,bigM,mu,a,predictors):    
    
    Tasks=range(len(disp)) #Liste des taches 
    Machine=range(M)
    
    model = LpProblem("Orano", LpMaximize)
    
    # Variables 
    y = LpVariable.dicts("y",((i,m) for i in Tasks for m in Machine),0,1,LpInteger) #y_{i}^m si i est usinée sur la machine m
    x = LpVariable.dicts("x", ((i,j,m) for i in Tasks for j in Tasks for m in Machine),0,1,LpInteger) #x_{i,j}^m=1 si i est usinée avant j
    deb = LpVariable.dicts("deb", Tasks,0, None)
    dem = LpVariable.dicts("dem", Tasks,0, None)
    real = LpVariable.dicts("real", Tasks,0, None)
    marge = LpVariable.dicts("marge", Tasks,0, None)
    z3 = LpVariable.dicts("z3", ((i,j,k,m) for i in Tasks for j in Tasks for k in Tasks for m in Machine),0,1,LpInteger)
    z2 = LpVariable.dicts("z2", ((i,j,m) for i in Tasks for j in Tasks for m in Machine),0,1,LpInteger)
    liv = LpVariable.dicts("liv", Tasks,0, None)
    W = LpVariable("W", lowBound=0)
    
    # Contraintes :
    for j in Tasks:
        
        for m in Machine:
            model += x[j,j,m] == 0 
            
        model += lpSum(y[j,m] for m in Machine)==1
        model += dem[j] >= disp[j]
        model += real[j] == dem[j] + duree[j] 
        model += W <= marge[j]
        model += liv[j] == deb[j] + 30
        model += liv[j] <= dmax[j]
        model += marge[j] == dmax[j] - liv[j]
        model += deb[j] >= real[j]
       
        
        for i in Tasks:
            if i != j:
                for m in Machine: 
                    model += dem[j]>= real[i]-bigM*(1-x[i,j,m])
                    model += z2[j,i,m] <= y[i,m]
                    model += z2[j,i,m] <= y[j,m]
                    model += z2[j,i,m] >= (y[i,m]+y[j,m])-1
                    model += z2[j,i,m] >= 0
            if i<j:
                for m in Machine:
                    model += x[i,j,m]+x[j,i,m]==z2[i,j,m]

            for k in Tasks:
                if i!=j and i!=k and j!=k:
                    for m in Machine : 
                        model += z3[i,j,k,m]<=z2[i,j,m]
                        model += z3[i,j,k,m]<=z2[i,k,m]
                        model += z3[i,j,k,m]>=(z2[i,j,m]+z2[j,k,m])-1
                        model += z3[i,j,k,m]>=0
                
    # Objectif : 
    #model+= W +0.5*lpSum(mu[i]*a[m]*y[i,m] for i in Tasks for m in Machine)
    model += W*10**6+lpSum(y[i,m]*predictors[m](mu[i])*duree[i] for m in Machine for i in Tasks)*100/365
    #model+=lpSum(y[i,m]*predictors[m](mu[i])*duree[i] for m in Machine for i in Tasks)*100/365
    
    # Ouverture du fichier contenant les logs
    f = open('capture.txt', 'w')
    orig_std_out = dup(1)
    dup2(f.fileno(), 1)
    
    #Resolution du PLNE : 
    starttime=time.time() #Pour avoir le temps d'execution
    model.solve(PULP_CBC_CMD(maxSeconds=60, msg = 1))
    solveTime=time.time()-starttime
    
    # Ecriture des logs dans un fichier
    dup2(orig_std_out, 1)
    close(orig_std_out)
    f.close()
    
    #Affichage des éléments de résolution
    f_val=[]
    for i in range(0,len(Tasks)):
        f_val.append(model.variables()[i].varValue)
    order=np.argsort(f_val)
    
    print("Temps de résolution = ", solveTime)
    print("Statut de la solution = ", LpStatus[model.status])
    print("Valeur optimale = ", value(model.objective))
    return(solveTime,value(model.objective),model.variables())
