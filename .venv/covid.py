import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 600)
pd.set_option('display.max_columns', 10)



df=pd.read_excel('../datasets/COVID-19-geographic-disbtribution-worldwide-2020-12-14.xlsx')
df.dropna(inplace=True)


#pays avec le plus de cas
payscas = df.groupby('countriesAndTerritories')['cases'].sum()

print('Le pays avec le plus de cas est : ' , payscas.sort_values(ascending=False).index[0] , ', avec : ' , payscas.sort_values(ascending=False).values[0] , ' cas ')
plt.figure(figsize=(30,20))
payscas.plot(kind='bar', color='salmon')
plt.title('Nombre de cas par pays')
plt.xlabel('Pays')
plt.ylabel('Cas')
plt.show()



#pays avec le plus grand taux de mortalité
df['tauxmortalite'] = df['deaths']/df['cases']
df['tauxmortalite'] = df['tauxmortalite'].replace([float('inf'), float('-inf')], float('nan'))
tauxmort = df.groupby(['countriesAndTerritories'])['tauxmortalite'].mean()
pays_max_mortalite = tauxmort.idxmax()
taux_max_mortalite = tauxmort.max()
print('Le taux de mortalité le plus élevé est retrouvé chez', pays_max_mortalite, 'avec un taux de mortalité de :', taux_max_mortalite)
plt.figure(figsize=(30,20))
sns.barplot(x=tauxmort.index, y=tauxmort.values, color='red')
plt.title('Taux de mortalité par pays')
plt.xlabel('Pays')
plt.ylabel('Taux mortalite')
plt.xticks(rotation=90)
plt.show()


#pays avec le plus de morts
paysmorts = df.groupby('countriesAndTerritories')['deaths'].sum()
print('Le pays avec le plus de morts est : ' , paysmorts.sort_values(ascending=False).index[0] , ', avec : ' , paysmorts.sort_values(ascending=False).values[0] , ' morts ')
plt.figure(figsize=(30,20))
paysmorts.plot(kind='bar', color='purple')
plt.title('Nombre de morts par pays')
plt.xlabel('Pays')
plt.ylabel('Morts')
plt.show()



#comparaison cas décés
casparmois = df.groupby('month')[['cases', 'deaths']].sum()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30, 15))

sns.lineplot(x=casparmois.index, y=casparmois['cases'], color='green', ax=ax1)
ax1.set_title('Evolution des cas')
ax1.set_xlabel('Months')
ax1.set_ylabel('Cas')


sns.lineplot(x=casparmois.index, y=casparmois['deaths'], color='red', ax=ax2)
ax2.set_title('Evolution des morts')
ax2.set_xlabel('Months')
ax2.set_ylabel('Décès')
plt.show()




#comparaison plusieurs pays
allemagne = df[df.countriesAndTerritories == 'Germany']
allemagnemois = allemagne.groupby('month')[['cases','deaths']].sum()



uk = df[df.countriesAndTerritories == 'United_Kingdom']
ukmois = uk.groupby('month')[['cases','deaths']].sum()



france = df[df.countriesAndTerritories == 'France']
francemois = france.groupby('month')[['cases','deaths']].sum()



italie = df[df.countriesAndTerritories == 'Italy']
italiemois = italie.groupby('month')[['cases','deaths']].sum()

fig, axes = plt.subplots(2, 2, figsize=(30, 30))


sns.lineplot(x=allemagnemois.index, y=allemagnemois['cases'], color='black', ax=axes[0, 0])
axes[0, 0].set_title('Evolution des cas en Allemagne')
axes[0, 0].set_xlabel('Months')
axes[0, 0].set_ylabel('Cas')


sns.lineplot(x=ukmois.index, y=ukmois['cases'], color='red', ax=axes[0, 1])
axes[0, 1].set_title('Evolution des cas en Angleterre')
axes[0, 1].set_xlabel('Months')
axes[0, 1].set_ylabel('Cas')

sns.lineplot(x=francemois.index, y=francemois['cases'], color='blue', ax=axes[1, 0])
axes[1, 0].set_title('Evolution des cas en France')
axes[1, 0].set_xlabel('Months')
axes[1, 0].set_ylabel('Cas')

sns.lineplot(x=italiemois.index, y=italiemois['cases'], color='green', ax=axes[1, 1])
axes[1, 1].set_title('Evolution des cas en Italie')
axes[1, 1].set_xlabel('Months')
axes[1, 1].set_ylabel('Cas')

plt.tight_layout()
plt.show()




#comparaison des par continent
continents = df.groupby('continentExp')[['cases', 'deaths']].sum()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30, 15))
sns.barplot(x=continents.index, y=continents['cases'], color='red', ax = ax1)
ax1.set_title('Nombre de cas')
ax1.set_xlabel('Months')
ax1.set_ylabel('Cas')


sns.barplot(x=continents.index, y=continents['deaths'], color='black', ax=ax2)
ax2.set_title('Nombre de morts')
ax2.set_xlabel('Months')
ax2.set_ylabel('Décès')
plt.show()


