import streamlit as st

# Configuration
st.set_page_config(page_title="Gabou Génie Civil | Expertise G15", page_icon="🏗️", layout="wide")

# CSS Inspiré du style institutionnel (Propre et contrasté)
st.markdown("""
    <style>
    /* Fond de page gris très clair pour faire ressortir les blocs blancs */
    .stApp {
        background-color: #F4F7F6;
    }

    /* Barre de Navigation (Style G15) */
    .nav-bar {
        background-color: #FFFFFF;
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 3px solid #1A237E; /* Ligne Bleu Nuit */
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .nav-links a {
        text-decoration: none;
        color: #3D1F16 !important; /* Chocolat */
        font-weight: bold;
        margin-left: 20px;
        font-size: 15px;
    }
    .nav-links a:hover {
        color: #1A237E !important; /* Bleu Nuit au survol */
    }

    /* Section Héro (Bannière) */
    .hero {
        background-color: #3D1F16;
        color: white !important;
        padding: 80px 50px;
        text-align: left;
    }
    .hero h1 { color: white !important; font-size: 50px; margin-bottom: 10px; }
    .hero p { color: #DCDCDC !important; font-size: 20px; border-left: 4px solid #1A237E; padding-left: 15px; }

    /* Blocs de contenu blancs (Comme sur le site du CEDT) */
    .white-card {
        background-color: #FFFFFF;
        padding: 40px;
        margin: 20px 50px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    
    h2 { color: #1A237E !important; border-bottom: 2px solid #F4F7F6; padding-bottom: 10px; }
    h3 { color: #3D1F16 !important; }
    p, li { color: #444444 !important; line-height: 1.6; }

    /* Bouton WhatsApp */
    .whatsapp-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("""
    <div class="nav-bar">
        <div style="font-weight: 900; font-size: 20px; color: #1A237E;">GABOU GC</div>
        <div class="nav-links">
            <a href="#">ACCUEIL</a>
            <a href="#a-propos">À PROPOS</a>
            <a href="#services">NOS SERVICES</a>
            <a href="#contact">CONTACT</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- BANNIÈRE PRINCIPALE ---
st.markdown("""
    <div class="hero">
        <h1>Gabou Génie Civil</h1>
        <p>L'expertise technique au service du développement durable.<br>
        Inspiré par la rigueur de la formation du CEDT G15.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION À PROPOS (Bloc Blanc) ---
st.markdown(f"<div id='a-propos' class='white-card'>", unsafe_allow_html=True)
st.markdown("<h2>À propos de l'entreprise</h2>", unsafe_allow_html=True)
st.write("""
Spécialisée en Génie Civil et VRD, notre entreprise s'appuie sur une solide base technique pour réaliser vos projets d'infrastructure. 
Notre approche combine les méthodes classiques de construction et les nouvelles technologies géomatiques pour une précision optimale.
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION SERVICES (Bloc Blanc) ---
st.markdown(f"<div id='services' class='white-card'>", unsafe_allow_html=True)
st.markdown("<h2>Nos Domaines d'Intervention</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🏗️ Bâtiment & Construction")
    st.write("- Études techniques et calcul de structure")
    st.write("- Suivi et contrôle de chantiers")
    st.write("- Gros œuvre et second œuvre")
with col2:
    st.markdown("### 💧 VRD & Assainissement")
    st.write("- Aménagement de voiries urbaines")
    st.write("- Dimensionnement de réseaux d'évacuation")
    st.write("- Études topographiques")
st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION CONTACT (Bloc Blanc) ---
st.markdown(f"<div id='contact' class='white-card' style='margin-bottom: 100px;'>", unsafe_allow_html=True)
st.markdown("<h2>Contactez-nous</h2>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown("### 📞 Téléphone")
    st.write("+221 77 058 33 45")
with c2:
    st.markdown("### 📧 Email")
    st.write("gabougc2026@gmail.com")
st.markdown("</div>", unsafe_allow_html=True)

# WhatsApp Flottant
st.markdown("""
    <div class="whatsapp-btn">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
