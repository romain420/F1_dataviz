#!/usr/bin/env python
# coding: utf-8

#import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
import plotly.graph_objects as go
import plotly.express as px
import opendatasets as od
import os
import dash
from dash import dcc
from dash import html


# ### Création des dataframes pour chaque fichier csv avec pandas

# In[2]:


#import des fichier s'ils n'existe pas
if os.path.exists('formula-1-world-championship-1950-2020'):
    print('le repertoir exist deja')
else:
    print("le repertoir n'exist pas")
    od.download("https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020")
    print('le repertoir exist a present')


# In[3]:


#création de dataframe pour chaque fichier 'csv'
df_circuits = pd.read_csv('formula-1-world-championship-1950-2020/circuits.csv')
df_constructor_results = pd.read_csv('formula-1-world-championship-1950-2020/constructor_results.csv')
df_constructor_standings = pd.read_csv('formula-1-world-championship-1950-2020/constructor_standings.csv')
df_constructors = pd.read_csv('formula-1-world-championship-1950-2020/constructors.csv')
df_driver_standings = pd.read_csv('formula-1-world-championship-1950-2020/driver_standings.csv')
df_drivers = pd.read_csv('formula-1-world-championship-1950-2020/drivers.csv')
df_lap_times = pd.read_csv('formula-1-world-championship-1950-2020/lap_times.csv')
df_pit_stops = pd.read_csv('formula-1-world-championship-1950-2020/pit_stops.csv')
df_qualifying = pd.read_csv('formula-1-world-championship-1950-2020/qualifying.csv')
df_races = pd.read_csv('formula-1-world-championship-1950-2020/races.csv')
df_results = pd.read_csv('formula-1-world-championship-1950-2020/results.csv')
df_seasons = pd.read_csv('formula-1-world-championship-1950-2020/seasons.csv')
df_status = pd.read_csv('formula-1-world-championship-1950-2020/status.csv')


# ### Création d'une liste possedant tous les dataframes

# In[4]:


list_df = [df_circuits,
          df_constructor_results,
          df_constructor_standings,
          df_constructors,
          df_driver_standings,
          df_drivers,
          df_lap_times,
          df_pit_stops,
          df_qualifying,
          df_races,
          df_results,
          df_seasons,
          df_status]


# ## Affichage des informations de chaque dataframes

# In[5]:


#for i in list_df : i.info()


# ## Description des dataframes un à un

# In[6]:


#dataframe sur les différents circuits
df_circuits.drop(columns=["url"],inplace=True)
df_circuits.head()


# In[7]:


#rename columns for easiest understanding
df_circuits.rename(columns = {'circuitRef':'Ref_circuit',
                             'location':'city',
                             'lat':'latitude',
                             'lng':'longitude',
                             'alt':'altitude'},
                    inplace = True)
# afficher les nouvelles entêtes
df_circuits.head()


# In[8]:


#un peu de data viz
#tout d'abord trier les circuits du moins élevé au plus élevé
df_circuits = df_circuits.sort_values(by=['altitude'])
df_circuits = df_circuits.reset_index()
df_circuits.drop(columns=["index"],inplace=True)
#df_circuits.drop(columns=["level_0"],inplace=True)
df_circuits.head()


# In[9]:


######graphe a modifier avec plus de detailles (rajouter une colonne continent, mettre diffrente couleur en fonction du continent, agradir le tableau pour avoir une absicse lisible)#####
#graphe de description
plt.scatter(df_circuits['name'],df_circuits['altitude'], alpha=0.5)  # alpha chances the transparency
#titre et legendes
plt.title('Formala 1 circuit altitude')
plt.xlabel('Circuit name')
plt.ylabel('Circuit altitude')
#affichage du graph
plt.show()


# A première vu le graph ci-dessus n'est pas très représentatif et compréhensible.
# Pour rendre ce graph plus attractif,  nous allons créer une colonne qui donne le continent dans lequel se trouve le circuit.

# In[10]:


#nous allons d'abord recuperer uniquement la colonne qui donne le pays
pays = df_circuits['country']
print("Il y a ligne", len(pays), "à la base")
#dans un second temps nous allons retirer les doublons
#pays = set(pays)
pays = pays.drop_duplicates().reset_index()#gerons les duplications de pays comme dans un dataframe
pays = pays['country']
print("A present on voit qu'il y a", len(pays), "pays different dans en F1")


# A présent nous allons créer une liste qui regroupe tous le continent

# In[11]:


continents = ['North_America', 'South_America', 'Africa', 'Asia', 'Oceania', 'Europe']


# Nous allons maintenant créer un dictionnaire des continents avec les pays qui s'y trouvent

# In[12]:


#dans cd dictionnaire la clé sera le pays et la value le continent pour des soucis pratiques
continents_dic = {
    'Azerbaijan' : 'Asia',
    'Korea' : 'Asia',
    'Russia' : 'Asia',
    'UAE' : 'Asia',
    'USA' : 'North_America',
    'Spain' : 'Europe',
    'China' : 'Asia',
    'Netherlands' : 'Europe',
    'Bahrain' : 'Asia',
    'Monaco' : 'Europe',
    'Argentina' : 'South_America',
    'Vietnam' : 'Asia',
    'Australia' : 'Oceania',
    'Canada' : 'North_America',
    'Saudi Arabia' : 'Asia',
    'South Africa' : 'Africa',
    'Singapore' : 'Asia',
    'Malaysia' : 'Asia',
    'Morocco' : 'Africa',
    'UK' : 'Europe',
    'Portugal' : 'Europe',
    'Belgium' : 'Europe',
    'Italy' : 'Europe',
    'Japan' : 'Asia',
    'Germany' : 'Europe',
    'France' : 'Europe',
    'Turkey' : 'Asia',
    'Sweden' : 'Europe',
    'India' : 'Asia',
    'Hungary' : 'Europe',
    'Switzerland' : 'Europe',
    'Austria' : 'Europe',
    'Brazil' : 'South_America',
    'Mexico' : 'North_America'
}
#representation des clee et value de 'continents_dic'
print("Les clee de 'continents_dic' sont :\n",continents_dic.keys())
print('')
print("Les values de 'continents_dic' sont :\n",continents_dic.values())


# In[13]:


#creation d'un dictionnaire qui attribue une couleur a un continent
couleur_dic = {
    'Asia' : '#F26230',
    'North_America' : '#223D96',
    'South_America' : '#653195',
    'Africa' : '#FEC810',
    'Oceania' : '#29AC46',
    'Europe' : '#eb242b'
}
#representation des clee et value de 'continents_dic'
print("Les clee de 'couleur_dic' sont :\n",couleur_dic.keys())
print('')
print("Les values de 'couleur_dic' sont :\n",couleur_dic.values())


# Il faut maintenant un introduire les valeurs de 'continents_dic' dans une nouvelle colonne de 'df_circuits'

# In[14]:


#fonctin en 1 ligne (lambda) permetant d'assigner les valeurs de la nouvelle colonnes 'continents en finction de 'pays'
df_circuits['continents'] = df_circuits.apply(lambda row: continents_dic[row['country']], axis = 1)
df_circuits['colors'] = df_circuits.apply(lambda row: couleur_dic[row['continents']], axis = 1)#dans cette colonnes les couleurs sont stoké sous forme de code
df_circuits.head()#on peut visualiser dans le df ci-dessous la nouvelle colonne 'continents' qui concorde bien avec 'pays'


# ## Emplacement géographique des circuits

# Réalisation d'un script qui affichera l'empacement de chaque circuit sur la carte, ainsi qu'un symbole qui sera plus ou moins gros en fonction du nombre de course s'étant tenu sur celui-ci

# In[15]:


#creation d'une liste des latitudes et une autre liste pour les longitude
latitudes = df_circuits['latitude']
longitudes = df_circuits['longitude']
couleurs = df_circuits['colors']

#initialisation de la map
coords = (43.4057, 39.9578)
map = folium.Map(location=coords, tiles='OpenStreetMap')

for i in range(len(latitudes)):
    folium.Circle(
        location = (latitudes[i], longitudes[i]),
        radius = 1,#nb_course[i]*2,#nombre de course aillant eu lieu sur circuit
        color = couleurs[i],
        fill = True,
#         fill_color = couleurs[i]
    ).add_to(map)

map


# Les point sont pratiquent lorsqu'on regarde la carte du monde dans ca globalité. Or lorsqu'on regarde à l'echelle d'un continent ou meme d'un pays les points sont trop petits.
# Il faudrait donc différencier les cas et garder cette carte, en rajoutant une carte par continent avec des marqueur plus visible.

# ## Nettoyage des du dataframe des constructeurs

# Dans ce dataframe le but va être de trié et de retirer le plus d'information possible du dataframe.

# In[16]:


df_constructors.head()


# In[17]:


nb_constru = df_constructors.shape[0]
print("Il y a eu ", nb_constru, "de constructeur en F1 entre 1950 et 2021")


# In[18]:


#nous allons a present verifier s'il y a des deplicate dans les constructeurs
nom_constru = df_constructors['name']
nom_constru = nom_constru.drop_duplicates()
taille_nom_constru = len(nom_constru)

#comparaison rapide pour savoir si il y a des duplicates ou non
if taille_nom_constru == nb_constru:
    print("Il n'y a pas de duplicates")
else:
    print("Il y avait biend des duplicates")


# On va commencé a regarder pour merge les dataframes des constructeurs avec celui de leur resultat

# In[19]:


#visualisation du dataframe de victoie de constructeur
df_constructor_results.head()


# A present nous allons merge les 2 tableau a fin d'avoir les resulats par constructeurs merge par rapport au 'constructeurId'

# In[20]:


#merge des dataframe 'df_constructors' avec 'df_constructors_results'
df_constructors = df_constructors.merge(df_constructor_results, how='inner', on='constructorId')
df_constructors.tail()


# Nous allons a present tenter de re-organiser le dataframe pour le rendre plus lisible

# In[21]:


new_columns = ['constructorId',
               'constructorResultsId',
               'constructorRef',
               'name',
               'nationality',
               'raceId',
               'points',
               'status',
               'url']
df_constructors = df_constructors[new_columns]
df_constructors.head()


# In[22]:


#drope des duplicate pour le dataframe 'df_constructors'
df_constructors = df_constructors.drop_duplicates()
df_constructors


# In[23]:


#visualisation de la forme du dataframe
df_constructors.shape
df_constructors.dtypes


# ### Calcule des points par équipe

# Cette partie va etes dedier au nombre de pooints inscrit par chaque ecurie au cours de l'histoire de la F1

# In[24]:


df_constructors.columns


# In[25]:


#utilisation de la fonction 'groupby' sur laquelle on applique la sum sur
result_const = df_constructors.groupby('name').agg({'points':'sum'}).reset_index()
result_const


# In[26]:


#le but va etre de sorte les points dans l'ordre croissant
result_const = result_const.sort_values(by=['points'])
result_const = result_const.reset_index()
# result_const.drop(columns=["index"],inplace=True)
#result_const.drop(columns=["level_0"],inplace=True)
result_const[160:]


# Graphe des meilleurs constructeurs en fonction du nombre de points marqué dans leur histoire

# In[27]:


######graphe a modifier avec plus de detailles (rajouter une colonne continent, mettre diffrente couleur en fonction du continent, agradir le tableau pour avoir une absicse lisible)#####
#graphe de description
plt.scatter(result_const['name'],result_const['points'], alpha=0.5)  # alpha chances the transparency
#titre et legendes
plt.title('Formala 1 Constructors poinnts')
plt.xlabel('Constructor name')
plt.ylabel('Constructor carriere points')
#affichage du graph
plt.show()


# ## Nous allons maintenant nous occuper de la partie 'result'

# In[28]:


#visualisation de la forme du dataframe
df_results.head()


# In[29]:


#affichons la dataframe des drivers
df_drivers


# In[30]:


#recuperation des noms prenom et id du driver
name = ['driverId', 'forename', 'surname']
driver_name = df_drivers[name]
driver_name


# In[31]:


#réalisation d'un merge entre les dataframes drivers name et df_result
new_result = df_results.merge(driver_name, how='inner', on='driverId')
new_result


# ### Realisation d'une fonction de recupeation de stat de cours pour tous les drivers ou 1 seul

# Le but va aussi être de merge le dataframe ci-dessus avec un les circuits sur lequels ont lieu les course

# Dans un premier temps recuperons les informations qui nous interresse depuis les dataframe 'circuits', 'result', 'constructor', 'race'

# In[32]:


df_races.head()


# In[33]:


#creation de la nouvelle df de race
columns_race = ['raceId', 'circuitId', 'name', 'date']
race_info = df_races[columns_race]
race_info = race_info.rename(columns={"name": "GP_name",
                                      "date" : "GP_date"})
race_info.head()


# In[34]:


#creation de la nouvelle df de cicuit
columns_circuits = ['circuitId', 'name']
circuits_info = df_circuits[columns_circuits]
circuits_info = circuits_info.rename(columns={"name": "circuit_name"})
circuits_info.head()


# In[35]:


#creation de la nouvelle df de constructeur
columns_constructors = ['constructorId', 'name']
constructor_info = df_constructors[columns_constructors]
constructor_info = constructor_info.rename(columns={"name": "constructor_name"})
constructor_info.head()


# #### Les merges

# Le premier merge consistera a fusionner 'circuits_info' et 'race_info' par rapport au 'circuitId'

# In[36]:


#merge et changement de l'ordre des colonnes de 'race_info'
race_info = race_info.merge(circuits_info, how='inner', on='circuitId')
new_race_columns = ['raceId',
                    'GP_name',
                    'circuit_name',
                    'GP_date']
race_info = race_info[new_race_columns]
race_info


# Nous allons maintenant merge les df 'constructor_info', 'race_info' et 'df_result' concecutivement

# In[37]:


#################################
#  ATTENTION LE TEMPS D'EXECUTION DE CETTE CELLULES ET RELATIVEMENT LONG
#  EN RAISON DU NOMBRE D'OPERATION REALISE
#################################
#merge avec 'circuit_info'
new_result = new_result.merge(constructor_info, how='inner', on='constructorId')
#merge avec 'race_info'
new_result = new_result.merge(race_info, how='inner', on='raceId')
#affichage du nouveau 'new_result' et remise en ordre des indexs
new_result.drop_duplicates().reset_index()


# In[38]:


new_result.columns


# In[39]:


#pour plus de lisibilité nous allons a prèsent fusionner les colonnes 'forename' et 'surname' dans une seul colonne
new_result['full_name'] = new_result['forename'] + ' ' + new_result['surname']
new_result = new_result.drop_duplicates().reset_index()
new_result


# In[40]:


new_result['raceId'].max()


# ### Creation de la fonction de resultats par GP/drivers

# In[41]:


#pour faciliter lutilisation de 'resulut_info' nous allons utiliser une fonction qui retourne le 'GP_name' ainsi que la 'GP_date'
#lorsqu'on lui place 'raceId' en argument
def gp_finder(race_id):
    """Cette fonction permet de rentrer l'id d'une course et d'avoir en retour
    le nom du grand prix ainsi que la date de celui-ci.
    Attention il est important que la 'race_id' soit contenu entre [1, 1060]

        arg : 'race_id' --> type 'int64'
        return : 'GP_name' & 'GP_date' type 'str'
    """
    gp_info_nd = new_result.loc[new_result['raceId'] == race_id, ['GP_name','GP_date']].drop_duplicates()
    #return gp_info_nd
    print("Il s'agit du '", gp_info_nd['GP_name'][0], "' qui a eu lieu le", gp_info_nd['GP_date'][0])

gp_finder(18)


# ### /!\ WARNING /!\ : Pour le moment la fonction ne fonctionne qu'avec un seul driver, corriger pour pourvoir mettre une liste de drivers

# In[42]:


#fonction retournant les information d'un GP en fonction de son ID ou de drivers en particulier si souhaite
def result_info(race_id, driver_name):
    """Cette fonction a ete creee pour pouvoir donner les resultat complet d'un GP si l'argument 'driver_name' et vide
    ou alors de donnée les resultat d'un GP pour un ou plusieurs driver

        arg : 'race_id' --> Id de du GP qui vous interressent type 'int64'
              'driver_mame' --> 'full_name' du ou des driver qui vous interresse type 'str' ou 'list'

        return : les info relative au GP : 'rank', 'grid', 'vitesse'...
    """
    #test de condition si l'argument 'driver_name' et vide ou non
    if driver_name == None:
        #recuperation de l'information de tous les drivers du GP (environ une 20 de ligne)
        gp_info_classement = new_result.loc[new_result['raceId'] == race_id, ['GP_name',
                                                                             'GP_date',
                                                                             'circuit_name',
                                                                             'full_name',
                                                                             'constructor_name',
                                                                             'grid',
                                                                             'points',
                                                                             'fastestLapTime',
                                                                             'fastestLapSpeed',
                                                                            ]]
        #retourne les info des drivers et les donne celon leur rank
        return gp_info_classement.sort_values(by=['grid'])
    #condition si le nom du drivers est reseigne
    else:
        #recuperation de l'information d'un seul driver pour le moment
        gp_info_driver = new_result.loc[(new_result['raceId'] == race_id) & (new_result['full_name'] == driver_name),
                                                                            ['GP_name',
                                                                             'GP_date',
                                                                             'circuit_name',
                                                                             'full_name',
                                                                             'constructor_name',
                                                                             'grid',
                                                                             'points',
                                                                             'fastestLapTime',
                                                                             'fastestLapSpeed',
                                                                            ]]
        #deniere condition logique qui permet de verifier si la combinaison demander est possible
        #(si le driver a bien participé a cette course)
        #dans un premier temps on test si requette rpecedentes est vide si c'est le cas on dis que le driver n'a
        #jamais participé a ce GP
        if gp_info_driver.empty == True:
            return print("Ce driver n'a jamais participer a cette course.")
        #dans l'autre cas on retourne les information du driver relative ce GP
        else:
            return gp_info_driver

#test de la fonction avec un GP et un driver
result_info(18, 'Maxime bourgain')


# ## Creation de fonction de scatter 'Driver' et 'Constructeurs'

# Dans cette partie le but et de sera de créer des graph pour aider à la visualisation des information des dataframes

# ### Constructions des dataframes des scatters

# Nous allons tout d'abord commencer par regrouper les informations qui nous interressent dans des dataframes pour les graphs qui suivrons

# In[43]:


new_result.columns


# In[44]:


#creation du dataframe 'df_dinamic_driv_cons' a partir de colonnes recupere dans 'new_result'
graph_dinamic_driv_cons = ['raceId','driverId', 'constructorId', 'full_name', 'constructor_name', 'points', 'position', 'GP_date']
df_dinamic_driv_cons = new_result[graph_dinamic_driv_cons]
df_dinamic_driv_cons = df_dinamic_driv_cons.drop_duplicates()
df_dinamic_driv_cons


# ### Création des nouvelles colonnes

# A présent nous allons créer les colonnes qui nous manque pour pouvoir créer les scatters

# In[45]:


#ajout d'une colonne 'years' a partir de 'GP_date'
def recup_years():
    df_dinamic_driv_cons['years'] = df_dinamic_driv_cons['GP_date'].str[:4].astype(int)
    return df_dinamic_driv_cons

recup_years()


# In[46]:


#verification des classement dans chaque GP
test = ['rank', 'grid', 'position', 'points', 'constructor_name', 'GP_name', 'circuit_name', 'GP_date', 'full_name']
new_result[test][:22].sort_values(by=['points'])


# In[47]:


#trie du df rapport a la date et au resultat de la course
df_dinamic_driv_cons = df_dinamic_driv_cons.sort_values(by=['GP_date', 'points'])
df_dinamic_driv_cons


# A présent l'objectif est de compter le nnombre de point ainsi que le nombre de victoire par driver

# Regrouper les informations dans des plus petite df (2 colonne) pour ensuite les transformaer en dictionnaire et les ajouter a 'df_dinamic_driv_cons'

# In[48]:


#utilisation de la fonction 'groupby' sur laquelle on applique la 'count' sur
driver_points = df_dinamic_driv_cons.groupby('full_name').agg({'points':'sum'}).reset_index()
driver_points.sort_values(by=['points'])#.loc[driver_points['full_name'] == 'Lewis Hamilton']#verification pour un driver souhaité


# In[49]:


#creation d'un dictionnaire a partir de ce df
#.set_index('state').to_dict()['name']
dico_point_driver = driver_points.set_index('full_name').to_dict()['points']


# In[50]:


#ajout de la nouvelle colonne qui repertories les points par driver
df_dinamic_driv_cons['points_drivers'] = df_dinamic_driv_cons.apply(lambda row: dico_point_driver[row['full_name']], axis = 1)
df_dinamic_driv_cons


# In[51]:


#mise a l'echelle logarithmique avec remise a 0 des valeur '< 0'
df_dinamic_driv_cons['points_drivers_log'] = np.log(df_dinamic_driv_cons['points_drivers'])
df_dinamic_driv_cons['points_drivers_log'].loc[df_dinamic_driv_cons['points_drivers_log'] < 0] = 0
df_dinamic_driv_cons


# ### Calcule du nombre de course couru et du nombre de victoire

# Nous allons dans un premier temps compter les nombre de course réalisé par un driver

# In[52]:


nb_race = df_dinamic_driv_cons.groupby('full_name').agg({'driverId':'count'}).reset_index()
nb_race = nb_race.sort_values(by=['driverId']).reset_index()
#rename columns
#rename columns for easiest understanding
nb_race.rename(columns = {'driverId':'number_race'}, inplace = True)
rename_nb_race = ['full_name', 'number_race']
nb_race = nb_race[rename_nb_race]
#'nb_race' nouvelle dataframe qui contient le nombre de course disputé par un driver au cours de ca cariere
nb_race


# In[53]:


#créationd d'une fonction de création de dictionnaire a partir de 2 colonnes d'un dataframe
def df_to_dico(dico_name, df, column_key, column_value):
    """fonction qui permet la création de dictionnaire a partir de colonnes de dataframe
            argument :
               - 'dico_name' type str, est le nom que vous donnez a votre dictionnaire
               - 'df' type dataframe, est le dataframe que vous voulez transformer en dictionnaire
               - 'column_key' type str, la colonne du dataframe qui servira de 'key'
               - 'column_value' type str, la colonne du dataframe qui servira de 'value'

            retour :
               - retourne un dictionnaire qui a pour keys et values les infos rentré en argument
    """
    dico_name = df.set_index(column_key).to_dict()[column_value]
    return dico_name

dico_nb_race = {}
dico_nb_race = df_to_dico(dico_nb_race, nb_race, 'full_name', 'number_race')


# In[54]:


#ajout de la nouvelle colonne qui repertories le nombre de course par driver
df_dinamic_driv_cons['nombre_race'] = df_dinamic_driv_cons.apply(lambda row: dico_nb_race[row['full_name']], axis = 1)
df_dinamic_driv_cons


# In[55]:


#ces 2 lignes permettent de remplacer '\N' par 0 car '\N' est une str particiliere
df_dinamic_driv_cons.position =  df_dinamic_driv_cons.position.replace(r'\s+|\\N', '0', regex=True)
df_dinamic_driv_cons.position =  df_dinamic_driv_cons.position.astype(int)


# Dans un second temps on va compter le nombre de victoire par driver

# In[56]:


#fonction permettant de compter le nombre de victoire de chaque driver dans l'histoire de la F1
def count_victory(df, column_interest, column_agg, function_apply, new_col_name):
    """fonction qui permet de compter le nombre de victoire de driver, constructeur...
            arguments :
                - 'df' type datframe : permet de renseigner la dataframe dans laquel vous voulez travailler
                - 'column_interest' type str : permet de renseigner la colonne par rapport a laquel vous souhaitez
                                               compter le nombre de victoire

            retour : 'df_group' type dataframe : retourne une dataframe qui a 1 colonne du nom et le nombre de victoire
                                                 en fonction de la prmiere colonne
    """
    df_group =  df[df.position==1][[column_interest, column_agg]]
    df_group = df_group.groupby(column_interest).agg({column_agg:function_apply}).reset_index()
    df_group.rename(columns = {column_agg:new_col_name}, inplace = True)
    rename_nb_win = [column_interest, new_col_name]
    df_group = df_group[rename_nb_win]

    return df_group

finish_1 = count_victory(df_dinamic_driv_cons, 'full_name', 'position', 'count', 'number_victory')
constructor_victory = count_victory(df_dinamic_driv_cons, 'constructor_name', 'position', 'count', 'number_constru_victory')
#constructor_victory#le nombre de victoire par écurie a lui l'aire coérent


# In[57]:


#df_dinamic_driv_cons.position.value_counts()


# In[58]:


#creation d'un dictionnaire a partir des 2 colonnes du dataframe genere precedement
dico_nb_win = {}
dico_nb_win = df_to_dico(dico_nb_win, finish_1, 'full_name', 'number_victory')

#creation d'un dictionnaire avec de value vide
driver_points = df_dinamic_driv_cons[:][['full_name', 'position']]
driver_points['position'] = 0
driver_points
dico_zero = {}
dico_zero = df_to_dico(dico_zero, driver_points, 'full_name', 'position')


# Merge des 2 dictionnaire créée si dessus

# In[59]:


dico_zero.update(dico_nb_win)
dico_nb_win = dico_zero


# In[60]:


#fonction permtant d'intergrer une colonne dans un datframe
def intergre_df_columns(df, dico, column_to_compute, column_computed):
    """Fonction permettant d'integrer des valeurs dans une nouvelle colonne en fonction des valeurs d'autre(s) colonne(s)
       a partir d'un dictionnaire créée précédement (vous pouvez utiliser la fonction 'df_to_dico(,,,)' pour créer des dico à
       partir de 2 colonnes de dataframe).

       argument :
           - 'df' type dataframe : dataframe dans lequel vous allez créer une nouvelle colonne
           - 'dico' type dictionnaire : dictionnaire qui posséde 'column_computed' en clée et 'column_to_compute' en value
                                        (vous pouvez utiliser la fonction 'df_to_dico(,,,)' pour créer des dico à partir
                                        de 2 colonnes de dataframe)
           - 'column_to_compute' type str : nom de la colonnes par rapport à laquelle vous voulez créer la nouvelle colonne
           - 'column_computed' type str : nom la colonne que vous voulez créer
       retour :
           - 'df' type dataframe : dataframe dans lequel vous ajouté une nouvelle colonne
    """

    df[column_computed] = df.apply(lambda row: dico[row[column_to_compute]], axis = 1)
    return df

df_dinamic_driv_cons = intergre_df_columns(df_dinamic_driv_cons, dico_nb_win, 'full_name', 'nombre_win')
df_dinamic_driv_cons


# In[61]:


#fonction permettant de compter le nobre de point inscrit dans l'histoir par un driver ou une ecurie
def count_points(df, column_interest):
    """Fonction permettant de compter le nombre de point inscrit en F1 par tous les drives/écuries

       arguments :
           -
       retour :
           -
    """
    #utilisation de la fonction 'groupby' sur laquelle on applique la 'count' sur
#     driver_points = df_dinamic_driv_cons.groupby('full_name').agg({'points':'sum'}).reset_index()
#     driver_points.sort_values(by=['points'])#.loc[driver_points['full_name'] == 'Lewis Hamilton']#verification pour un driver souhaité

    df_group = df.groupby(column_interest).agg({'points':'sum'}).reset_index()
    df_group.rename(columns = {'points':'number_points'}, inplace = True)
    rename_nb_win = [column_interest, 'number_points']
    df_group = df_group[rename_nb_win]

    return df_group.sort_values(by=['number_points']).reset_index()

constru_point = count_points(df_dinamic_driv_cons, 'constructor_name')
constru_point


# Dans cette cellules il y a un probleme avec le nombre de points accumulé par constructeurs. Ce problème est mis en évidence
# dans la cellule suivante. le probleme dans ce cas dois lier au donnée car on ne compte plus en fonction du constructeurs mais
# des points mis par un driver dans une écurie.
# Il doit donc y avoir des probleme de coérence entre les point mis mis par les
# drivers dans certaine écurie. Si le probleme n'est pas la il dois alors venir de duplication, ce qui est bizarre car le
# nombre de points par drivers est lui correcte.
# ***INFO A VERIFIER***

# On peut déjà constater que 'Lotus F1' et 'Team Lotus' sont différencier alors qu'elle rempresente la meme équipe

# In[62]:


test = pd.concat([constru_point, result_const], axis=1)
#test[160:]


# ### Technique de comptage dinamique

# Tentons une nouvelle technique qui nous permeterai de trouver un moyenne de compter le nombre de points/victoire de façon progressive au cours du temps.
# Pour les drivers comme pour les écuries.

# In[63]:


#premiere tentavive a partir du dataframe 'df_dinamic_driv_cons'
df_dinamic_driv_cons[24821:]


# Pour mettre en place cette technique il faut s'assurer que de dataframe est deja trier par date.
# Dans notre cas c'est déjà fait.

# In[64]:


#mise ne place de la technique
df_dinamic_driv_cons["cum_points"] = df_dinamic_driv_cons.groupby(['full_name'])['points'].cumsum(axis=0)
#df_dinamic_driv_cons


# La colonne a bien été créée à présent assurons nous que les résultats sont coérenh pour un driver

# In[65]:


#cellule de test pour calculer le nombre de point au cour du temps
# df_dinamic_driv_cons.loc[df_dinamic_driv_cons['full_name'] == 'Lewis Hamilton', ['points',
#                                                                               'cum_points',
#                                                                               'constructor_name',
#                                                                               'GP_date',
#                                                                               'full_name']]


# A partir de cette methode tentons de créer une fonction qui nous permettra de faire la meme chose.

# In[66]:


#fonction permettant de compter le nobre de point inscrit dans l'histoir par un driver ou une ecurie
def count_points(df, column_interest, new_col_name):
    """Fonction permettant de compter le nombre de point inscrit en F1 par tous les drives/écuries de façon dynamique au
       cours du temps
       arguments :
           -
       retour :
           -
    """
    df[new_col_name] = df.groupby([column_interest])['points'].cumsum(axis=0)
    return df


# In[67]:


#test de la fonction du dessus pour les constructeurs
count_points(df_dinamic_driv_cons, 'constructor_name', 'cum_constru_points')

#cellule de test pour calculer le nombre de point au cour du temps
# df_dinamic_driv_cons.loc[df_dinamic_driv_cons['constructor_name'] == 'Alpine F1 Team', ['points',
#                                                                               'cum_constru_points',
#                                                                               'constructor_name',
#                                                                               'GP_date',
#                                                                               'full_name']]


# Création d'une fonction permettant de compter le nombre de victoire par driver/constructeur.

# In[68]:


#cellule de test avant la création de la fonction
df_group = df_dinamic_driv_cons[df_dinamic_driv_cons.position==1]
df_dinamic_driv_cons['victory_driv_count'] = df_group.groupby(['full_name'])['position'].cumcount() + 1


# In[69]:


#fonction permettant de compter le nobre de point inscrit dans l'histoir par un driver ou une ecurie
def count_victory(df, column_interest, new_col_name):
    """Fonction permettant de compter le nombre de point inscrit en F1 par tous les drives/écuries de façon dynamique au
       cours du temps
       arguments :
           -
       retour :
           -
    """
    df_group = df[df.position==1]
    df[new_col_name] = df_group.groupby([column_interest])['position'].cumcount() + 1

    return df


# In[70]:


#comptage du nombre de victoire par constructeur
count_victory(df_dinamic_driv_cons, 'constructor_name', 'victory_constru_count')


# Dans les 2 colonnes remplacer les :
# - *'NaN'* par la dernière valeur prise par un driver ou une écurie
#
#
# Le faire dans la fonction *'count_points(,,)'* et *'count_victory(,,)'*

# In[71]:


#replacement de 'Nan' par '0'
# df_dinamic_driv_cons = df_dinamic_driv_cons.fillna(0)


# ### Creation des graphs dynamics

# Dans cette partie le but sera de créer 2 graphs différent :
#     - Graph drivers
#     - Graph constructeurs

# In[72]:


# px.scatter(df_dinamic_driv_cons, x="nombre_race", y="nombre_win", animation_frame="years",
#            animation_group="full_name", size="victory_driv_count", color="constructor_name",
#            hover_name="constructor_name",
#            log_x=True, size_max=55, range_x=[0,360], range_y=[0,105])


# ## Graph dynamique du nombre de course sur chaque circuit

# Il faut déduire les informations dont nous avons besoin pour réaliser ce graph.

# info a récupérer :
# - longitude
# - latitude
# - nom_circuit
# - nom_GP
# - nb_GP
# - meilleur_performance *(en option)*
# - url

# Visualisation des dataframe qui possendent les info suceptible de nous interressé

# In[73]:


df_circuits.head()


# In[74]:


df_results.head()


# In[75]:


df_races.head()


# Récuperation des champs qui nous interressent dans les dataframe si-dessus

# In[76]:


#recuperation des informations de 'df_circuits'
list_circuit = ['circuitId', 'name', 'country', 'latitude', 'longitude', 'continents']
new_circuit_df = df_circuits[list_circuit]

#recuperation des infos de 'df_result'
list_result = ['driverId', 'raceId', 'laps', 'time', 'fastestLapTime', 'fastestLapSpeed']
new_result_df = df_results[list_result]#creation de la nouvelle dataframe de résultat

#recuperation des infos de 'df_races'
list_races = ['raceId', 'year', 'name', 'circuitId', 'url']
new_race_df = df_races[list_races]#creation de la nouvelle dataframe des races
new_race_df = new_race_df.rename(columns = {'name' : 'GP_name'})


# ### Merge progressif des différents dataframe

# Dans cette partie la le but sera de merge progressivement chaque dataframe les uns avec les autres.

# In[77]:


#merge de dataframe race et circuits par rapport a l'id circuit
new_race_df = new_race_df.merge(new_circuit_df, how = 'inner', on = 'circuitId').sort_values(by=['year'])
new_race_df.head()


# In[78]:


#merge de dataframe race et result par rapport a l'id race
merge_race_result = new_race_df.merge(new_result_df, how = 'inner', on = 'raceId').sort_values(by=['year'])
merge_race_result.head()


# Ajout du non de driver en fonction de leur ID grace a la fonction **'intergre_df_columns'**

# In[79]:


#creation d'une colonne 'full_name' dans le dataframe de resultat
df_drivers["full_name"] = df_drivers["forename"] + " " + df_drivers["surname"]


# In[80]:


#création d'un dictionnaire des ID avec le full_name des drivers
list_dico_driver = ['driverId', 'full_name']
df_dico_nom_dri = df_drivers[list_dico_driver].drop_duplicates().reset_index()
dico_driver_name = df_to_dico('dico_driver_name', df_dico_nom_dri, 'driverId', 'full_name')
#df_drivers.loc[df_drivers.driverId == , ['driverId', 'forename', 'surname']]

intergre_df_columns(merge_race_result, dico_driver_name, 'driverId', 'full_name')
merge_race_result.head()


# Pour pouvoir travailler plus simplement avec le dataframe **'merge_race_result'** nous allons regarder le *type* de chaques colonnes

# In[81]:


merge_race_result.dtypes


# On voit que les colonnes ***'fastestLapTime'*** et ***'fastestLapSpeed'*** sont *'object'* alors qu'on attends du *int* ou du *float*. La raison pour laquel nous avons ce phénomène est à cause du **\N** que nous allons remplacer par **NaN**.

# In[82]:


#boucle 'for' pour les 2 colonnes qui sont de type 'object'
list_columns_to_change = ['time', 'fastestLapTime']
for i in list_columns_to_change:
    merge_race_result[i] = merge_race_result[i].replace(r'\s+|\\N', 'no_info', regex=True)

#changement de type pour la colonne 'fastestLapSpeed' passage en type 'float'
merge_race_result['fastestLapSpeed'] = merge_race_result['fastestLapSpeed'].replace(r'\s+|\\N', '0', regex=True)
merge_race_result['fastestLapSpeed'] = merge_race_result['fastestLapSpeed'].astype(float)


# Pour chaque circuit le but sera de récupérer la meilleur performance.
# Pour que lorsque l'on *click* sur un des points sur la carte on obtienne les informations suivantes:
# - ***'year'*** année du GP
# - ***'GP_name'*** nom du GP
# - ***'url'***
# - ***'name'*** non du circuit
# - ***'laps'***
# - ***'time'***
# - ***'fastestLapTime'***
# - ***'fastestLapSpeed'***
# - ***'full_name'***

# In[83]:


#recuperation des tours les plus rapides
fast_lap_gp = merge_race_result.groupby(['GP_name'])['fastestLapTime'].min()#création d'une serie contenant les meilleurs temps par GP
dico_fast_lap = fast_lap_gp.to_dict()#transformation de serie => dictionnaire

#integration de la colonnes 'GP_fastes_lap' dans le dataframe 'merge_race_result'
intergre_df_columns(merge_race_result, dico_fast_lap, 'GP_name', 'GP_fastes_lap')
merge_race_result.head()


# Le but sera de garder uniquement les ligne qui on la meme value dans les colonnes **'fastestLapTime'** et **'GP_fastes_lap'**

# In[84]:


filter_race_result = merge_race_result.query("fastestLapTime == GP_fastes_lap").reset_index()#filtre sur les
filter_fastest_info = filter_race_result.query("fastestLapTime != 'no_info'")
#filter_fastest_info#fastest lap on every GP that we have the info

#creation d'un dictionnaire sur grace a 2 colonne de 'filter_fastest_info'
dico_fastest_lap = {}
dico_fastest_lap = df_to_dico(dico_fastest_lap, filter_fastest_info, 'GP_fastes_lap', 'full_name')
dico_fastest_lap['no_info'] = 'no_info'
dico_fastest_lap


# Après avoir filtré les meilleur temps par GP, le but sera de récupérer les grands pris de facon unique, soit drop si une raceId est présente plusieur fois.

# In[85]:


merge_race_result = merge_race_result.drop_duplicates(subset=['raceId'])
merge_race_result = merge_race_result.drop(['fastestLapTime', 'full_name'], axis=1)#on retire les colonnes qui ne nous interessent plus

#integration de la nouvelle colonne a partir d'un dictionnaire
intergre_df_columns(merge_race_result, dico_fastest_lap, 'GP_fastes_lap', 'full_name')
# merge_race_result


# In[86]:


nombre_race = merge_race_result.groupby(['GP_name']).agg({'raceId':'count'}).reset_index()#contage du nombre de GP


# In[87]:


#contage progressif du nombre de GP et push dan une nouvelle colonne de notre df
merge_race_result['nombre_GP'] = merge_race_result.groupby(['GP_name'])['raceId'].cumcount() + 1


# In[88]:


#test sur un GP pour voire la coerance de notre travail
merge_race_result.loc[merge_race_result['GP_name'] == 'Azerbaijan Grand Prix', ['year', 'country', 'continents', 'GP_fastes_lap', 'nombre_GP']]


# La map dynamic des GP au cours du temps a travers le monde.

# In[89]:


#encore quelques bueugues a corriger :
#- garder le circuit meme si pas de course dans l'année (optionnel)
fig = px.scatter_geo(merge_race_result,
                     lon = 'longitude',
                     lat = 'latitude',
                     color = 'nombre_GP', color_continuous_scale = 'Plasma',
                     hover_name = 'name',
                     size = 'nombre_GP',
                     animation_frame = 'year',
                     projection="natural earth1")
fig.update_layout(
    title_text = 'Evolution du nombre de courses par GP de 1950 à 2021',
    geo = dict(
        scope = 'europe',
        landcolor = 'rgb(217, 217, 217)',
        )
    )
fig.show()


# Creation d'une seconde map non dynimique dans une focntion permettant de placer des argument et des filtres sur les continent/courses qui nous interressent.

# In[90]:


#map static qui doit etre transformé en fonction dans lequel on assignera le continent ou la course qui nous interressent
def show_map(scope):
    """Fonction de generation de map place des points aux coordonnées des circuits de F1
       argument :
           - scope type str : permet de rentrer le nom de la zone qui nous interresse (None autorise)
       retour :
           - affichage de la map centre sur la zone demande
    """
    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = merge_race_result['longitude'],
        lat = merge_race_result['latitude'],
        text = merge_race_result['name'] + '<br>Fastest lap : ' + merge_race_result['GP_fastes_lap'] + 'min' + '<br>By : ' + merge_race_result['full_name'],
        marker = dict(
            size = (merge_race_result['nombre_GP']**2)/20,
            opacity = 0.8,
            colorscale = 'Turbo',
            cmin = 1,
            color = merge_race_result['nombre_GP'],
            cmax = merge_race_result['nombre_GP'].max(),
            colorbar_title="Nombre de GP<br>1950-2021",
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
            )
        ))
    fig.update_layout(
        title_text = 'Emplacement et nombre de GP de chaque circuit<br>en' + scope,
        geo = dict(
            scope = scope,
            landcolor = 'rgb(217, 217, 217)',
            )
        )

    fig.show()


#utilisation de la fonction 'show_map()'
show_map('asia')#ligne 'color' a commenté décommenter pour récuperer les informations des couleurs


# ## Création du dashboard
# initialisation de l'application
app = dash.Dash(__name__)

# definition du type de l'application
app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls'),# partie de gauche reserve aux actions de l'utilisateur
                                  html.Div(className='eight columns div-for-charts bg-grey')#emplcaemnt de la premiere chartre premier graph
                                  ])
                                ])
#run de l'application affichage du dashboard dans une page de votre navigateur
if __name__ == '__main__':
    app.run_server(debug=True)
