## <p align='center'>Alexa sur Home-Assitant</p>

 ## I. Prérequis
### A. Création des compte
```
Un site web en HTTPS
```
Il faut obligatoirement que le site soit en HTTPS car amazon refuse de traiter avec un site non HTTPS , sinon ce réferer a : #Amettresolucepourskipca

```
Redirection 443
```
Il faut obligatoirement que le port externe 443 renvoie sur 8123 sur le port de votre box / routeur

```
Token Home-Assistant
```
Il faut un token pour Alexa , dans UserName>Sécurité>Crée un jeton
Donne un nom Alexa Test , puis conservez le précieusement

```
Configuration YAML
```
Ajouté : https://github.com/Jayas4/Home-Assistant-X-Alexa/blob/main/Code/configuration.yaml
En fonction de vos besoin rajouté des filtres ou des règles de Par-Feu
  
  ## II. Création des compte
### A. Création des compte

Crée du compte Aws Console avec n'importe quelle E-Mail sur le site : 
```
Le site Aws console nous servira a crée la fonction  et a éffectué des test avant le déployement
```
Crée du compte Alexa Devloppeur avec l'E-Mail de votre compte Alexa sur le site : https://developer.amazon.com/

```
Le site Alexa Devloppeur nous servira a crée la skill , gérer les url de connexion et l'implementer 
```
  ## II. Création des compte
### A. Création des compte

Crée du compte Aws Console avec n'importe quelle E-Mail sur le site : https://aws.amazon.com/fr/console/
```
Le site Aws console nous servira a crée la fonction lambda , et a éffectué des test avant le déployement
```
Crée du compte Alexa Devloppeur avec l'E-Mail de votre compte Alexa sur le site : https://developer.amazon.com/
```
Le site Alexa Devloppeur nous servira a crée la skill , gérer les url de connexion et l'implementer 
```

  ## III. Configuration
### A. Aws Console

Création
```
Création Fonction Lambda
Nom Home-Assitant
Execution Python 3.9
Architecture x86_64
Créer un nouveau rôle avec les autorisations Lambda de base
```
Intégré le contenu https://github.com/Jayas4/Home-Assistant-X-Alexa/blob/main/Code/lambda_fonction.py dans le code

Pour ma part a le token dans le code car impossible de le mettre dans les variables d'environement du a un bug encore inconnue

Ajouter l'url H-A FonctionH-A>Configuration>Variables D'environement

Ajouté BASE_URL , valeur url externe H-A 

### B. Test Aws Console

Test avec un JSON évènement 
```
FonctionH-A>Configuration>Variables D'environement
Nom d'évènement : Discovery
Contenu json :
Remplacer le token par son token H-A
Lancer le test
Voir les détails
Voir la réponse , normalement :
{
  "event": {
    "header": {
      "namespace": "Alexa.Discovery",
      "name": "Discover.Response",
      "messageId": "ID PERSONNEL",
      "payloadVersion": "3"
    },
    "payload": {
      "endpoints": [
        { et la suite pour les appareils découvert
```
Si des problèmes surviennent , ce réfèrer a : https://github.com/Jayas4/Home-Assistant-X-Alexa/blob/main/Code/debugs.yaml

### C. Alexa Devloppeur

#### A .Création d'une skill
```
Création d'une Skill
Nom Home-Assitant
Choisir votre Langue
Experience Smart Home
```
#### B .Configuration de Smart Home
⚠️Ne toucher a rien sauf a choses qui sont marqué ci dessous

Pour Smart Home
```
Aller sur https://aws.amazon.com/fr/console/
Choisir votre fonction H-A
Cliquer en haut a droite sur Coper  L'ARN
Puis coller ca dans Default endpoint*
Choisir votre région
Cliquez en suite en bas a droite sur Setup Account Linking
```

Setup Account Linking
```
Pour Authorization URI* entrez https://VOTREADRESSEHA/auth/authorize
PourToken URI entrez https://VOTREADRESSEHA/auth/token
Pour Votre Secret , entre n'importe quoi ,
Autentification shema doit être changer en Credential Request Body
Le scope doit être : smart_home
Pour Alexa Redirect , vous devez copier pour votre région
Et vous devez le mettre dans Your Client ID
```
  ## III. Final
  ### A .Application Amazon Alexa
```
Allez dans L'applciation Amazon Alexa , rendez vous dans Plus>Skills
Descendre tout en bas
Puis cliquer sur Vos Skills
Choisir Dev , puis cliquer sur votre skill crée , et activer la skills / lier le compte
```

Cela devrait vous demandez de vous connectez a votre compte Home Assistant , puis tout deviendra fonctionnel !

En cas de problème innatendu , vous pouvez me contactez par :

Mon serveur discord et @jaja21 : https://discord.gg/KWkbKbsRZK

Ou 

Par mp discord : jaja

 
