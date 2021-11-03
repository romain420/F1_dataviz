# F1_dataviz
Projet de dataviz sur des données de F1 de 1950 à aujourd'hui (2021 derniére course premier GP d'Autriche)

## Les objectifs du projet 
Dans ce projet le but est de réaliser de la dataviz à l'aide de python et des library fournie par le langage.

## Les pré-requis

### D'ou vient le dataset

Actuellement le projet est un notebook qui prends son dataset sur un projet 'kaggle' sur la F1 dont le lien est fournis ci-dessous :
lien du dataset sur [kaggle](https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020).
  
Le dataset a été mis en ligne par 'Vopani' un utilisateur apparement regulier de la platforme aillant le grade de 'Grandmaster'.
Le projet est néant-moins mis assez régulièrement à jour par la communotée. Il est donc possible que des GP de la saison 2021 ai été rajouté ou même que 
des informations manquantes ou éroner soit mise à jour depuis le début du projet.

## User Guide

### L'environement de travail

Nous avons dans ce projet choisi de travailler avec l'environement '[anaconda](https://www.anaconda.com/products/individual)', qui propose une grande divercité de library des prè-installé.
Et donc une grande facilité d'utilisation. 

Mais vous n'etes pas obliger de d'avoir anaconda sur votre machine. Il est néanmoins obligatoir d'avoir pyhton d'installé. Pour savoir si pyhton est bien installé il vous suffit d'ouvrir un *cmd* sur Windows ou un *Terminal* sur linux et de rentrer la commande ```python``` ou ```python3```. Si un editeur *python* souvre vous pouvez quitter l'editeur grace à la commande ```quit()``` et passer à l'étape suivante. Si se n'est pas la cas il vous faudra installer [python3](https://www.python.org/downloads/) qui vous sera proposé directement sous Windows.  

Lorsque vous êtes assurés que *pyhton* est bien installé dans votre envrionnement de travail vous n'avez plus cas vous positionner dans le dossier du projet et entrer la commande : 

  - Sous Windows : 
    ```
    python main.py
    ```
  - Sous Linux : 
    ```
    python3 main.py
    ```
Vous devez attendre l'execution compléte du code jusqu'à ce que celui-ci affiche une partie de script indicant : 

```cmd
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'first_dash_test' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```
A partir de ce moment la vous pourrez ouvrir le navigateur de votre choix (chromium privilégié) et y rentrer l'[adresse](http://127.0.0.1:8050/) precisé dans le script ci-dessus ou alors *localhost:8050*. 

Il se peut que des petite erreur serveur ce produise lors du chargment du dashboard. Dans ce cas n'hésitez pas à recharger la page jusqu'à ce que les erreur disparaisse si elle ne le fait pas automatiquement. 

Si vous voulez vous pouvez vous pouvez installer els library manuellement bien que leur installation ce fait de manière automatique à l'execution de la commande précédente.
Les library a installé dans l'environement anaconda sont : 

  - 'folium' lien du git :
     ```
     conda install folium -c conda-forge
     ```
  - Pour installer le dashboard : 
    ```
    conda install -c conda-forge dash
    ```
  - Pour installer 'Plotly' : 
    ```
    conda install -c conda-forge plotly
    ```
  - Pour installer 'dash' :
    ```
    pip install dash
    ```
  - Pour installer 'opendataset' : 
    ```
    pip install opendatasets --upgrade
    ```

Les library indiqué ci-dessus sont à installer imperativement pour le bon fonctionnement du code. Il faut aussi installer l'environement ***anaconda*** (si ce n'est pas déjà fait) pour la gestion des package de base telque de **numpy** ou **pandas**. 

## Developper Guide

A l'intérieur de ce **repository**, vous trouverez tout les parties du code permettant de **néttoyer** les données, de **generer** des csv et pour finir le code permettant par la suite de **generer** le *Dashboard*.

### Nettoyage des données

Pour nettoyer les données, 2 solutions sont possible :
  - Utiliser le fichier ```F1_dataviz_last.py``` qui est un script python dans lequel les données sont triées et ensuite générere des fichier **csv** qui serviront à la création du dashboard. Il s'agit de la méthode la plus rapide pour rajouter des opérations dans le néttoayage des données.
  - La seconde solution consiste à utiliser le **notebook** jupyter (utilsable directement l'***anaconda_prompt***). Pour ça il vous faudra utiliser le fichier ```F1_dataviz.ipynb```, il s'agit d'un notebook qui vous permettra d'executer votre code patie par partie pour avoir le rendu de votre travail en  'temps réels' (la documantation de [jupyter_notebook](https://jupyter.org/documentation)). Avec cette methode vous serez obliger de générer un fichier ```.py```, il devrat donc replacer le fichier script ```F1_dataviz_last.py```.

### Génération du dashboard 

Pour generer le dashboard une seul solution s'offre à vous. Vous devez executer le fichier ```first_dash_test.py```.

Ce fichier est découper en 2 partie : 
  - La première qui sert à generer le squelette et le style de la page du **dashboard**.
  - La seconde est celle des **callbacks** qui sert à créer les graphs et gerer le lien entre les graphs et les actions de l'utilisateur.

### L'execution compléte du dashboard
Pour l'execution compléte du dashboard il vous faut lancer le fichier ```main.py``` dans une invete de commande comme stipuler dans le User Guide à l'aide de la commande : 
  - si vous êtes sur *Windows*
    ```
    python main.py
    ```
  - si vous êtes sur *Linux*  
    ```
    python3 main.py
    ```

## Rapport d'analyse 

Dans ce projet le but était de mettre en évidence des informations à propos de la *F1*. 

Dans un premier temps nous avons voulu montre les circuits les plus présent dans le monde de la F1. Nous nous sommes vite rendu compte grace à ces graphes, que la F1 est avant tout un sport très européen. La majoritée des Grand Prix et des circuits s'y trouvent. Et le nombre de course qui on eu lieu sur chaque circuit est globalement bien plus élevé en Europe que dans le reste du monde.

Dans un second temps nous avons voulu faire une comparaison sur les temps de pit-stop pour les plus grande écurie pour pouvoir les departager sur des critères qui ne sont pas uniquement basé sur des données recolter sur la piste mais aussi dans les stands. On c'est appercu d'une sorte d'homogénéité mais malgrés tout une différence c'est faite sur l'amplitude des résultats (soit le nombre de fois ou une écurie arrivé à faire ce temps).

Pour finir nous avons voulu mettre en place les des classement par saison. Il y en a 2 differents, l'un concerne les ***drivers*** présent dans le champinnat et donne leur classement Grand Prix après Grand Prix. Le second concerne le classement des ***Constructeurs*** au cours de la saison la aussi Grand Prix après Grand Prix.

## Conclusion

Le but de ce dashboard est de donnée un rapides appérçue de la F1 au personne qui ne connaisse pas ou très peu ce milieux mais aussi donner des compléments d'information à des personnes qui connaitrais mieux ce milieu

Ce projet a vocation à évolué grace à des idées de lecture des donnée suplémentaire ou des idées de personnes interressé. N'hésitez pas à poster des commentaire et idées constructive pour améliorer le dashboard déjà existant.
