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

    /* Bannière principale avec effet 3D */
    .hero-section {
        background: linear-gradient(145deg, #0A0F2C, #1B1F3B); /* Bleu nuit dégradé */
        padding: 40px 50px;
        color: white;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.8), inset 0 0 15px rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .hero-main-title {
        font-size: 50px;
        font-weight: 800;
        line-height: 1.0;
        margin-bottom: 15px;
        text-shadow: 
            2px 2px 4px rgba(0,0,0,0.8),
            0 0 10px #FFFFFF,
            0 0 20px #FFFFFF,
            0 0 30px #1E90FF;
    }

    .hero-highlight {
        color: #FFFFFF;
        text-shadow: 
            2px 2px 4px rgba(0,0,0,0.8),
            0 0 10px #FFFFFF,
            0 0 20px #FFFFFF,
            0 0 30px #1E90FF;
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

    /* Section À propos */
    .about-section {
        background: linear-gradient(145deg, #1B1F3B, #0A0F2C);
        color: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        margin: 30px 0;
        box-shadow: 0 6px 15px rgba(0,0,0,0.7), inset 0 0 10px rgba(255,255,255,0.1);
    }
    .about-section h2 {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 15px;
        text-shadow: 0 0 8px #FFFFFF;
    }
    .about-section p {
        font-size: 16px;
        line-height: 1.6;
        opacity: 0.95;
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

# --- À PROPOS ---
st.markdown("<div id='a-propos'></div>", unsafe_allow_html=True)
st.markdown("""
    <div class="about-section">
        <h2>À Propos de Gabou Génie Civil</h2>
        <p>
        Fondée en 2026 par Monsieur <strong>Abdoulaye Faty</strong>, Gabou Génie Civil est le fruit d'une ambition portée par l'excellence technique et la rigueur académique du <strong>CEDT G15</strong> (Centre d’Entrepreneuriat et de Développement Technique).
        </p>
        <p>
        Géomaticien de formation, le fondateur a souhaité allier la précision des technologies cartographiques et spatiales aux enjeux majeurs du génie civil et de l'assainissement urbain. Cette approche innovante permet à l'entreprise d'offrir des solutions d'ingénierie d'une précision chirurgicale, adaptées aux réalités du terrain.
        </p>
        <p>
        Basée à <strong>Guédiawaye</strong>, au cœur de la région de Dakar, Gabou Génie Civil se positionne comme un partenaire stratégique pour la conception, le suivi et la réalisation d'infrastructures durables. Qu'il s'agisse de projets de bâtiment ou de réseaux de voirie et d'assainissement (VRD), l'entreprise s'engage à bâtir l'avenir du Sénégal avec intégrité et professionnalisme.
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
