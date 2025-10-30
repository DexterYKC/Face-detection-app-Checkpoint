import numpy as np
import streamlit as st
from PIL import Image
import cv2, os
cascade_path = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(cascade_path)
assert not face_cascade.empty(), "Haar cascade introuvable"


st.title("Détection de visages")

st.markdown("""
### Instructions d'utilisation

1. Charge une **image** contenant un ou plusieurs visages.  
2. Choisis la **couleur** des rectangles autour des visages.  
3. Ajuste les paramètres :
   - **scaleFactor** (zoom de recherche, précision)
   - **minNeighbors** (filtrage des faux positifs)  
4. Clique sur **Détecter les visages**.  
5. Télécharge ensuite l image.
""")


uploaded_file = st.file_uploader("📤 Charge ton image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(image, caption="Image originale", use_container_width=True)

    rect_color = st.color_picker("🎨 Choisis la couleur du rectangle", "#00FF00")
    scale_factor = st.slider("⚙️ Ajuste scaleFactor", 1.01, 1.5, 1.1, 0.01)
    min_neighbors = st.slider("🔍 Ajuste minNeighbors", 1, 10, 5, 1)
    thickness = st.slider("📏 Épaisseur du rectangle", 1, 5, 2)
    if st.button("🚀 Détecter les visages"):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)

        st.write(f"✅ {len(faces)} visage(s) détecté(s)")

        hex_color = rect_color.lstrip('#')
        bgr_color = tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))

        for (x, y, w, h) in faces:
            cv2.rectangle(img_array, (x, y), (x + w, y + h), bgr_color, thickness)

        st.image(img_array, caption="Résultat", use_container_width=True)

        result_path = "faces_detected.jpg"
        cv2.imwrite(result_path, cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

        with open(result_path, "rb") as f:
            st.download_button(
                "⬇️ Télécharger l'image détectée",
                f,
                file_name="faces_detected.jpg",
                mime="image/jpeg"
            )
