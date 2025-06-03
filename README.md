# *🎯 Objectif*
Construire un modèle de machine learning (Random Forest Regressor) pour prédire les frais médicaux en fonction de caractéristiques personnelles (âge, IMC, tabagisme, etc.), afin d’aider les compagnies d’assurance à mieux évaluer les risques et fixer les tarifs.

# *📊 Données*

* Source : Kaggle (harishkumardatalab/medical-insurance-price-prediction)
  
* Taille : 2 700 lignes, 7 colonnes
  
* Variables :
   * age : Âge
   * sex : Sexe
   * bmi : Indice de masse corporelle
   * children : Nombre d’enfants
   * smoker : Tabagisme (oui/non)
   * region : Région
   * charges : Frais médicaux (cible)
     
# *🧹 Prétraitement*

* Vérification des valeurs manquantes et aberrantes
  
* Visualisations : scatter plots, boxplots, camemberts
  
* Encodage :
    * smoker et sex → booléens
    * region → renommée en français (southwest → Nord, etc.)
    * Séparation des données en X (features) et y (target)







