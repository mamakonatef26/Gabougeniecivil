import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS : Correction totale pour la lisibilité sur fond sombre
st.markdown("""
    <style>
    /* Global : Fond noir et texte blanc */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Menu de navigation */
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
    .nav-link:hover {
        color: #1A237E !important;
        border-bottom: 2px solid #1A237E !important;
    }

    /* Bannière principale Chocolat */
    .hero-section {
        background-color: #3D1F16; 
        padding: 40px 50px;
        color: white !important;
        border-radius: 5px;
        margin-bottom: 40px;
    }
    .hero-main-title { 
        font-size: 50px; 
        font-weight: 800; 
        color: white !important;
        margin: 10px 0;
    }
    .hero-quote {
        font-size: 16px; 
        font-weight: bold; 
        color: white !important;
        border-left: 4px solid #1A237E !important; /* Barre Bleu Nuit */
        padding-left: 15px;
        text-transform: uppercase;
    }

    /* Forcer tous les titres et textes hors bannière en BLANC */
    h1, h2, h3, p, span, li {
        color: #FFFFFF !important;
    }

    /* Couleur spécifique pour les icônes ou petits accents en Bleu Nuit */
    .blue-accent {
        color: #1A237E !important;
        font-weight: bold;
    }

    /* Suppression des ancres Streamlit qui apparaissent en orange */
    .element-container a {
        color: #1A237E !important;
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
        <a class="nav-link" href="#a-propos">À propos</a>
        <a class="nav-link" href="#nos-services">Nos Services</a>
        <a class="nav-link" href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

# --- ACCUEIL (Bannière) ---
st.markdown("""
    <div class="hero-section">
        <p style="letter-spacing: 2px; font-size: 14px;">ENTREPRISE PRIVÉE — DAKAR, SÉNÉGAL</p>
        <h1 class="hero-main-title">Gabou<br>Génie Civil</h1>
        <p class="hero-quote">NOUS BÂTISSONS VOS AMBITIONS</p>
        <p style="font-size: 18px; max-width: 600px; opacity: 0.9;">
            Études et réalisations en génie civil et VRD (Voirie et Réseau Divers). 
            Une expertise solide pour transformer vos visions en infrastructures durables.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION À PROPOS ---
st.markdown("<div id='a-propos' style='padding: 20px 50px;'>", unsafe_allow_html=True)
st.header("À propos")
st.write("Gabou Génie Civil accompagne vos projets de construction avec rigueur et professionnalisme à Dakar et partout au Sénégal.")
st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION NOS SERVICES ---
st.markdown("<div id='nos-services' style='padding: 20px 50px;'>", unsafe_allow_html=True)
st.header("Nos Services")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🏗️ <span class='blue-accent'>Bâtiment</span>", unsafe_allow_html=True)
    st.write("Conception et réalisation de gros œuvre.")
with col2:
    st.markdown("### 💧 <span class='blue-accent'>VRD</span>", unsafe_allow_html=True)
    st.write("Assainissement et réseaux divers.")
st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION CONTACT ---
st.markdown("<div id='contact' style='padding: 20px 50px;'>", unsafe_allow_html=True)
st.divider()
st.subheader("Contact")
st.write("📞 +221 77 058 33 45")
st.write("📧 gabougc2026@gmail.com")
st.markdown("</div>", unsafe_allow_html=True)

# WhatsApp
st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
