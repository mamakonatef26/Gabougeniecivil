import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS : Nettoyage total du orange pour du BLEU NUIT
st.markdown("""
    <style>
    /* 1. Barre de navigation */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        gap: 20px;
        padding: 20px;
    }
    .nav-link {
        text-decoration: none;
        color: #FFFFFF !important;
        font-weight: 500;
        font-size: 16px;
    }
    /* CHANGEMENT : Survol en Bleu Nuit (plus de orange ici) */
    .nav-link:hover {
        color: #1A237E !important;
        border-bottom: 2px solid #1A237E !important;
    }

    /* 2. Bannière principale */
    .hero-section {
        background-color: #3D1F16; 
        padding: 40px 50px;
        color: white;
        border-radius: 0px;
        margin-bottom: 40px;
    }
    .hero-top-text { color: #FFFFFF !important; letter-spacing: 2px; font-weight: bold; font-size: 14px; text-transform: uppercase; }
    .hero-main-title { font-size: 50px; font-weight: 800; line-height: 1.0; margin: 15px 0; color: white !important; }
    
    /* CHANGEMENT : Barre du slogan en Bleu Nuit */
    .hero-quote {
        font-size: 16px; font-weight: bold; color: #FFFFFF !important;
        border-left: 4px solid #1A237E !important; 
        padding-left: 15px;
        margin-bottom: 20px; text-transform: uppercase;
    }

    /* 3. Global Streamlit : Supprimer le orange des liens et boutons par défaut */
    a { color: #1A237E !important; }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #3D1F16 !important; }
    
    /* Couleur de la ligne de division (divider) */
    hr { border-top: 1px solid #1A237E !important; }

    .content-section {
        padding: 20px 50px;
        color: #3D1F16;
    }

    /* Bouton WhatsApp */
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
        <a class="nav-link" href="#a-propos">À propos</a>
        <a class="nav-link" href="#nos-services">Nos Services</a>
        <a class="nav-link" href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

# --- ACCUEIL ---
st.markdown("""
    <div class="hero-section">
        <p class="hero-top-text">ENTREPRISE PRIVÉE — DAKAR, SÉNÉGAL</p>
        <h1 class="hero-main-title">Gabou<br>Génie Civil</h1>
        <p class="hero-quote">NOUS BÂTISSONS VOS AMBITIONS</p>
        <p style="font-size: 18px; max-width: 600px; opacity: 0.9;">
            Études et réalisations en génie civil et VRD (Voirie et Réseau Divers). 
            Une expertise solide pour transformer vos visions en infrastructures durables.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTIONS ---
st.markdown("<div id='a-propos' class='content-section'><h2>À propos</h2><p>Gabou Génie Civil accompagne vos projets de construction avec rigueur et professionnalisme à Dakar et partout au Sénégal.</p></div>", unsafe_allow_html=True)

st.markdown("<div id='nos-services' class='content-section'><h2>Nos Services</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='color: #1A237E !important;'>🏗️ Bâtiment</h3>", unsafe_allow_html=True)
    st.write("Conception et réalisation de gros œuvre.")
with col2:
    st.markdown("<h3 style='color: #1A237E !important;'>💧 VRD</h3>", unsafe_allow_html=True)
    st.write("Assainissement et réseaux divers.")
st.markdown("</div>", unsafe_allow_html=True)

# --- CONTACT ---
st.divider()
st.markdown("<div id='contact' class='content-section'><h3>Contact</h3><p>📞 +221 77 058 33 45<br>📧 gabougc2026@gmail.com</p></div>", unsafe_allow_html=True)

# WhatsApp
st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
