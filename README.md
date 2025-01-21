# BE-Orano-Scheduling

**Pitch :** le but de ce projet est d’optimiser l’ordonnancement d’un module de production. 

**Langage :** python.

**Pré-requis** : il est nécessaire d’installer le package puLP de python au préalable. 

**Architecture :** afin d’avoir un code lisible et facilement compréhensible nous l’avons réparti en différents fichiers .py 

-Le fichier **Solve_PLNE.py** contient l’implémentation du PLNE. La fonction qu’il contient permet la résolution du problème.

-Le fichier **Graphics.py** contient l’implémentation des fonctions d’affichage, permettant le traitement visuel des résultats obtenu. Les fonctions qu’il contient permettent d’afficher l’emploi du temps, l’histogramme des marges ou encore les graphes de rendements. 

-Le fichier **utils.py** contient l’intégralité des fonctions annexes, que l’on pourrait qualifier d’utilitaires.

**Execution :** le fichier **main.ipynb** est un notebook executable qui permettra de résoudre le problème et d’effectuer diverses opérations de visualisation du résultat obtenu.