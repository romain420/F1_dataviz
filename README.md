# F1_dataviz
Projet de dataviz sur des données de F1 de 1950 à aujourd'hui (2021 derniére course premier GP d'Autriche)

## Les objectifs du projet 
Dans ce projet le but est de réaliser de la dataviz à l'aide de python et des library fournie par le langage.

## Les pré-requis

### D'ou vient le dataset

Actuellement le projet est un notebook qui prends son dataset sur un projet 'kaggle' sur la F1 dont le lien est fournis ci-dessous :
lien du dataset sur kaggle :

  - https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020
  
Le dataset a été mis en ligne par 'Vopani' un utilisateur apparement regulier de la platforme aillant le grade de 'Grandmaster'.
Le projet est néant-moins mis assez régulièrement à jour par la communotée. Il est donc possible que des GP de la saison 2021 ai été rajouté ou même que 
des informations manquantes ou éroner soit mise à jour depuis le début du projet.

### L'environement de travail

Nous avons dans ce projet choisi de travailler avec l'environement 'anaconda' (lien de l'instalation : https://www.anaconda.com/products/individual), qui propose une grande divercité de library des prè-installé.
Et donc une grande facilité d'utilisation. Néant-moins quelque library sont à installer sur votre environement si vous voulez complètement utilisé les 
capacité de notre projet.
Les library a installé dans l'environement anaconda sont : 

  - 'folium' lien du git : https://python-visualization.github.io/folium/installing.html
  - Pour installer le dashboard : ```conda install -c conda-forge dash```
  - Pour installer 'Plotly' : ```conda install -c conda-forge plotly```
  - Pour installer 'jupyter-dash' si vous preferez travailler sur notre notebook : ```conda install -c conda-forge jupyter-dash```

  
## Le travail réalisé

### Intro

Comme nous l'avons dis précedement, dans ce projet nous avons travaillé à l'aide d'un dataset dans lequel les données étaient stoqué dans 13 fichiers 'csv' différents.

### Les circuits

Nous avons dans un premier temps cherché à analizé le dataframe sur les circuits. Pour chercher à voir l'atitude des différents circuits. Dans un second temps le nous
avons cherché à les afficher sur une carte à partir de leur coordonnées géographique.
On a donc décidé ensuite de leur attribuer une couleur en fonction du continent sur lequel il se trouve, pour une facilitée de compréhension et d'aquisition de l'informations.

### Les constructeurs

Dans cette partie, l'objectif était de nettoyer les données des constructeurs de F1, à fin de pouvoir les classer en fonction du nombre de point inscrit par chacuns d'entre eux.
on a la aussi cherché a les affiché sous forme de graphe.

### Les résultats 

Dans le dataset mis à notre disposition, il y avait un dataframe qui regroupait toute les courses par driver ainsi que toute les information relative a celle-ci. Le premier
problèmes auquels nous avons été confrouté était le manque d'information compréhenssible, tout était stoqué sous forme d' 'id' ('constructeurid', 'driverid'...). 
Il nous à donc fallu merge les dataframes en fonction des id pour récuperé les noms de driver et constructeur en tout lettres pour facilité la conpréhention et la prise
d'information dans notre dataframe.
