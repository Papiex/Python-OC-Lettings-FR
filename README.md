## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository.
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Papiex/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

L'application déployée avec heroku: `https://python-oc-lettings-672.herokuapp.com/`
Suivi des erreur avec Sentry (exemple) : `https://papiex.sentry.io/share/issue/cab01c21827944fab4842ae9df918239/`

Requis :
- Compte Heroku
- Heroku CLI `https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli`
- Compte Docker
- Docker Desktop `https://www.docker.com/products/docker-desktop/`
- Compte CircleCI
- Compte Sentry

- Se connecter à votre compte Heroku et DockerHub dans le shell à la racine du projet
(...\Python-OC-Lettings-FR>) avec ces commandes :
  - `heroku login`
  - `docker login`

- Créer un depôt Docker sur DockerHub
- Créer une application Heroku
- Créer un projet Sentry basé sur Django

### Lancement application en local via la création d'une image Docker :

- Démarrer DockerHub
- Lancer cette commande à la racine du projet `docker build -t python-oc-lettings-fr .`
- Lancer l'application avec cette commande : `docker run -p 8000:8000 image_que_vous_venez_de_créer`
- Rendez-vous sur `http://localhost:8000/` dans votre naviguateur pour accéder à l'application


### Déploiement sur heroku, docker de l'application via un pipeline CI/CD CIRCLECI :

Explication des étapes du déploiement :


__l'étape linter_and_tests sera effectué peu importe la branche, docker_deployment et heroku_deployment ne se lanceront que si l'on est sur la branche master__


- `linter_and_tests` lancera flake8 et pytest (cette étape sera effectué sur n'importe quelle branche)
- `docker_deployment` si l'étape linter_and_tests à réussi, une image de l'application sera déployée sur DockerHub
- `heroku_deployment` si le docker_deployment à réussi, l'application est déployée en ligne grâce à Heroku
Chaque étape se lance que si l'étape précédente à réussi.

Etapes pour effectuer un déploiement :
- Lié le repository de Github cloné avec votre compte CircleCI
- Ajouter la variable d'environnement SENTRY_DSN dans votre application Heroku
- Ajouter ces variables d'environnement dans le projet CIRCLECI:
  - DOCKERHUB_PASSWORD
  - DOCKERHUB_USERNAME
  - HEROKU_APP_NAME
  - HEROKU_TOKEN
  - SENTRY_DSN
- Ouvrer le fichier nommé `.env` dans la racine du projet puis modifier cette ligne à l'intérieur :
  - `SENTRY_DSN=votre_sentry_dsn_trouvable_dans_le_projet_sentry`
- Effectuer un commit vide ou pas puis faite un git push sur la branche master de votre repo cloné.
- Une fois l'application en ligne, vous pouvez créer une erreur pour vérifier que sentry est bien en place en vous rendant à cette adresse: `https://nom_application.herokuapp.com/sentry-debug/`



### Lancement application en local via la récupération d'une image Docker :

Lien repository Docker :
- Aller sur le dêpot Docker `https://hub.docker.com/r/papiex/python-oc-lettings-fr` (Choisir le tag de la dernière image déployée)
- Lancer cette commande `docker run -p 8000:8000 papiex/python-oc-lettings-fr:dernier_tag` (Si elle n'est pas trouvé en local, elle sera automatiquement récupérée sur DockerHub)
- Rendez-vous sur `http://localhost:8000/` dans votre naviguateur pour accéder à l'application
