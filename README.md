# Détection de Visages
      https://face-detection-app-checkpoint-9dqgyzk4yfdcaynom4bbl5.streamlit.app/
## Objectif du projet
Ce projet consiste à créer une application **Streamlit** qui permet de **détecter les visages sur une image** grâce à l’algorithme **Viola–Jones**.  
L’utilisateur peut interagir avec l’application pour :
- Charger une image,
- Choisir la couleur des rectangles autour des visages,
- Régler les paramètres de détection (`scaleFactor`, `minNeighbors`, `épaisseur`),
- Sauvegarder et télécharger l’image finale

## ⚙️ Technologies utilisées
- **Python 3**
- **Streamlit**
- **OpenCV**
- **Pillow**
- **NumPy**


# Fonctionnalités principales

**Fonctionnalité** 
- Upload d'image: L’utilisateur peut charger une image (JPEG/PNG) contenant un ou plusieurs visages
- Choix de la couleur: L’utilisateur peut choisir la couleur des rectangles via un sélecteur
- Ajustement des paramètres: **scaleFactor**, **minNeighbors** et l’épaisseur du rectangle sont réglables avec des sliders
- Détection des visages: L’algorithme Viola–Jones (Haar Cascade) détecte les visages en temps réel
- Sauvegarde et téléchargement: L’utilisateur peut sauvegarder et télécharger l’image annotée sur son appareil

# Exemple d’utilisation

1. Charger une photo de groupe ou un portrait
2. Ajuster les paramètres selon les besoins
3. Cliquer sur "Détecter les visages"
4. Visualiser les résultats directement sur la page
5. Télécharger l’image annotée
