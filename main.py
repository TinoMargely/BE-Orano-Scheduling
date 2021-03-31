#Importation des fonctions : 
from Solve_PLNE import solvePLNEMultiMachines
from utils import *
from graphics import *

# Lecture des donnees du fichier Orano-données-Double.xlsx :
data = pd.read_excel("data/raw/Orano-données-Double.xlsx", sheet_name="Optim", header=5, usecols=[3,4,5,6,7], nrows=47)

# Calculs des performances de chaque machines pour chaque valeur de taux d'uranium : 
predictors=perfs()

# convertion des données et récupération des n premieres commandes : 
n = 15
disp, dmax, duree = dataframe_to_list(data)
disp, dmax, duree = disp[:n], dmax[:n], duree[:n]

# Résolution du PLNE avec des valeurs aléatoires de mu : 
a=[12,-8]
np.random.seed(15)
mu=np.random.uniform(0.02,0.049,15)
[t,price,var]= solvePLNEMultiMachines(disp, dmax, duree,2,10**6,mu,a,predictors)

## Affichage : 

# récupération des variables du plne :
demVal,debVal,livVal,realVal,real2,dem2,deb2,liv2,machine=getValues(var,2, disp)

# Graphique représentant les emplois du temps des machines : 
showEDT(machine,deb2,dem2,real2,liv2)

# Histogramme représentant la marge de chaque commande sur la machine où elle est effectuée :
showMarge(machine,livVal,dmax,2)

#Graphique représentant le rendement de la machine en fonction de la teneur en uranium désirée.
# Chaque point rouge représente une commande : 
showRendements(machine,mu,predictors)

