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
________________________________________________________________________________
| Variable    |  Type                 |  Description                           |

| age         |  Quantitative         |     Âge de l'assuré                    |

| sex         | Qualitative binaire   |     Sexe (Male/Female)                 |

| bmi         | Quantitative          |     Indice de Masse Corporelle         |

| children    | Quantitative          |     Nombre d'enfants à charge          |

| smoker      | Qualitative binaire   |     Statut fumeur (Yes/No)             |

| region      | Qualitative           |     Région de résidence (4 modalités)  |

| charges     | Quantitative          |      Frais médicaux (variable cible)   |
________________________________________________________________________________
Source : Kaggle - Medical Insurance Price Prediction

# **🏗️ Architecture du projet**
📦 projet-assurance

├── 📄 assurance.py          

├── 📄 application.py        

├── 📄 modele.pkl          

├── 📄 campagne.csv       

├── 📁 static/

│   └── favicon.ico

└── 📄 README.md

# **🛠️ Technologies utilisées**

*Data Science & Machine Learning*

1. Python 

2. pandas - Manipulation de données

3. numpy - Calculs numériques

4. scikit-learn - Modèle RandomForest et preprocessing

5. OpenTURNS - Analyse de sensibilité (indices de Sobol)

*Visualisation*

1. matplotlib - Graphiques statistiques
2. seaborn - Visualisations avancées
3. yellowbrick - Diagnostics de régression

*Déploiement*

1. FastAPI - API REST
   
2. uvicorn - Serveur ASGI
   
3. joblib - Sérialisation du modèle
   
4. Pydantic - Validation des données



**Installer les dépendances**

pip install pandas numpy matplotlib seaborn scikit-learn
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























