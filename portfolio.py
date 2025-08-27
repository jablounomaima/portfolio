import streamlit as st
from PIL import Image

# --- Configuration de la page ---
st.set_page_config(page_title="Portfolio - Ingénieure Génie Logiciel", layout="wide")

# --- Image et titre ---
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("assets/photo.jpg")  # Mets ta photo ici
    st.image(image, width=180)
with col2:
    st.title("👩‍💻 Oumaima - Ingénieure en Génie Logiciel")
    st.write("Passionnée par le développement logiciel, la conception d’architectures web et la résolution de problèmes complexes.")

st.markdown("---")

# --- À propos ---
st.header("À propos de moi")
st.write("""
🎓 Diplôme : Master en Génie Logiciel  
💻 Spécialisée en **Python, Java, Spring Boot, Angular, Docker**  
🚀 Expérience dans le développement web, la gestion de bases de données et DevOps  
""")

st.markdown("---")

# --- Compétences ---
st.header("🛠️ Compétences")
skills = {
    "Langages": ["Python", "Java", "C#", "JavaScript"],
    "Frameworks": ["Spring Boot", "Django", "Angular", "React"],
    "Outils": ["Git", "Docker", "Linux", "MySQL", "PostgreSQL"]
}
for category, items in skills.items():
    st.subheader(category)
    st.write(", ".join(items))

st.markdown("---")

# --- Projets ---
st.header("📂 Projets")

st.subheader("📌 Application de gestion d’un foyer étudiant")
st.write("Développement d’une application web avec **Angular (frontend)** et **Spring Boot (backend)** permettant la gestion des chambres, paiements et résidents.")

st.subheader("📌 Site e-commerce Cravate.tn")
st.write("Plateforme de vente en ligne développée avec **Symfony et Docker** pour gérer le catalogue, le panier et les commandes.")

st.subheader("📌 Projet Open Source")
st.write("Participation à des projets sur **GitHub** liés à l’automatisation et aux API.")

st.markdown("---")

# --- Contact ---
st.header("📞 Contact")
st.write("📧 Email : oumaima@example.com")
st.write("[🔗 LinkedIn](https://www.linkedin.com)")
st.write("[🐙 GitHub](https://github.com/)")

# Bouton CV
with open("assets/cv.pdf", "rb") as pdf_file:
    st.download_button(
        label="📄 Télécharger mon CV",
        data=pdf_file,
        file_name="CV_Oumaima.pdf",
        mime="application/pdf"
    )
