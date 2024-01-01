import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from mdule import nettoyage, getville, listeproduits
from itertools import combinations
from collections import Counter

#pour tout afficher
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


#recup des données

data = "../datasets/SalesAnalysis/Sales_Data/"


#fusion des différents fichiers
files = [fichier for fichier in os.listdir(data) if fichier.endswith('csv')]


df = pd.DataFrame()

for fichier in files:
    intermittent = pd.read_csv(data + fichier)
    df = pd.concat([df, intermittent])

df = nettoyage(df)



#TROUVER MEILLEUR MOIS + CA

df = df.set_index('Order Date')
df.sort_index(inplace = True)
df['Month'] = df.index.month_name()
df['CA'] = df['Price Each'] * df['Quantity Ordered']
caparmois = df.groupby('Month')['CA'].sum().sort_values(ascending = False)
print('Le meilleur mois est donc : ',caparmois.index[0] , 'avec un chiffre d affaire de ',caparmois.values[0], 'comme on peut le voir clairement ici : \n')
order = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]
caparmois.loc[order].plot.bar(figsize = (10,8))
plt.title("CA par mois")
plt.show()


#LA VILLE QUI A LE PLUS ACHETE
df['Ville'] = df['Purchase Address'].apply(getville)
ventesparville = df.groupby('Ville')['Quantity Ordered'].sum().sort_values(ascending=False)
print('\nLa ville qui a le plus commandé est : ' , ventesparville.index[0] + ' avec : ' , ventesparville.values[0] , ' produits!')
ventesparville.plot.barh(figsize = (10,8))
plt.title('Artcles vendus par ville')
plt.show()

#A QUELLE HEURE FAIRE DE LA PUB

df['Heure'] = df.index.hour
caparheure = df.groupby('Heure')['CA'].sum()
print("\nLe chiffre d'affaires le plus élevé est réalisé vers ", caparheure.sort_values(ascending = False).index[0] , 'h!')
plt.figure(figsize=(10,8))
sns.lineplot(data=pd.DataFrame(caparheure)['CA'])
plt.xticks(ticks=range(0, 24))
plt.show()



#PRODUITS SOUVENT ACHETES ENSEMBLES
 #on recup les commandes avec plus d'un article
commandesp = df[df['Order ID'].duplicated(keep=False)].copy()
produitsensembles = commandesp.groupby('Order ID')['Product'].apply(listeproduits)
count = Counter()

for achat in produitsensembles.to_list() :
    produits = achat.split(';')
    count.update(Counter(combinations(produits, 2)))

print('\nLes deux plus achetés ensemble sont donc ', count.most_common(1))


#PRODUIT LE PLUS VENDU
nombresventes = df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False)
print('Le produit le plus vendu est donc ', nombresventes.index[0], ' avec : ', nombresventes.values[0] , ' ventes!!'  )


#PRODUIT LE PLUS VENDU PAR HEURE
heureproduit = df.groupby(['Heure', 'Product'])['Quantity Ordered'].sum()
plusvendus = heureproduit.groupby('Heure').idxmax()
produits_plus_vendus = heureproduit.loc[plusvendus]
print('\n\n',produits_plus_vendus.to_string(header = False))






