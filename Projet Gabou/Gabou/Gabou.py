import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# CSS : Remplacement du Orange par Bleu Nuit (#1A237E)
st.markdown("""
    <style>
    /* Menu de navigation */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        gap: 20px;
        padding: 20px;
    }
    .nav-link {
        text-decoration: none;
        color: #FFFFFF;
        font-weight: 500;
        font-size: 16px;
    }
    .nav-link:hover {
        color: #1A237E; /* Bleu Nuit au survol */
        border-bottom: 2px solid #1A237E;
    }

    /* Bannière principale Chocolat */
    .hero-section {
        background-color: #3D1F16; 
        padding: 40px 50px;
        color: white;
        border-radius: 0px;
        margin-bottom: 40px;
    }
    .hero-top-text { color: #FFFFFF !important; letter-spacing: 2px; font-weight: bold; font-size: 14px; text-transform: uppercase; }
    .hero-main-title { font-size: 50px; font-weight: 800; line-height: 1.0; margin: 15px 0; }
    
    /* Barre verticale en Bleu Nuit */
    .hero-quote {
        font-size: 16px; font-weight: bold; color: #FFFFFF !important;
        border-left: 3px solid #1A237E !important; /* Changement ici */
        padding-left: 15px;
        margin-bottom: 20px; text-transform: uppercase;
    }

    /* Style des sections de contenu */
    .content-section {
        padding: 40px 50px;
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
        <p class="hero-top-text">ENTREPRISE PRIVÉE — DAKAR, SÉNÉGAL</p>
        <h1 class="hero-main-title">Gabou<br>Génie Civil</h1>
        <p class="hero-quote">NOUS BÂTISSONS VOS AMBITIONS</p>
        <p style="font-size: 18px; max-width: 600px; opacity: 0.9;">
            Études et réalisations en génie civil et VRD (Voirie et Réseau Divers). 
            Une expertise solide pour transformer vos visions en infrastructures durables.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION À PROPOS ---
st.markdown("<div id='a-propos' class='content-section'>", unsafe_allow_html=True)
st.header("À propos")
st.write("""
Gabou Génie Civil est une entreprise sénégalaise dédiée à l'excellence dans le secteur du bâtiment et des travaux publics. 
Basés à Guédiawaye, nous accompagnons nos clients de la conception à la réalisation de leurs projets.
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION NOS SERVICES ---
st.markdown("<div id='nos-services' class='content-section'>", unsafe_allow_html=True)
st.header("Nos Services")
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='color: #1A237E;'>🏗️ Génie Civil</h3>", unsafe_allow_html=True)
    st.write("Construction de bâtiments, gros œuvre et structures complexes.")
with col2:
    st.markdown("<h3 style='color: #1A237E;'>💧 VRD & Assainissement</h3>", unsafe_allow_html=True)
    st.write("Aménagement de voiries et gestion des réseaux de fluides.")
st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION CONTACT ---
st.divider()
st.markdown("<div id='contact' class='content-section'>", unsafe_allow_html=True)
st.subheader("Nous contacter")
st.write("📞 +221 77 058 33 45 | 📧 gabougc2026@gmail.com")
st.write("📍 Dakar, Sénégal")
st.markdown("</div>", unsafe_allow_html=True)

# Bouton WhatsApp flottant
st.markdown("""
    <div class="whatsapp-float">
        <a href="https://wa.me/221770583345" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60">
        </a>
    </div>
    """, unsafe_allow_html=True)
