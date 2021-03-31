from matplotlib import pyplot as plt
import numpy as np

def showRendements(machine,mu,predictors):
    x=np.linspace(0.02,0.05,200)
    print("RENDEMENTS :")
    for m in range(len(machine)):
        plt.figure(figsize=(12,8))
        plt.plot(x,predictors[m](x))
        for i in machine[m]:
            plt.plot(mu[i],predictors[m](mu[i]), 'ro')
            plt.annotate(str(i),(mu[i],predictors[m](mu[i])+10),color="red",weight='bold',fontsize=10,ha='center',va='center')
        plt.title("Machine "+str(m))
        plt.show()