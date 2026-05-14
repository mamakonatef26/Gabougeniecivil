import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS pour imiter le style du CEDT (image_79a338.png)
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
        color: #FF4B2B;
        border-bottom: 2px solid #FF4B2B;
    }

    /* Bannière principale affinée */
    .hero-section {
        background-color: #3D1F16; 
        padding: 40px 50px; /* Réduit de 80px à 40px pour un cadre moins haut */
        color: white;
        border-radius: 0px;
        margin-bottom: 20px;
    }
    
    .hero-main-title {
        font-size: 50px; /* Légèrement réduit pour gagner de l'espace */
        font-weight: 800;
        line-height: 1.0;
        margin-bottom: 15px;
    }

    .hero-quote {
        font-size: 16px;
        font-weight: bold;
        color: #FF4B2B;
        border-left: 3px solid #FF4B2B;
        padding-left: 15px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }

    /* Bouton WhatsApp flottant (en bas à droite) */
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

# --- BANNIÈRE D'ACCUEIL (Style CEDT) ---
st.markdown("""
    <div class="hero-section">
        <p class="hero-top-text">ENTREPRISE PRIVÉE — DAKAR, SÉNÉGAL</p>
        <h1 class="hero-main-title">
            Gabou<br>
            Génie <span class="hero-highlight">Civil</span>
        </h1>
        <p class="hero-quote">« CONSTRUIRE AVEC RIGUEUR ET PASSION »</p>
        <p style="font-size: 18px; max-width: 600px; opacity: 0.9;">
            Expertise en BTP, assainissement et études techniques. 
            Nous transformons vos visions en infrastructures durables.
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

# Bouton WhatsApp (Style icône flottante comme sur l'image)
st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
