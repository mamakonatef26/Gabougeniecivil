import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# --- STYLE CSS ---
st.markdown("""
    <style>
    /* Menu de navigation */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        gap: 25px;
        padding: 20px;
        font-family: sans-serif;
    }
    .nav-link {
        text-decoration: none;
        color: #FFFFFF;
        font-weight: 500;
        font-size: 16px;
    }
    .nav-link:hover {
        color: #FFFFFF;
        border-bottom: 2px solid #FFFFFF;
    }

    /* Bannière principale */
    .hero-section {
        background: linear-gradient(135deg, #0A0F2C, #1B1F3B); /* Bleu nuit dégradé */
        padding: 40px 50px;
        color: white;
        border-radius: 0px;
        margin-bottom: 20px;
    }
    
    .hero-main-title {
        font-size: 50px;
        font-weight: 800;
        line-height: 1.0;
        margin-bottom: 15px;
        text-shadow: 0 0 10px #FFFFFF, 0 0 20px #FFFFFF, 0 0 30px #CCCCCC; /* effet de brillance */
    }

    .hero-highlight {
        color: #FFFFFF;
        text-shadow: 0 0 10px #FFFFFF, 0 0 20px #FFFFFF, 0 0 30px #CCCCCC;
    }

    .hero-quote {
        font-size: 16px;
        font-weight: bold;
        color: #FFFFFF;
        border-left: 3px solid #FFFFFF;
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
            <span class="hero-highlight">Génie Civil</span>
        </h1>
        <p class="hero-quote">We build your dreams</p>
        <p style="font-size: 18px; max-width: 600px; opacity: 0.9;">
            Études et réalisations en génie civil et VRD (Voirie et Réseau Divers). 
            Une expertise solide pour transformer vos visions en infrastructures durables.
        </p>
    </div>
    """, unsafe_allow_html=True)



# --- CONTACT & WHATSAPP ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.divider()
st.subheader("Nous contacter")
st.write("📞 +221 77 058 33 45 | 📧 gabougc2026@gmail.com")

st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
