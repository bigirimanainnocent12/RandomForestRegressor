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
      
# *🧠 Modélisation*      
      
* Pipeline avec :
  * StandardScaler pour les variables numériques
  * OneHotEncoder pour les variables catégorielles
  * RandomForestRegressor comme modèle
* Optimisation des hyperparamètres avec GridSearchCV :
  * n_estimators, max_depth, min_samples_split, min_samples_leaf

# *📈 Évaluation*

* Meilleurs paramètres affichés
* Métriques :
    * RMSE (Root Mean Squared Error)
    * R² (coefficient de détermination)
    * MAPE (Mean Absolute Percentage Error)
* Visualisation des résidus avec Yellowbrick

# *💾 Sauvegarde & Prédiction*

* Le modèle est sauvegardé avec joblib
* Une campagne de test est créée pour prédire les frais d’un profil fictif :

| age | sex   | bmi  | children | smoker | region |
|-----|-------|------|----------|--------|--------|
| 24  | False | 23   | 2        | True   | Nord   |



