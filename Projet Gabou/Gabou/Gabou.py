import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS mis à jour : Tout en Blanc sur Chocolat
st.markdown("""
    <style>
    /* Menu de navigation en haut à droite */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        gap: 25px;
        padding: 20px;
        font-family: sans-serif;
    }
    .nav-link {
        text-decoration: none;
        color: #3D1F16;
        font-weight: 500;
        font-size: 16px;
    }
    .nav-link:hover {
        color: #FF4B2B; /* On garde une touche d'orange au survol pour l'interactivité */
        border-bottom: 2px solid #FF4B2B;
    }

    /* Bannière principale affinée */
    .hero-section {
        background-color: #3D1F16; 
        padding: 40px 50px;
        color: white;
        border-radius: 0px;
        margin-bottom: 20px;
    }
    
    /* Texte du haut en BLANC */
    .hero-top-text {
        color: #FFFFFF !important;
        letter-spacing: 2px;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .hero-main-title {
        font-size: 50px;
        font-weight: 800;
        line-height: 1.0;
        margin-bottom: 15px;
    }

    /* Le mot Civil en BLANC */
    .hero-highlight {
        color: #FFFFFF !important;
    }

    /* Slogan et barre latérale en BLANC */
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

# --- MENU DE NAVIGATION ---
st.markdown("""
    <div class="nav-container">
        <a class="nav-link" href="#">Accueil</a>
        <a class="nav-link" href="#a-propos">À propos</a>
        <a class="nav-link" href="#services">Nos Services</a>
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

# --- SECTIONS SUIVANTES ---
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.header("Nos Domaines d'Expertise")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("🏗️ **BTP & Gros Œuvre**")
with col2:
    st.info("💧 **Assainissement**")
with col3:
    st.info("📐 **Bureau d'Études**")

# --- CONTACT & WHATSAPP ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.divider()
st.subheader("Nous contacter")
st.write("📞 +221 77 058 33 45 | 📧 gabougc2026@gmail.com")

# Bouton WhatsApp flottant
st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
