# **📋 Table des matières**

À propos du projet

Dataset

Architecture du projet

Technologies utilisées

Installation

Utilisation

Méthodologie

Résultats

API REST

Analyse de sensibilité


# **🎯 À propos du projet**
Ce projet vise à construire un modèle de Machine Learning pour prédire les frais d'assurance santé en fonction de caractéristiques personnelles et comportementales des assurés. L'objectif est d'améliorer l'efficacité et la rentabilité des compagnies d'assurance maladie en leur permettant d'évaluer plus précisément les risques et de tarifer leurs offres.
Problématique
Comment construire un modèle d'apprentissage automatique pour améliorer l'efficacité et la rentabilité des compagnies d'assurance maladie ?
# **📊 Dataset**
L'ensemble de données contient 27 000 observations avec 7 variables :
VariableTypeDescriptionageQuantitativeÂge de l'assurésexQualitative binaireSexe (Male/Female)bmiQuantitativeIndice de Masse CorporellechildrenQuantitativeNombre d'enfants à chargesmokerQualitative binaireStatut fumeur (Yes/No)regionQualitativeRégion de résidence (4 modalités)chargesQuantitativeFrais médicaux (variable cible)
Source : Kaggle - Medical Insurance Price Prediction
# **🏗️ Architecture du projet**
📦 projet-assurance
├── 📄 assurance.py          # Script principal
├── 📄 application.py        # API FastAPI
├── 📄 modele.pkl           # Modèle entraîné sauvegardé
├── 📄 campagne.csv         # Exemple de données de test
├── 📁 static/
│   └── favicon.ico
└── 📄 README.md
🛠️ Technologies utilisées
Data Science & Machine Learning

Python 3.8+
pandas - Manipulation de données
numpy - Calculs numériques
scikit-learn - Modèle RandomForest et preprocessing
OpenTURNS - Analyse de sensibilité (indices de Sobol)

Visualisation

matplotlib - Graphiques statistiques
seaborn - Visualisations avancées
yellowbrick - Diagnostics de régression

Déploiement

FastAPI - API REST
uvicorn - Serveur ASGI
joblib - Sérialisation du modèle
Pydantic - Validation des données

# **📥 Installation**
*Prérequis*
bashpython >= 3.8
pip >= 21.0
Étapes d'installation

Cloner le repository

bashgit clone https://github.com/votre-username/projet-assurance.git
cd projet-assurance

Créer un environnement virtuel

bashpython -m venv venv
venv\Scripts\activate  # Windows

*Installer les dépendances*

bashpip install pandas numpy matplotlib seaborn scikit-learn
pip install kagglehub joblib openturns yellowbrick
pip install fastapi uvicorn pydantic
# **🚀 Utilisation**

1. Entraînement du modèle
   
  bashpython assurance.py
  Le script effectue :

    ✅ Chargement et exploration des données
    ✅ Analyse exploratoire (EDA)
    ✅ Prétraitement des données
    ✅ Optimisation des hyperparamètres (GridSearchCV)
    ✅ Évaluation du modèle
    ✅ Analyse de sensibilité (Sobol)
    ✅ Sauvegarde du modèle (modele.pkl)

2. Lancement de l'API
   
  python application.py
  
  L'API sera accessible sur http://localhost:8000
  
# **Documentation interactive**

Swagger UI : http://localhost:8000/docs
ReDoc : http://localhost:8000/redoc

3. Exemple de prédiction
4. 
   "http://localhost:8000/deploiement/?age=24&sexe=Homme&bmi=23&children=2&smoker=Yes&region=Nord"



# Prédiction
prediction = model.predict(data)
print(f"Charges estimées : ${prediction[0]:,.2f}")
🔬 Méthodologie
1. Prétraitement des données

Encodage des variables catégorielles (sexe, fumeur, région)
Standardisation des variables numériques
Pipeline scikit-learn pour automatisation

2. Modélisation

Algorithme : RandomForestRegressor
Optimisation : GridSearchCV avec validation croisée (5-fold)
Hyperparamètres optimisés :

n_estimators : [80, 90, 100, 200]
max_depth : [5, 10, 15, 20, 25, 30, None]
min_samples_split : [2, 5, 10, 15, 20]
min_samples_leaf : [8, 10, 20, 25]
max_features : ['sqrt', 'log2', None]



3. Évaluation

RMSE (Root Mean Squared Error)
R² (Coefficient de détermination)
MAPE (Mean Absolute Percentage Error)
Analyse des résidus (Yellowbrick)
Courbes d'apprentissage

📈 Résultats
Les performances du modèle sont évaluées sur l'ensemble de test (30% des données) :
Métriques de performance :
├── RMSE : [À remplir après exécution]
├── R² : [À remplir après exécution]
└── MAPE : [À remplir après exécution]
Variables les plus importantes
L'analyse montre que les facteurs clés influençant les charges sont :

Statut fumeur (smoker)
Âge (age)
IMC (bmi)

🌐 API REST
Endpoints disponibles
1. Information générale
httpGET /
Retourne les informations sur l'API.
2. Prédiction
httpGET /deploiement/
Paramètres :

age (int) : Âge de l'assuré
sexe (enum) : "Homme" ou "Femme"
bmi (float) : Indice de Masse Corporelle
children (int) : Nombre d'enfants
smoker (enum) : "Yes" ou "Non"
region (enum) : "Nord", "Sud", "Est" ou "Ouest"

Réponse :
json{
  "Sa charge est de ": 12345.67
}
Exemple avec Postman
GET http://localhost:8000/deploiement/?age=35&sexe=Femme&bmi=28.5&children=1&smoker=Non&region=Sud
🔍 Analyse de sensibilité
Le projet inclut une analyse de sensibilité complète utilisant les indices de Sobol via OpenTURNS.
Objectif
Identifier quelles variables ont le plus d'impact sur les prédictions du modèle.
Indices calculés

Indices de premier ordre : Effet direct de chaque variable
Indices totaux : Effet direct + interactions

Interprétation
Plus l'indice de Sobol est élevé, plus la variable est influente dans les prédictions du modèle.
📝 Statistiques descriptives
Le code génère des analyses statistiques complètes :

Distribution des variables par catégorie
Corrélations entre variables
Boxplots et scatter plots
Graphiques circulaires pour les variables catégorielles

























