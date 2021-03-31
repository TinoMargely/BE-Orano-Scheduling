from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

def showMarge(machine,livVal,dmax,M):
    print("MARGES : ")
    marges=np.array(dmax)-np.array(livVal)
    marges2=[[] for m in range(M)]
    for m in range(M):
        for i in machine[m]:
            marges2[m].append(marges[i])
        plt.subplots(figsize=(12, 8))
        sns.barplot(machine[m],marges2[m])
        plt.title("Marges sur la machine {}".format(m))
        plt.xlabel("Tache")
        plt.ylabel("Marges")