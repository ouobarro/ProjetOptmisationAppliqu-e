# ProjetOptmisationAppliqu-e
Traitement et création de modèle permettant de constituer des groupes selon des contraintes spécifiques en utilisant le langage  Minizinc

# Consignes pour pouvoir exécuter notre projet
    1. Installer l'environnement de développement Python sur sa machine (il faut avoir python 3 sur sa machine)
        ->  mkdir -v TestProjetOptimisationAppliquee
        ->  cd TestProjetOptimisationAppliquee
        ->  sudo python3 -m venv ./optiEnvVirtuel
        ->  sudo chmod -R 777 optiEnvVirtuel
        ->  cd optiEnvVirtuel
        ->  git init
        ->  git clone <http:://le-lien-du-clone-sur-github>
        ->  source ./bin/activate
    2. Installer Minizinc pour python et pour votre système d'exploitation (Linux)
        ->  pip3 install minizinc
    3. Installer Django pour assurer le demarrage du serveur web
        ->  pip3 install django
    4. Installer l'IDE Pycharm Communtity (optionnel)
    5. Ouvrer un terminal et exécuter la commande suivante :
        -> python3 leCheminAbsoluVersLeFichier/optimisationAppliquee/manage.py runserver
    6. Vous verrez un message vous signalant que le serveur a demarré
    7. Cliquer sur le lien qui vous a été donné et vous serez rédiriger vers votre navigateur par défaut
    8. Vous pourrez enfin profiter de toutes les avantages de notre plateforme
