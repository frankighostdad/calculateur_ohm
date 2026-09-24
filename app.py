import streamlit as st
import base64

st.set_page_config(page_title="Calculateur Électronique", layout="centered")

def ajouter_fond(fichier_image):
    try:
        with open(fichier_image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("data:image/jpg;base64,{encoded_string}");
                background-size: cover;
                background-attachment: fixed;
            }}
            h1, p, span, label {{
                text-shadow: 2px 2px 5px #000000;
                font-weight: 600 !important;
                color: #FAFAFA !important;
            }}
            .stTextInput, .stNumberInput > div {{
                background-color: rgba(0, 0, 0, 0.7); 
                color: white;
            }}
            .stTabs [data-baseweb="tab-list"] {{
                background-color: rgba(0, 0, 0, 0.85);
                border-radius: 10px;
                padding: 10px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        pass

ajouter_fond("circuit.jpg")

st.title("Calculateur de Loi d'Ohm ⚡")
st.write("Bienvenue sur l'application Web de mon circuit !")
st.divider()

onglet_tension, onglet_courant, onglet_resistance = st.tabs(["⚡ Tension (V)", "🌊 Courant (A)", "🧱 Résistance (Ω)"])

with onglet_tension:
    try:
        st.image("batterie.jpg", width=100)
    except:
        pass
    courant = st.number_input("Entre le courant (en Ampères) :", min_value=0.0, value=0.0, key="c1")
    resistance = st.number_input("Entre la résistance (en Ohms) :", min_value=0.0, value=0.0, key="r1")
    
    if st.button("Calculer la tension", key="btn1"):
        tension = courant * resistance
        puissance = tension * courant
        st.success(f"Résultat : {tension:.2f} Volts")
        
        # L'easter egg de la fumée magique
        if puissance > 5:
            st.warning(f"🔥 Alerte ! {puissance:.2f} Watts... Tu as libéré la fameuse « fumée magique » ! Le composant est grillé ! 💨")
        else:
            st.info(f"💡 Puissance dissipée : {puissance:.2f} Watts")

with onglet_courant:
    try:
        st.image("eclair.jpg", width=100)
    except:
        pass
    tension = st.number_input("Entre la tension (en Volts) :", min_value=0.0, value=0.0, key="t2")
    resistance = st.number_input("Entre la résistance (en Ohms) :", min_value=0.0, value=0.0, key="r2")
    
    if st.button("Calculer le courant", key="btn2"):
        if resistance == 0 and tension > 0:
            st.error("💥 BOUM ! Court-circuit ! Prépare l'extincteur !")
        elif resistance == 0:
            st.error("Attention : La résistance ne peut pas être de 0 Ohm !")
        else:
            courant = tension / resistance
            puissance = tension * courant
            st.success(f"Résultat : {courant:.4f} Ampères")
            
            if puissance > 5:
                st.warning(f"🔥 Alerte ! {puissance:.2f} Watts... Tu as libéré la fameuse « fumée magique » ! Le composant est grillé ! 💨")
            else:
                st.info(f"💡 Puissance dissipée : {puissance:.2f} Watts")

with onglet_resistance:
    try:
        st.image("resistance.jpg", width=100)
    except:
        pass
    tension = st.number_input("Entre la tension (en Volts) :", min_value=0.0, value=0.0, key="t3")
    courant = st.number_input("Entre le courant (en Ampères) :", min_value=0.0, value=0.0, key="c3")
    
    if st.button("Calculer la résistance", key="btn3"):
        if courant == 0:
            st.error("Attention : Le courant ne peut pas être de 0 Ampère !")
        else:
            resistance = tension / courant
            puissance = tension * courant
            st.success(f"Résultat : {resistance:.2f} Ohms")
            
            if puissance > 5:
                st.warning(f"🔥 Alerte ! {puissance:.2f} Watts... Tu as libéré la fameuse « fumée magique » ! Le composant est grillé ! 💨")
            else:
                st.info(f"💡 Puissance dissipée : {puissance:.2f} Watts")
