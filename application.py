import os
os.chdir("C:/Users/Utilisateur/Desktop/APPLICATION MODELE")
print("Répertoire courant :", os.getcwd())
import streamlit as st
import joblib
import pandas as pd

# Charger le modèle entraîné
@st.cache_resource
def load_model():
    # Charger le modèle avec joblib
    try:
        with open("C:/Users/Utilisateur/Desktop/APPLICATION MODELE/modele.pkl", "rb") as file:
            model = joblib.load(file)
        return model
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {str(e)}")
        return None

model = load_model()

# Vérifiez si le modèle est valide
if model and not hasattr(model, "predict"):
    st.error("Le modèle chargé n'a pas de méthode 'predict'. Vérifiez que vous avez bien enregistré un modèle scikit-learn valide.")
elif not model:
    st.error("Le modèle n'a pas pu être chargé correctement. Veuillez vérifier le fichier.")

# Interface utilisateur
st.title("Déploiement d'un modèle RandomForestRegressor()")

# Ajouter une photo illustrative
st.image("C:/Users/Utilisateur/Desktop/APPLICATION MODELE/image.jpg", caption="Photo", use_column_width=True)

st.subheader("Simuler vos dépenses médicales")

# Champs d'entrée utilisateur
age = st.number_input("Quel âge avez-vous ?", min_value=0, step=1, format="%d")
sex = st.radio("Quel est votre sexe ?", ["Homme", "Femme"])  # Pas de valeur par défaut
bmi = st.number_input("Quel est votre IMC (Indice de Masse Corporelle) ?", min_value=0.0, step=0.1, format="%.1f")
children = st.number_input("Nombre d'enfants", min_value=0, step=1, format="%d")
smoker = st.radio("Est-ce que vous fumez ?", ["Oui", "Non"])  # Pas de valeur par défaut
region = st.radio("Quelle est votre région ?", ["Nord", "Sud", "Est", "Ouest"])  # Pas de valeur par défaut

if st.button("Simulation"):
    try:
        # Afficher les données saisies par le client
        st.subheader("Données saisies par le client :")
        donne = pd.DataFrame({
            "Age": [age],
            "Sexe": [sex],
            "Indice de Masse Corporelle": [bmi],
            "Nombre d'enfants": [children],
            "Fumeur": [smoker],
            "Région": [region]
        })
        st.write(donne)

        # Encodage des variables qualitatives
        sex_encoded = False if sex == "Femme" else True  # False pour Femme, True pour Homme
        smoker_encoded = True if smoker == "Oui" else False  # True pour Oui, False pour Non

        # Préparer les données pour le modèle
        input_data = pd.DataFrame({
            'age': [age],
            'sex': [sex_encoded],  # Booléen
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker_encoded],  # Booléen
            'region': [region]  # Pas d'encodage supplémentaire pour la région
        })

        # Prédiction avec le modèle
        if model:
            prediction = model.predict(input_data)
            st.success(f"Les dépenses médicales pour ce client seront : {prediction[0]:.2f} $")
        else:
            st.error("Le modèle n'est pas disponible pour effectuer la prédiction.")
    except Exception as e:
        st.error(f"Une erreur est survenue : {str(e)}")
