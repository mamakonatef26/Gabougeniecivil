import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS : FORCER LE THÈME CLAIR ET LE TEXTE NOIR
st.markdown("""
    <style>
    /* Force le fond en blanc et le texte en noir pour la lisibilité */
    .stApp {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    /* Menu de navigation (Texte Bleu Nuit) */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        gap: 25px;
        padding: 20px;
        background-color: #F8F9FA;
    }
    .nav-link {
        text-decoration: none;
        color: #1A237E !important;
        font-weight: bold;
        font-size: 16px;
    }

    /* Bannière Chocolat (Seul bloc sombre) */
    .hero-section {
        background-color: #3D1F16; 
        padding: 60px 50px;
        color: #FFFFFF !important;
        margin-bottom: 30px;
    }
    .hero-main-title { 
        font-size: 55px; 
        font-weight: 800; 
        color: #FFFFFF !important;
        margin-bottom: 10px;
    }
    .hero-quote {
        font-size: 18px; 
        font-weight: bold; 
        color: #FFFFFF !important;
        border-left: 5px solid #1A237E !important; /* Barre Bleu Nuit */
        padding-left: 20px;
    }

    /* Titres des sections en Bleu Nuit */
    h1, h2, h3 {
        color: #1A237E !important;
        font-weight: 700 !important;
    }

    /* Texte normal en Noir profond */
    p, span, div {
        color: #000000 !important;
    }

    /* Bouton WhatsApp */
    .whatsapp-float {
        position: fixed;
        bottom: 25px;
        right: 25px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE DE NAVIGATION ---
st.markdown("""
    <div class="nav-container">
        <a class="nav-link" href="#">ACCUEIL</a>
        <a class="nav-link" href="#a-propos">À PROPOS</a>
        <a class="nav-link" href="#nos-services">SERVICES</a>
        <a class="nav-link" href="#contact">CONTACT</a>
    </div>
    """, unsafe_allow_html=True)

# --- ACCUEIL (Bannière) ---
st.markdown("""
    <div class="hero-section">
        <p style="letter-spacing: 2px; color: #FFFFFF !important;">ENTREPRISE PRIVÉE — DAKAR, SÉNÉGAL</p>
        <h1 class="hero-main-title">Gabou Génie Civil</h1>
        <p class="hero-quote">NOUS BÂTISSONS VOS AMBITIONS</p>
        <p style="font-size: 19px; opacity: 0.9; color: #FFFFFF !important;">
            Expertise en bâtiment, travaux publics et assainissement à Guédiawaye.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTIONS ---
st.markdown("<div id='a-propos' style='padding: 40px 50px;'>", unsafe_allow_html=True)
st.header("À Propos")
st.write("Gabou Génie Civil est un bureau d'études et de réalisation spécialisé dans le BTP et les VRD. Nous mettons notre expertise au service de la durabilité de vos infrastructures.")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.markdown("<div id='nos-services' style='padding: 40px 50px;'>", unsafe_allow_html=True)
st.header("Nos Services")
c1, c2 = st.columns(2)
with c1:
    st.subheader("🏗️ Bâtiment & Génie Civil")
    st.write("Construction, rénovation et suivi de chantiers complexes.")
with c2:
    st.subheader("💧 VRD & Assainissement")
    st.write("Gestion des réseaux d'eaux et aménagement urbain.")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- CONTACT ---
st.markdown("<div id='contact' style='padding: 40px 50px;'>", unsafe_allow_html=True)
st.header("Contact")
st.markdown("### 📞 Téléphone : **+221 77 058 33 45**")
st.markdown("### 📧 Email : **gabougc2026@gmail.com**")
st.write("📍 Dakar, Sénégal")
st.markdown("</div>", unsafe_allow_html=True)

# WhatsApp
st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="65">
        </a>
    </div>
    """, unsafe_allow_html=True)
