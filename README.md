## 0. Bases : Structure du Dockerfile
Exercice 0 : 
Ecrire un dockerfile pour exécuter du code java

## 🧱 1. Bases : Structure du Dockerfile
Exercice 1 :

Écris un Dockerfile minimal qui :

Utilise une image python:3.12-slim

Copie ton code source dans /app

Définit /app comme répertoire de travail

Exécute python app.py au démarrage

## 🧹 2. Bonnes pratiques : Caching, Clean, Layers
Exercice 2 :

Modifie l'exercice 1 pour :

Ajouter un fichier requirements.txt

Installer les dépendances Python avant de copier le code

Utiliser le moins de couches possible

Supprimer les caches ou fichiers temporaires si besoin

## 🔐 3. Sécurité et utilisateurs
Exercice 3 :

Modifie le Dockerfile pour :

Ne pas utiliser l’utilisateur root

Créer un utilisateur appuser

Lancer l’application avec cet utilisateur

## 🧪 4. Healthcheck
Exercice 4 :

Ajoute un HEALTHCHECK qui vérifie que l’API répond sur /health (port 8000).

## 🧼 5. Multi-stage builds (optimisation taille)
Exercice 5 :

Écris un Dockerfile multi-stage pour une application Go :

Étape 1 : construire le binaire

Étape 2 : copier uniquement le binaire dans une image scratch ou alpine

## 🐳 6. Variables d’environnement, Entrypoint, CMD
Exercice 6 :

Crée un Dockerfile qui :

Définit une variable d’environnement ENV APP_ENV=production

Utilise ENTRYPOINT pour lancer gunicorn

Accepte des arguments à l’exécution (CMD)

⚙️ 7. ARG et Build-time config
Exercice 7 :

Ajoute un ARG VERSION, utilisé pour spécifier une version d'un paquet à installer via apt ou pip.

🪛 8. Labels et Metadata
Exercice 8 :

Ajoute des LABEL avec les infos suivantes :

Auteur

Version

Description

💥 9. COPY vs ADD et fichiers Dockerignore
Exercice 9 :

Explique la différence entre COPY et ADD

Écris un .dockerignore pour ignorer .git, __pycache__, *.log

🔁 10. BONUS : Paramétrage dynamique (ARG + ENV)
Exercice 10 :

Rends le port d'écoute configurable :

Utilise ARG PORT

Passe sa valeur à ENV

Dans CMD, utilise $PORT

📦 Format final
Chaque exercice peut ensuite être validé en local avec :

bash
Copier
Modifier
docker build -t test .
docker run --rm -p 8000:8000 test
Et en observant :

Les couches (docker history)

L’utilisateur (docker exec whoami)

L’état (docker inspect --format '{{.State.Health.Status}}')

L’espace disque (docker image ls)