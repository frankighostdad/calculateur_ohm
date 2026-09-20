import streamlit as st

st.title("Calculateur Ohm Web ⚡")
st.write("Choisis la valeur que tu cherches à calculer :")

# Menu pour choisir quoi calculer
choix = st.radio("Je veux calculer :", ["La Tension (V)", "Le Courant (A)", "La Résistance (Ohms)"])

st.divider() # Ligne de séparation

# Affichage selon le choix
if choix == "La Tension (V)":
    st.image("batterie.jpg", width=50) # Affiche l'image de la batterie
    courant = st.number_input("Entre le Courant (en Ampères) :", value=0.0)
    resistance = st.number_input("Entre la Résistance (en Ohms) :", value=0.0)
    if st.button("Calculer la Tension", type="primary"):
        tension = courant * resistance
        st.success(f"Résultat : La tension est de {tension:.2f} Volts")

elif choix == "Le Courant (A)":
    st.image("eclair.jpg", width=50) # Affiche l'image de l'éclair
    tension = st.number_input("Entre la Tension (en Volts) :", value=0.0)
    resistance = st.number_input("Entre la Résistance (en Ohms) :", value=1.0)
    if st.button("Calculer le Courant", type="primary"):
        courant = tension / resistance
        st.success(f"Résultat : Le courant est de {courant:.2f} Ampères")

elif choix == "La Résistance (Ohms)":
    st.image("resistance.jpg", width=50) # Affiche l'image de la résistance
    tension = st.number_input("Entre la Tension (en Volts) :", value=0.0)
    courant = st.number_input("Entre le Courant (en Ampères) :", value=1.0)
    if st.button("Calculer la Résistance", type="primary"):
        resistance = tension / courant
        st.success(f"Résultat : La résistance est de {resistance:.2f} Ohms")