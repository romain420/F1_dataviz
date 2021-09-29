#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
import plotly.graph_objects as go
import plotly.express as px


# ### Création des dataframes pour chaque fichier csv avec pandas

# In[2]:


#création de dataframe pour chaque fichier 'csv'
df_circuits = pd.read_csv('circuits.csv')
df_constructor_results = pd.read_csv('constructor_results.csv')
df_constructor_standings = pd.read_csv('constructor_standings.csv')
df_constructors = pd.read_csv('constructors.csv')
df_driver_standings = pd.read_csv('driver_standings.csv')
df_drivers = pd.read_csv('drivers.csv')
df_lap_times = pd.read_csv('lap_times.csv')
df_pit_stops = pd.read_csv('pit_stops.csv')
df_qualifying = pd.read_csv('qualifying.csv')
df_races = pd.read_csv('races.csv')
df_results = pd.read_csv('results.csv')
df_seasons = pd.read_csv('seasons.csv')
df_status = pd.read_csv('status.csv')


# ### Création d'une liste possedant tous les dataframes

# In[3]:


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

# In[43]:


for i in list_df : i.info()


# ## Description des dataframes un à un

# In[5]:


#dataframe sur les différents circuits
df_circuits.drop(columns=["url"],inplace=True)
df_circuits.head()


# In[6]:


#rename columns for easiest understanding
df_circuits.rename(columns = {'circuitRef':'Ref_circuit',
                             'location':'city',
                             'lat':'latitude',
                             'lng':'longitude',
                             'alt':'altitude'},
                    inplace = True)
# afficher les nouvelles entêtes
df_circuits.head()


# In[7]:


#un peu de data viz 
#tout d'abord trier les circuits du moins élevé au plus élevé
df_circuits = df_circuits.sort_values(by=['altitude'])
df_circuits = df_circuits.reset_index()
df_circuits.drop(columns=["index"],inplace=True)
#df_circuits.drop(columns=["level_0"],inplace=True)
df_circuits.head()


# In[8]:


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

# In[9]:


#nous allons d'abord recuperer uniquement la colonne qui donne le pays
pays = df_circuits['country']
print("Il y a ligne", len(pays), "à la base")
#dans un second temps nous allons retirer les doublons 
#pays = set(pays)
pays = pays.drop_duplicates().reset_index()#gerons les duplications de pays comme dans un dataframe
pays = pays['country']
print("A present on voit qu'il y a", len(pays), "pays different dans en F1")


# A présent nous allons créer une liste qui regroupe tous le continent

# In[10]:


continents = ['North_America', 'South_America', 'Africa', 'Asia', 'Oceania', 'Europe']


# Nous allons maintenant créer un dictionnaire des continents avec les pays qui s'y trouvent

# In[11]:


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


# In[12]:


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

# In[13]:


#fonctin en 1 ligne (lambda) permetant d'assigner les valeurs de la nouvelle colonnes 'continents en finction de 'pays' 
df_circuits['continents'] = df_circuits.apply(lambda row: continents_dic[row['country']], axis = 1)
df_circuits['colors'] = df_circuits.apply(lambda row: couleur_dic[row['continents']], axis = 1)#dans cette colonnes les couleurs sont stoké sous forme de code
df_circuits.head()#on peut visualiser dans le df ci-dessous la nouvelle colonne 'continents' qui concorde bien avec 'pays'


# ## Emplacement géographique des circuits

# Réalisation d'un script qui affichera l'empacement de chaque circuit sur la carte, ainsi qu'un symbole qui sera plus ou moins gros en fonction du nombre de course s'étant tenu sur celui-ci

# In[14]:


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

# In[15]:


df_constructors.head()


# In[16]:


nb_constru = df_constructors.shape[0]
print("Il y a eu ", nb_constru, "de constructeur en F1 entre 1950 et 2021")


# In[17]:


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

# In[18]:


#visualisation du dataframe de victoie de constructeur
df_constructor_results.head()


# A present nous allons merge les 2 tableau a fin d'avoir les resulats par constructeurs merge par rapport au 'constructeurId'

# In[19]:


#merge des dataframe 'df_constructors' avec 'df_constructors_results'
df_constructors = df_constructors.merge(df_constructor_results, how='inner', on='constructorId')
df_constructors.tail()


# Nous allons a present tenter de re-organiser le dataframe pour le rendre plus lisible

# In[20]:


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


# In[21]:


#drope des duplicate pour le dataframe 'df_constructors'
df_constructors = df_constructors.drop_duplicates()
df_constructors


# In[22]:


#visualisation de la forme du dataframe
df_constructors.shape
df_constructors.dtypes


# ### Calcule des points par équipe

# Cette partie va etes dedier au nombre de pooints inscrit par chaque ecurie au cours de l'histoire de la F1

# In[23]:


df_constructors.columns


# In[24]:


#utilisation de la fonction 'groupby' sur laquelle on applique la sum sur 
result_const = df_constructors.groupby('name').agg({'points':'sum'}).reset_index()
result_const


# In[25]:


#le but va etre de sorte les points dans l'ordre croissant
result_const = result_const.sort_values(by=['points'])
result_const = result_const.reset_index()
# result_const.drop(columns=["index"],inplace=True)
#result_const.drop(columns=["level_0"],inplace=True)
result_const[160:]


# Graphe des meilleurs constructeurs en fonction du nombre de points marqué dans leur histoire

# In[26]:


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

# In[27]:


#visualisation de la forme du dataframe 
df_results.head()


# In[28]:


#affichons la dataframe des drivers
df_drivers


# In[29]:


#recuperation des noms prenom et id du driver
name = ['driverId', 'forename', 'surname']
driver_name = df_drivers[name]
driver_name


# In[30]:


#réalisation d'un merge entre les dataframes drivers name et df_result
new_result = df_results.merge(driver_name, how='inner', on='driverId')  
new_result


# ### Realisation d'une fonction de recupeation de stat de cours pour tous les drivers ou 1 seul 

# Le but va aussi être de merge le dataframe ci-dessus avec un les circuits sur lequels ont lieu les course

# Dans un premier temps recuperons les informations qui nous interresse depuis les dataframe 'circuits', 'result', 'constructor', 'race'

# In[31]:


df_races.head()


# In[32]:


#creation de la nouvelle df de race
columns_race = ['raceId', 'circuitId', 'name', 'date']
race_info = df_races[columns_race]
race_info = race_info.rename(columns={"name": "GP_name",
                                      "date" : "GP_date"})
race_info.head()


# In[33]:


#creation de la nouvelle df de cicuit
columns_circuits = ['circuitId', 'name']
circuits_info = df_circuits[columns_circuits]
circuits_info = circuits_info.rename(columns={"name": "circuit_name"})
circuits_info.head()


# In[34]:


#creation de la nouvelle df de constructeur
columns_constructors = ['constructorId', 'name']
constructor_info = df_constructors[columns_constructors]
constructor_info = constructor_info.rename(columns={"name": "constructor_name"})
constructor_info.head()


# #### Les merges

# Le premier merge consistera a fusionner 'circuits_info' et 'race_info' par rapport au 'circuitId'

# In[35]:


#merge et changement de l'ordre des colonnes de 'race_info'
race_info = race_info.merge(circuits_info, how='inner', on='circuitId')
new_race_columns = ['raceId',
                    'GP_name',
                    'circuit_name',
                    'GP_date'] 
race_info = race_info[new_race_columns]
race_info


# Nous allons maintenant merge les df 'constructor_info', 'race_info' et 'df_result' concecutivement

# In[36]:


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


# In[37]:





# In[38]:


#pour plus de lisibilité nous allons a prèsent fusionner les colonnes 'forename' et 'surname' dans une seul colonne
new_result['full_name'] = new_result['forename'] + ' ' + new_result['surname']
new_result = new_result.drop_duplicates().reset_index()
new_result


# In[39]:


new_result['raceId'].max()


# ### Creation de la fonction de resultats par GP/drivers

# In[40]:


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

# In[45]:


new_result.columns


# In[47]:


#creation du dataframe 'df_dinamic_driv_cons' a partir de colonnes recupere dans 'new_result' 
graph_dinamic_driv_cons = ['driverId', 'constructorId', 'full_name', 'constructor_name', 'points', 'GP_date']
df_dinamic_driv_cons = new_result[graph_dinamic_driv_cons]
df_dinamic_driv_cons


# ### Création des nouvelles colonnes

# A présent nous allons créer les colonnes qui nous manque pour pouvoir créer les scatters

# In[ ]:


#ajout d'une colonne 'years' a partir de 'GP_date'

