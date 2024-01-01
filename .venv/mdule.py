import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


def nettoyage(df) :

    #suppression des nuls
    df.dropna(inplace=True)
    # top orderid = orderid et orderdate = orderdate (erreur dans les données) à corriger
    df = df.drop(df.loc[df['Order Date'] == "Order Date", :].index)
    # attribution des types corrects
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
    df['Price Each'] = pd.to_numeric(df['Price Each'])
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

def getville(addresse) :
    #fonction qui récupere le nom de la ville depuis une adresse
    return addresse.split(',')[1].strip()


def listeproduits(commande : list) :
    return ';'.join(commande)