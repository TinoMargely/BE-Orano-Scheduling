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