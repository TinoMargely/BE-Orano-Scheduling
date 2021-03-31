from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
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