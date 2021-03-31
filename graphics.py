from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

def showEDT(machine,deb2,dem2,real2,liv2):
    print('PLANIFICATION :')     
    for m in range(len(machine)):
        
        deb=dict(zip(machine[m],deb2[m]))
        dem=dict(zip(machine[m],dem2[m]))
        real=dict(zip(machine[m],real2[m]))
        liv=dict(zip(machine[m],liv2[m]))
        order=sorted(deb,key=deb.get)
        plt.clf()
        fig, axs = plt.subplots(figsize=(12, 1), tight_layout=True)
        
        colors = list(mcolors.CSS4_COLORS.keys())
        colors_to_exclude = ['light', 'white', 'snow', 'slate', 'gray', 'beige', 'blanchedalmond', 'aliceblue', 'azure',
                         'bisque', 'aqua', 'cornsilk']
        for col in colors_to_exclude:
            colors = [c for c in colors if col not in c]
            
        used_colors = dict()
        for i in range(len(machine[m])):
            for col in colors:
                if col not in used_colors.values():
                    used_colors[i] = col
                    break
        j=0
        
        for i in machine[m]:
            x=dem[order[j]]
            axs.add_patch(patches.Rectangle((x, 0), real[order[j]], 1, facecolor=colors[j],edgecolor='white',linewidth=2.0))
            axs.annotate(order[j],(x+(real[order[j]]-dem[order[j]])/2,0.5),color='w', weight='bold',fontsize=10, ha='center', va='center')
            j+=1
            
        plt.xticks(liv2[m])
        plt.yticks([])
        plt.title('Machine ' + str(m))
        plt.show()


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
