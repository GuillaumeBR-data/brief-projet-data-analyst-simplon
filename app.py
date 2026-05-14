import plotly.express as px
import pandas as pd

#1) Chargement des données
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

#2) # Regroupement des ventes par produit
ventes_produit = données.groupby('produit', as_index=False)['qte'].sum()

# Vérification des  ventes par produit
print(ventes_produit)

#3) Création du premier graphique
figure = px.bar(ventes_produit, y='qte', x='produit', title='Quantité vendue par produit', color='produit',color_discrete_map={'Produit A': 'orange','Produit B': 'blue','Produit C' : 'green'},width=500,height=350)

# Ajustement des titres
figure.update_xaxes(title='Produits')
figure.update_yaxes(title='Quantité')
figure.update_layout(title='Les ventes par produit')

figure.write_html("ventes-par-produit.html")
print("ventes-par-produit.html généré avec succès !")

#4) Calcul du chiffre d'affaire 
données['chiffre_affaire'] = données['qte'] * données['prix']

# Regroupement du chiffre d'affaires par produit
chiffre_daffaire_produit = données.groupby('produit',as_index=False)['chiffre_affaire'].sum()

# Vérification du chiffre d'affaires par produit
print(chiffre_daffaire_produit)

#5) Création du second graphique
figure = px.bar(chiffre_daffaire_produit, y='chiffre_affaire', x='produit', title="Chiffre d'affaire par produit", color='produit',color_discrete_map={'Produit A': 'orange','Produit B': 'blue','Produit C' : 'green'},width=500,height=350)

# Ajustement des titres
figure.update_xaxes(title='Produits')
figure.update_yaxes(title="Chiffre d'affaires")
figure.update_layout(title="Le chiffre d'affaires par produit")

figure.write_html("chiffre-d'affaires-par-produit.html")
print("Chiffre-d'affaires-par-produit.html généré avec succès !")