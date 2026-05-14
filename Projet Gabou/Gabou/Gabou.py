import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS complet pour supprimer les cadres orange et harmoniser le style
st.markdown("""
    <style>
    /* Navigation */
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
    }

    /* Bannière principale affinée */
    .hero-section {
        background-color: #3D1F16; 
        padding: 40px 50px;
        color: white;
        margin-bottom: 30px;
    }
    .hero-top-text { color: #FFFFFF !important; letter-spacing: 2px; font-weight: bold; font-size: 14px; }
    .hero-main-title { font-size: 50px; font-weight: 800; line-height: 1.0; margin: 15px 0; }
    .hero-highlight { color: #FFFFFF !important; }
    .hero-quote {
        font-size: 16px;
        font-weight: bold;
        color: #FFFFFF !important;
        border-left: 3px solid #FFFFFF !important;
        padding-left: 15px;
        text-transform: uppercase;
    }

    /* Suppression des cadres orange des colonnes de services */
    .custom-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: none; /* Enlève toute bordure */
        text-align: center;
        color: #3D1F16;
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
st.markdown('<div class="nav-container"><a class="nav-link" href="#">Accueil</a><a class="nav-link" href="#services">Nos Services</a><a class="nav-link" href="#contact">Contact</a></div>', unsafe_allow_html=True)

# --- BANNIÈRE D'ACCUEIL ---
st.markdown("""
    <div class="hero-section">
        <p class="hero-top-text">ENTREPRISE PRIVÉE — DAKAR, SÉNÉGAL</p>
        <h1 class="hero-main-title">Gabou<br>Génie <span class="hero-highlight">Civil</span></h1>
        <p class="hero-quote">NOUS BÂTISSONS VOS AMBITIONS</p>
        <p style="font-size: 18px; max-width: 600px; opacity: 0.9;">
            Études et réalisations en génie civil et VRD (Voirie et Réseau Divers). 
            Une expertise solide pour transformer vos visions en infrastructures durables.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SERVICES (SANS CADRES ORANGE) ---
st.markdown("<h2 style='color: #3D1F16; text-align: center;'>Nos Domaines d'Expertise</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="custom-card">🏗️<br><b>BTP & Gros Œuvre</b></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="custom-card">💧<br><b>Assainissement</b></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="custom-card">📐<br><b>Bureau d\'Études</b></div>', unsafe_allow_html=True)

# --- CONTACT ---
st.divider()
st.markdown("<div id='contact' style='color: #3D1F16;'><h3>Nous contacter</h3><p>📞 +221 77 058 33 45 | 📧 gabougc2026@gmail.com</p></div>", unsafe_allow_html=True)

# WhatsApp
st.markdown('<div class="whatsapp-float"><a href="https://wa.me/221770583345" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60"></a></div>', unsafe_allow_html=True)
