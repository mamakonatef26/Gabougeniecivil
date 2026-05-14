import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS : Design épuré et professionnel (Inspiration CEDT G15)
st.markdown("""
    <style>
    /* Global : Fond blanc pur */
    .stApp {
        background-color: #FFFFFF !important;
    }

    /* En-tête / Navigation */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 8%;
        background: #FFFFFF;
        border-bottom: 2px solid #F0F2F6;
    }
    .logo {
        font-size: 24px;
        font-weight: 900;
        color: #1A237E; /* Bleu Nuit */
        text-transform: uppercase;
    }
    .nav-items a {
        text-decoration: none;
        color: #3D1F16 !important; /* Chocolat */
        margin-left: 30px;
        font-weight: 600;
        font-size: 14px;
    }

    /* Hero Section : Plus élégante, moins massive */
    .hero-wrap {
        padding: 60px 8%;
        background-color: #3D1F16; /* Chocolat */
        color: white !important;
        border-radius: 0 0 50px 0; /* Arrondi moderne */
    }
    .hero-title {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 10px;
        color: white !important;
    }
    .hero-sub {
        font-size: 20px;
        border-left: 4px solid #1A237E; /* Accent Bleu Nuit */
        padding-left: 20px;
        opacity: 0.9;
        color: white !important;
    }

    /* Section Titres */
    .section-title {
        color: #1A237E !important;
        font-size: 28px;
        font-weight: 700;
        margin: 40px 0 20px 0;
        border-bottom: 3px solid #3D1F16;
        display: inline-block;
    }

    /* Cards pour les Services */
    .service-card {
        background: #F8F9FA;
        padding: 25px;
        border-radius: 10px;
        border-top: 5px solid #1A237E;
        height: 100%;
    }

    /* Texte global */
    p, li, div {
        color: #2C3E50 !important;
    }
    
    /* WhatsApp */
    .wa-float {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header-container">
        <div class="logo">Gabou GC</div>
        <div class="nav-items">
            <a href="#">ACCUEIL</a>
            <a href="#propos">À PROPOS</a>
            <a href="#services">SERVICES</a>
            <a href="#contact">CONTACT</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
    <div class="hero-wrap">
        <h1 class="hero-title">Gabou Génie Civil</h1>
        <p class="hero-sub">L'expertise technique et la rigueur du CEDT G15 au service de vos infrastructures.</p>
    </div>
    """, unsafe_allow_html=True)

# --- CONTENU ---
st.markdown("<div style='padding: 0 8%;'>", unsafe_allow_html=True)

# À PROPOS
st.markdown("<div id='propos' class='section-title'>À Propos</div>", unsafe_allow_html=True)
st.write("""
Bureau d'études et de réalisation basé à Dakar, nous sommes spécialisés dans le **Génie Civil** et les **VRD**. 
Notre mission est de garantir la pérennité de vos ouvrages grâce à un suivi rigoureux et des solutions innovantes.
""")

# SERVICES
st.markdown("<div id='services' class='section-title'>Nos Services</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3 style="color:#1A237E;">🏗️ Bâtiment</h3>
            <p>Conception, calcul de structures et réalisation de projets immobiliers complexes.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3 style="color:#1A237E;">💧 VRD & Assainissement</h3>
            <p>Études de voiries et dimensionnement des réseaux de drainage et d'évacuation.</p>
        </div>
    """, unsafe_allow_html=True)

# CONTACT
st.markdown("<div id='contact' class='section-title'>Contact</div>", unsafe_allow_html=True)
st.markdown("### 📞 **+221 77 058 33 45**")
st.markdown("### 📧 **gabougc2026@gmail.com**")
st.write("📍 Guédiawaye, Dakar, Sénégal")

st.markdown("</div>", unsafe_allow_html=True)

# WHATSAPP
st.markdown("""
    <div class="wa-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
