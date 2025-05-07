# fichier: app.py

import os
import platform
import time

def main():
    print("Bienvenue dans le conteneur Docker !")
    print(f"Système : {platform.system()}")
    print(f"Version : {platform.version()}")
    print(f"Nom d'hôte : {platform.node()}")
    print(f"Répertoire courant : {os.getcwd()}")

    # Boucle infinie pour garder le conteneur actif
    while True:
        print("Le conteneur fonctionne toujours...")
        time.sleep(10)

if __name__ == "__main__":
    main()