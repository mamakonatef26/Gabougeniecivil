import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gabou Génie Civil", page_icon="🏗️", layout="wide")

# Couleurs personnalisées : Chocolat (#3D1F16) et Orange (#FF4B2B)
st.markdown(f"""
    <style>
    .stApp {{ background-color: #FFFFFF; }}
    .main-title {{ color: #3D1F16; font-size: 45px; font-weight: bold; text-align: center; margin-bottom: 0px; }}
    .sub-title {{ color: #FF4B2B; font-size: 22px; text-align: center; margin-bottom: 30px; font-style: italic; }}
    .service-card {{ 
        background-color: #3D1F16; padding: 25px; border-radius: 15px; 
        color: white; text-align: center; height: 250px; border-bottom: 5px solid #FF4B2B;
    }}
    .contact-box {{
        background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #3D1F16;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([1, 4])
with col1:
    # Affiche une icône de remplacement ou votre logo si le fichier est présent
    st.write("## 🏗️ GGC") 
with col2:
    st.markdown("<h1 class='main-title'>GABOU GÉNIE CIVIL</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Expertise technique & Solutions durables</p>", unsafe_allow_html=True)

st.divider()

# --- SERVICES ---
st.header("Nos Domaines d'Expertise")
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""<div class='service-card'>
    <h3>🚧 BTP & Gros Œuvre</h3>
    <p>Conception et construction de bâtiments solides répondant aux normes internationales de sécurité.</p>
    </div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""<div class='service-card'>
    <h3>💧 Assainissement & VRD</h3>
    <p>Spécialiste des réseaux d'évacuation, gestion des eaux et aménagement des voies de circulation.</p>
    </div>""", unsafe_allow_html=True)
with s3:
    st.markdown("""<div class='service-card'>
    <h3>📏 Bureau d'Études</h3>
    <p>Études techniques approfondies, topographie de précision et suivi rigoureux de vos chantiers.</p>
    </div>""", unsafe_allow_html=True)

st.write("") 

# --- SECTION CONTACT & INFOS ---
st.divider()
c1, c2 = st.columns(2)

with c1:
    st.subheader("📍 Coordonnées de l'entreprise")
    st.markdown(f"""
    <div class='contact-box'>
        <p><strong>📞 Téléphone :</strong> +221 33 814 48 30 / +221 77 058 33 45</p>
        <p><strong>📧 Email :</strong> gabougc2026@gmail.com</p>
        <p><strong>🏢 Siège :</strong> Dakar, Sénégal</p>
        <hr>
        <a href="https://maps.google.com/?q=Dakar" target="_blank" style="color: #FF4B2B; text-decoration: none; font-weight: bold;">
            📍 Voir la localisation sur Google Maps
        </a>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.subheader("🚀 Lancez votre projet")
    type_p = st.selectbox("Type de travaux", ["Construction", "Assainissement", "Étude technique", "Rénovation"])
    
    # Lien WhatsApp automatique
    num_wa = "221770583345" 
    msg = f"Bonjour Gabou Génie Civil, je vous contacte depuis votre site pour un projet de {type_p}."
    lien_wa = f"https://wa.me/{num_wa}?text={msg.replace(' ', '%20')}"
    
    st.markdown(f'''
        <a href="{lien_wa}" target="_blank">
            <button style="background-color: #FF4B2B; color: white; border: none; padding: 15px 25px; border-radius: 8px; cursor: pointer; width: 100%; font-size: 18px; font-weight: bold;">
                Discuter sur WhatsApp 💬
            </button>
        </a>
    ''', unsafe_allow_html=True)