# F1_dataviz
Projet de dataviz sur des données de F1 de 1950 à aujourd'hui (2021 dernière course premier GP d'Autriche)

## Les objectifs du projet 
Dans ce projet le but est de réaliser de la dataviz à l'aide de python et des librarys fournies par le langage.



## Les prérequis



### D'où vient le dataset



Actuellement le projet est un notebook qui prend son dataset sur un projet 'kaggle' sur la F1 dont le lien est fourni ci-dessous :

lien du dataset sur [kaggle](https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020).

  

Le dataset a été mis en ligne par 'Vopani' un utilisateur apparemment régulier de la plateforme ayant le grade de 'Grandmaster'.

Le projet est néanmoins mis assez régulièrement à jour par la communauté. Il est donc possible que des GP de la saison 2021 aient été rajoutés ou même que 

Des informations manquantes soit erronées soit mises à jour depuis le début du projet.

## User Guide

### L'environement de travail

Nous avons dans ce projet choisi de travailler avec l'environnement '[anaconda](https://www.anaconda.com/products/individual)', qui propose une grande diversité de library des prè-installé.

Et donc une grande facilité d'utilisation. 

Mais vous n'êtes pas obligé d'avoir anaconda sur votre machine. Il est néanmoins obligatoire d'avoir python d'installé. Pour savoir si python est bien installé il vous suffit d'ouvrir un *cmd* sur Windows ou un *Terminal* sur linux et de rentrer la commande ```python``` ou ```python3```. Si un éditeur *python* s'ouvre vous pouvez quitter l'éditeur grâce à la commande ```quit()``` et passer à l'étape suivante. Si ce n'est pas le cas il vous faudra installer [python3](https://www.python.org/downloads/) qui vous sera proposé directement sous Windows.  

Lorsque vous êtes assurés que *python* est bien installé dans votre environnement de travail vous n'avez plus cas vous positionner dans le dossier du projet et entrer la commande (pour certaines distributions de Linux tel que *Ubuntu 18*  vous pouvez utiliser la commande de Windows): 

  - Sous Windows : 
    ```
    python main.py
    ```
  - Sous Linux : 
    ```
    python3 main.py
    ```
Vous devez attendre l'exécution complète du code jusqu'à ce que celui-ci affiche une partie de script indiquant :  

```cmd
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'first_dash_test' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```
À partir de ce moment-là vous pourrez ouvrir le navigateur de votre choix (chromium privilégié) et y rentrer l'[adresse](http://127.0.0.1:8050/) précisé dans le script ci-dessus ou alors *localhost:8050*. 

Il se peut que des petites erreurs serveur se produisent lors du chargement du dashboard. Dans ce cas n'hésitez pas à recharger la page jusqu'à ce que les erreurs disparaissent si elle ne le fait pas automatiquement. 

Si vous voulez vous pouvez installer les librarys manuellement bien que leur installation se fasse de manière automatique à l'exécution de la commande précédente.

Les librarys a installé dans l'environement anaconda sont :  

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

Les librarys indiqués ci-dessus sont à installer impérativement pour le bon fonctionnement du code. Il faut aussi installer l'environnement ***anaconda*** (si ce n'est pas déjà fait) pour la gestion des packages de base telle que de **numpy** ou **pandas**. 

## Développer Guide

A l'intérieur de ce **repository**, vous trouverez toutes les parties du code permettant de **nettoyer** les données, de **générer** des csv et pour finir le code permettant par la suite de **generer** le *Dashboard*.

### Nettoyage des données

Pour nettoyer les données, 2 solutions sont possible :

  - Utiliser le fichier ```F1_dataviz_last.py``` qui est un script python dans lequel les données sont triées et ensuite générées des fichiers **csv** qui serviront à la création du dashboard. Il s'agit de la méthode la plus rapide pour rajouter des opérations dans le nettoyage des données.

  - La seconde solution consiste à utiliser le **notebook** jupyter (utilisable directement l'***anaconda_prompt***). Pour ça il vous faudra utiliser le fichier ```F1_dataviz.ipynb```, il s'agit d'un notebook qui vous permettra d'exécuter votre code partie par partie pour avoir le rendu de votre travail en  'temps réel (la documentation de [jupyter_notebook](https://jupyter.org/documentation)). Avec cette méthode vous serez obligé de générer un fichier ```.py```, il devra donc replacer le fichier script ```F1_dataviz_last.py```.

### Génération du dashboard 

Pour générer le dashboard une seule solution s'offre à vous. Vous devez exécuter le fichier ```first_dash_test.py```.

Ce fichier est découpé en 2 parties : 

  - La première qui sert à générer le squelette et le style de la page du **dashboard**.

  - La seconde est celle des **callbacks** qui sert à créer les graphes et gérer le lien entre les graphes et les actions de l'utilisateur.

### L'exécution complète du dashboard

Pour l'exécution complète du dashboard il vous faut lancer le fichier ```main.py``` dans une invite de commande comme stipuler dans le User Guide à l'aide de la commande : 
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

Dans un premier temps nous avons voulu montrer les circuits les plus présents dans le monde de la F1. Nous nous sommes vite rendu compte grâce à ces graphes, que la F1 est avant tout un sport très européen. La majorité des Grands Prix et des circuits s'y trouve. Et le nombre de course qui ont eux lieu sur chaque circuit est globalement bien plus élevé en Europe que dans le reste du monde.

Dans un second temps nous avons voulu faire une comparaison sur les temps de pit-stop pour les plus grandes écurie pour pouvoir les départager sur des critères qui ne sont pas uniquement basés sur des données récoltées sur la piste mais aussi dans les stands. On s'est aperçu d'une sorte d'homogénéité mais malgré tout une différence s'est faite sur l'amplitude des résultats (soit le nombre de fois ou une écurie arrivé à faire ce temps).

Pour finir nous avons voulu mettre en place les dés classement par saison. Il y en a 2 différents, l'un concerne les ***drivers*** présents dans le championnat et donne leur classement Grand Prix après Grand Prix. Le second concerne le classement des ***Constructeurs*** au cours de la saison là aussi Grand Prix après Grand Prix.

## Conclusion

Le but de ce dashboard est de données un rapide aperçu de la F1 aux personnes qui ne connaissent pas ou très peu ce milieu mais aussi donner des compléments d'informations à des personnes qui connaitrais mieux ce milieu

Ce projet a vocation à évoluer grâce à des idées de lecture des données supplémentaires ou des idées de personnes intéressées. N'hésitez pas à poster des commentaires et idées constructives pour améliorer le dashboard déjà existant.
