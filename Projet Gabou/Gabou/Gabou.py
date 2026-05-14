import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS pour un look minimaliste (Inspiré par image_792b16.png)
st.markdown("""
    <style>
    /* Menu de navigation */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        gap: 25px;
        padding: 20px;
    }
    .nav-link {
        text-decoration: none;
        color: #3D1F16;
        font-weight: 500;
        font-size: 16px;
    }

    /* Bannière principale (Couleur Chocolat) */
    .hero-section {
        background-color: #3D1F16; 
        padding: 40px 50px;
        color: white;
        border-radius: 0px;
        margin-bottom: 40px;
    }
    .hero-top-text {
        color: #FFFFFF !important;
        letter-spacing: 2px;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .hero-main-title {
        font-size: 50px;
        font-weight: 800;
        line-height: 1.0;
        margin-bottom: 15px;
    }
    .hero-highlight {
        color: #FFFFFF !important;
    }
    .hero-quote {
        font-size: 16px;
        font-weight: bold;
        color: #FFFFFF !important;
        border-left: 3px solid #FFFFFF !important;
        padding-left: 15px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }

    /* Bouton WhatsApp flottant */
    .whatsapp-float {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("""
    <div class="nav-container">
        <a class="nav-link" href="#">Accueil</a>
        <a class="nav-link" href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

# --- BANNIÈRE D'ACCUEIL ---
st.markdown("""
    <div class="hero-section">
        <p class="hero-top-text">ENTREPRISE PRIVÉE — DAKAR, SÉNÉGAL</p>
        <h1 class="hero-main-title">
            Gabou<br>
            Génie <span class="hero-highlight">Civil</span>
        </h1>
        <p class="hero-quote">NOUS BÂTISSONS VOS AMBITIONS</p>
        <p style="font-size: 18px; max-width: 600px; opacity: 0.9;">
            Études et réalisations en génie civil et VRD (Voirie et Réseau Divers). 
            Une expertise solide pour transformer vos visions en infrastructures durables.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION CONTACT (Directement après la bannière) ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.divider()
st.subheader("Nous contacter")
st.write("📞 +221 77 058 33 45 | 📧 gabougc2026@gmail.com")

# Bouton WhatsApp Flottant
st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
