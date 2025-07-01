# MonBotDiscord 🎮✨

Un petit bot Discord avec un panneau de configuration Flask pour gérer :
- Annonces
- Commandes de modération
- Messages automatiques
- Et plus encore !

## 🚀 Déploiement sur Railway ou Render

### ✅ Pré-requis
- Python 3.11 ou +
- Un token Discord (mets-le dans une variable d'environnement `TOKEN`)

### ✅ Structure du projet

MonBotDiscord/
├── bot.py # Ton bot principal
├── dashboard.py # (optionnel) Panneau Flask
├── requirements.txt # Dépendances
├── Procfile # Commande pour démarrer
├── .gitignore # Ignore les fichiers inutiles
└── README.md # Documentation


### ✅ Installer en local

```bash
# Crée un environnement virtuel
python -m venv venv

# Active l'environnement
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate

# Installe les dépendances
pip install -r requirements.txt

# Pour lancer le bot seul
python bot.py

# Pour lancer le dashboard Flask seul
python dashboard.py
