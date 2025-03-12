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
Pour Your Web Authorization URI* entre https://VOTREADRESSEHA/auth/authorize
```











## I. Configuration après installation 
### A. Renomer la machines
```
- Paramètres
- Système
- Renomer
```
<p align="center"> <img src="https://www.anoopcnair.com/wp-content/uploads/2022/04/image-107-1.png" width="500" height="auto" /> </p>


### B. Installation des Logiciels Constructeur

#### I. Lenovo Bridge
Détecte automatiquement le type et le numéro de série de votre système

Configuration requise
```
Systèmes : IdeaPad , IdeaCentre , Lenovo , ThinkCentre , ThinkPad , ThinkStation , Yoga
Systèmes d'exploitation : Microsoft Windows 10, 11
Remarque : Windows 10 IoT (64 bits) n'est pas pris en charge.
Navigateurs : Google Chrome 40+, Microsoft Edge, Microsoft Internet Explorer 10+, Mozilla Firefox 37+
Autorisations suffisantes dans Windows pour installer des programmes
Cookies activés dans votre navigateur.
```

1. <a href="https://download.lenovo.com/lsbv4/LSBSetup.exe">Cliquez ici </a>  pour télécharger directement Lenovo Service Bridge ou accédez à http://pcsupport. lenovo .com et cliquez sur Détecter le produit (déplacez le pointeur de la souris sur PC et sélectionnez Détecter le produit ) pour afficher l'introduction, les conditions générales et l'option de téléchargement de Lenovo Service Bridge.
<p align="center"> <img src="https://download.lenovo.com/km/media/images/HT104055/detectproduct2024_20240620143503762.png" width="500" height="auto" /> </p>

2. Acceptez les conditions générales et cliquez sur Continuer . Après un moment, téléchargez le fichier d'installation Lenovo Service Bridge.
<p align="center"> <img src="https://download.lenovo.com/km/media/images/HT104055/lenovoservicebridge1_20230206172044639.png" width="500" height="auto" /> </p>
<p align="center"> <img src="https://download.lenovo.com/km/media/images/HT104055/Lenovoservicebridge2_20230206172128146.png" width="500" height="auto" /> </p>

3. Ouvrez le fichier téléchargé, LSBsetup.exe. Cliquez sur le bouton Suivant pour démarrer le processus d'installation.
<p align="center"> <img src="https://download.lenovo.com/km/media/images/HT104055/ht104055part1_20200311115427623.png" width="500" height="auto" /> </p>
<p align="center"> <img src="https://download.lenovo.com/km/media/images/HT104055/ht104055part2_20200311115510275.png" width="500" height="auto" /> </p>

4. Après le processus d'installation, Lenovo Service Bridge détectera la machine et dirigera vers la page d'assistance du produit concerné.
<p align="center"> <img src="https://download.lenovo.com/km/media/images/HT104055/ht104055part3_20200311120112494.png" width="500" height="auto" /> </p>

Remarque : un message d’erreur s’affiche si le produit détecté ne répond pas à la configuration système requise de Lenovo Service Bridge.

Si la fonction Détecter mon numéro de série ne vous dirige pas vers la page d'assistance du produit concerné ou se bloque pendant le processus, utilisez les instructions suivantes :

Cliquez ici pour désinstaller Lenovo Service Bridge en suivant les étapes fournies
Accédez à C:\Users\votre nom d'utilisateur\AppData\Local\Programs\ Lenovo
Supprimer ou supprimer le nom de fichier Lenovo Service Bridge
Réinstaller Lenovo Service Bridge
<p align="center"> <img src="https://download.lenovo.com/km/media/images/HT104055/ht104055part4_20200311121231292.png" width="500" height="auto" /> </p>

#### I. Lenovo System Update
System Update télécharge les mises à jour de données pour les logiciels, les pilotes et le BIOS à partir d'un serveur Lenovo directement via Internet sans nécessiter de connaissances spécifiques de l'utilisateur sur l'emplacement du package ou s'il est nécessaire au système cible.
https://support.lenovo.com/fr/fr/downloads/ds012808-lenovo-system-update-for-windows-10-7-32-bit-64-bit-desktop-notebook-workstation

Systèmes d’exploitation compatibles
```
Les systèmes d'exploitation suivants sont pris en charge :
Microsoft Windows 11
Microsoft Windows 10
Microsoft Windows 7
```
https://download.lenovo.com/pccbbs/thinkvantage_en/system_update_5.08.03.59.exe

## II. Débarassé de ce qui n'est pas utile
### A. Supprimer les application préinstaller 
#### A. Supprimer les application préinstaller avec un script

Installation : https://github.com/Sycnex/Windows10Debloater

```
- Téléchargez le fichier .zip sur la page principale de GitHub et extrayez le fichier .zip à l'emplacement souhaité
- Une fois extrait, ouvrez PowerShell (ou PowerShell ISE ) en tant qu'administrateur
- Activer l'exécution de PowerShell Set-ExecutionPolicy Unrestricted -Force
- À l'invite, accédez au répertoire dans lequel vous avez extrait les fichiers : par exemple :cd c:\temp
- Ensuite, pour exécuter l'un ou l'autre des scripts, entrez ce qui suit : par exemple -.\Windows10DebloaterGUI.ps1
```
#### B. Supprimer les application préinstaller avec PowerShell

```
- Clic droit menu Démarrer
- PowerShell (en admin)
- Liste application préinstaller : Get-AppxPackage | Select-object name
- Supprimer les application préinstaller : Get-AppxPackage *<nom package>* | Remove-AppxPackage
- Exemple de commande pour Hub et commentaires : Get-AppxPackage *Microsoft.WindowsFeedbackHub* | Remove-AppxPackage

```
Installation : <a href="https://download.lenovo.com/pccbbs/thinkvantage_en/system_update_5.08.03.59.exe">Cliquez ici </a>  pour télécharger directement Lenovo System update

Listes des application  qui peuvent être desinstaller

```
APPLICATIONS	                  COMMANDE
3D Builder	                    Get-AppxPackage *3dbuilder* | Remove-AppxPackage
Actualités                     	Get-AppxPackage *bingnews* | Remove-AppxPackage
Alarmes et Horloge	            Get-AppxPackage *windowsalarms* | Remove-AppxPackage
Calculatrice	                  Get-AppxPackage *windowscalculator* | Remove-AppxPackage
Calendrier et Mail	            Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage
Caméra	                        Get-AppxPackage *windowscamera* | Remove-AppxPackage
Cartes	                        Get-AppxPackage *windowsmaps* | Remove-AppxPackage
Contacts	                      Get-AppxPackage *people* | Remove-AppxPackage
Enregistreur vocal	            Get-AppxPackage *soundrecorder* | Remove-AppxPackage
Films & Séries TV 	            Get-AppxPackage *zunevideo* | Remove-AppxPackage
Finance	                        Get-AppxPackage *bingfinance* | Remove-AppxPackage
Get Started	                    Get-AppxPackage *getstarted* | Remove-AppxPackage
Groove Musique	                Get-AppxPackage *zunemusic* | Remove-AppxPackage
Hub et commentaires	            Get-AppxPackage *Microsoft.WindowsFeedbackHub* | Remove-AppxPackage
Impression 3D	                  Get-AppxPackage *Microsoft.Print3D* | Remove-AppxPackage
Jeux	                          Get-AppxPackage *Microsoft.GamingApp* | Remove-AppxPackage
Météo	                          Get-AppxPackage *bingweather* | Remove-AppxPackage
Microsoft Solitaire Collection	Get-AppxPackage *solitairecollection* | Remove-AppxPackage
Microsoft Wallet	              Get-AppxPackage *Microsoft.Wallet* | Remove-AppxPackage
Notepad	                        Get-AppxPackage *Microsoft.Notepad* | Remove-AppxPackage
Obtenir de l’aide	              Get-AppxPackage *Microsoft.GetHelp* | Remove-AppxPackage
Obtenir Office                	Get-AppxPackage *officehub* | Remove-AppxPackage
Obtenir Skype                  	Get-AppxPackage *skypeapp* | Remove-AppxPackage
OneDrive	                      Get-AppxPackage *Microsoft.OneDriveSync* | Remove-AppxPackage
OneNote                        	Get-AppxPackage *onenote* | Remove-AppxPackage
Outils de capture d’écran      	Get-AppxPackage *Microsoft.ScreenSketch* | Remove-AppxPackage
Paint                          	Get-AppxPackage *Microsoft.Paint* | Remove-AppxPackage
Pense Bêtes                    	Get-AppxPackage *Microsoft.MicrosoftStickyNotes* | Remove-AppxPackage
Phone Companion	                Get-AppxPackage *windowsphone* | Remove-AppxPackage
Photos	                        Get-AppxPackage *photos* | Remove-AppxPackage
PowerAutomate	                  Get-AppxPackage *Microsoft.PowerAutomateDesktop* | Remove-AppxPackage
Réalité virtuelle	              Get-AppxPackage *Microsoft.MixedReality.Portal* | Remove-AppxPackage
Scanners                      	Get-AppxPackage *Microsoft.WindowsScan* | Remove-AppxPackage
Skype                          	Get-AppxPackage *skypeapp* | Remove-AppxPackage
Sport                          	Get-AppxPackage *bingsports* | Remove-AppxPackage
Teams                          	Get-AppxPackage *MicrosoftTeams* | Remove-AppxPackage
Visionneurs 3D	                Get-AppxPackage *Microsoft.Microsoft3DViewer* | Remove-AppxPackage
Votre téléphone                	Get-AppxPackage Microsoft.YourPhone -AllUsers | Remove-AppxPackage
Windows Store	                  Get-AppxPackage *windowsstore* | Remove-AppxPackage
Xbox	                          Get-AppxPackage *xboxapp* | Remove-AppxPackage
Zune Music	                    Get-AppxPackage *Microsoft.ZuneMusic* | Remove-AppxPackage
Zune Vidéo	                    Get-AppxPackage *Microsoft.ZuneVideo* | Remove-AppxPackage
```

<p align="center"> <img src="https://www.lecoindunet.com/wp-content/uploads/2023/02/creer-dossier-powershell.png" width="500" height="auto" /> </p>

### A. Supprimer les services intuiles depuis powersehll

```
- Clic droit menu Démarrer
- PowerShell (en admin)
- Liste application préinstaller : Get-Service
- Supprimer les application services : Set-Service -Name "Nom du service" -StartupType Disabled -Status Stopped
```

Listes des Services qui peuvent être desinstaller : 
```
Nom du service	Description
Acquisition d’image Windows (WIA)
stisvc	Fournit des services d’acquisition d’images pour les scanneurs et les appareils photo.
 Désactivez si vous n’utilisez pas de scanner.
 sc config "stisvc" start= disabled

Assistance IP
iphlpsvc	Fournit une connectivité de tunnel à l’aide des technologies de transition IPv6 (6to4, ISATAP, Proxy de port et Teredo) et IP-HTTPS. Si ce service est arrêté, l’ordinateur ne disposera pas des avantages de la connectivité améliorée offerts par ces technologies.
 Désactivez si vous n’utilisez pas de connexion IPv6.
 sc config "iphlpsvc" start= disabled

Assistance NetBIOS sur TCP/IP
lmhosts	Prend en charge le service NetBIOS sur TCP/IP (NetBT) et la résolution de noms NetBIOS pour les clients présents sur le réseau, ce qui permet aux utilisateurs de partager des fichiers, d’imprimer et d’ouvrir des sessions sur le réseau. Si ce service est arrêté, ces fonctions risquent de ne pas être disponibles. Si ce service est désactivé, les services qui en dépendent explicitement ne pourront pas démarrer.
 Désactivez si votre PC ne fait pas partie d’un Groupe de travail.
 sc config "lmhosts" start= disabled

Carte à puce
SCardSvr	Gère l’accès aux cartes à puce lues par l’ordinateur.
 sc config "SCardSvr" start= disabled

Client de suivi de lien distribué
TrkWks	Conserve les liens entre des fichiers NTFS au sein d’un ordinateur ou d’un ensemble d’ordinateurs en réseau.
 Désactivez si vous n’utilisez pas les dossiers partagés.
 sc config "TrkWks" start= disabled

Configuration des services Bureau à distance
SessionEnv	Le service Configuration des services Bureau à distance (RDCS) est responsable de toutes les activités de maintenance de session et de configuration du Bureau à distance et des services Bureau à distance nécessitant un contexte SYSTEM. Il faut y inclure les dossiers temporaires par session, ainsi que les thèmes et certificats des services Bureau à distance.
 Désactivez si vous n’utilisez pas la fonctionnalité Bureau à distance.
 sc config "SessionEnv" start= disabled

Contrôle parental
WpcMonSvc	Applique le contrôle parental aux comptes enfant dans Windows. Si ce service est arrêté ou désactivé, le contrôle parental peut ne pas être appliqué.
 Désactivez si vous n’utilisez pas la fonctionnalité Contrôle parental.
 sc config "WpcMonSvc" start= disabled

Expériences des utilisateurs connectés et télémétrie
DiagTrack	Le service d’expériences des utilisateurs connectés et de télémétrie offre des fonctionnalités qui prennent en charge les expériences des utilisateurs connectés et in-app. En outre, ce service gère la collecte et la transmission des informations de diagnostic et d’utilisation en fonction des événements (afin d’améliorer l’expérience et la qualité de la plateforme Windows) lorsque les paramètres des options de confidentialité des diagnostics et de l’utilisation sont activés sous Commentaires & diagnostics.
 sc config "DiagTrack" start= disabled

Fichiers hors connexion
CscService	Le service Fichiers hors connexion effectue des activités de maintenance sur le cache Fichiers hors connexion, répond aux événements d’ouverture et de fermeture de session des utilisateurs, implémente les données internes de l’API public, et distribue aux utilisateurs intéressés les événements pertinents relatifs aux activités Fichiers hors connexion et aux modifications apportées en mémoire cache.
 Désactivez si vous n’utilisez pas les dossiers partagés.
 sc config "CscService" start= disabled

Gestionnaire des cartes téléchargées
MapsBroker	Service Windows pour l’accès des applications aux cartes téléchargées.
 sc config "MapsBroker" start= disabled

Gestionnaire des connexions automatiques d’accès à distance
RasAuto	Crée une connexion vers un réseau distant à chaque fois qu’un programme référence un nom ou une adresse DNS ou NetBIOS distant.
 sc config "RasAuto" start= disabled

Gestionnaire des connexions d’accès à distance
RasMan	Gère les connexions d’accès à distance et les connexions de réseau privé virtuel (VPN) entre cet ordinateur et Internet ou d’autres réseaux distants.
 sc config "RasMan" start= disabled

 

Gestionnaire d’authentification Xbox Live
XblAuthManager	Fournit des services d’authentification et d’autorisation pour interagir avec Xbox Live.
 sc config "XblAuthManager" start= disabled


Jeu sauvegardé sur Xbox Live
XblGameSave	Ce service synchronise les données enregistrées pour les jeux dont la sauvegarde sur Xbox Live est activée.
 sc config "XblGameSave" start= disabled

Netlogon
Netlogon	Maintient un canal sécurisé entre cet ordinateur et le contrôleur de domaine pour authentifier les utilisateurs et les services.
 Désactivez si votre PC n’est pas connecté à un contrôleur de domaine.
 sc config "Netlogon" start= disabled

Ouverture de session secondaire
seclogon	Permet le démarrage des processus sous d’autres informations d’identification.
 sc config "seclogon" start= disabled

Partage de connexion Internet (ICS)
SharedAccess	Assure la traduction d’adresses de réseau, l’adressage, les services de résolution de noms et/ou les services de prévention d’intrusion pour un réseau de petite entreprise ou un réseau domestique.
 Désactivez si vous ne partagez jamais votre connexion Internet.
 sc config "SharedAccess" start= disabled

Registre à distance
RemoteRegistry	Permet aux utilisateurs à distance de modifier les paramètres du Registre sur cet ordinateur.
 sc config "RemoteRegistry" start= disabled


Routage et accès distant
RemoteAccess	Offre aux entreprises des services de routage dans les environnements de réseau local ou étendu.
 sc config "RemoteAccess" start= disabled

Serveur de trame de la Caméra Windows
FrameServer	Permettre à plusieurs clients d’accéder aux trames vidéo des appareils photo.
 Désactivez si vous n’utilisez pas de webcam.
 sc config "FrameServer" start= disabled

Service AVCTP
BthAvctpSvc	Ceci est le service de protocole de transport de contrôle audio vidéo.
 Désactivez si vous n’utilisez pas de périphérique audio Bluetooth ou de casque sans-fil.
 sc config "BthAvctpSvc" start= disabled

Service Collecteur standard du concentrateur de diagnostic Microsoft
diagnosticshub.
standardcollector.
service	Service Collecteur standard du concentrateur de diagnostic. Lors de l’exécution, ce service collecte les événements ETW en temps réel et les traite.
 sc config "diagnosticshub.standardcollector.service" start= disabled

Service de biométrie Windows
WbioSrvc	Le service de biométrie Windows permet aux applications clientes de capturer, comparer, manipuler et stocker des données biométriques sans avoir directement accès au matériel ou aux échantillons. Le service est hébergé dans un processus SVCHOST privilégié.
 Désactivez si votre PC n’est pas équipé d’un lecteur d’empreintes.
 sc config "WbioSrvc" start= disabled

Service de chiffrement de lecteur BitLocker
BDESVC	BDESVC héberge le service de chiffrement de lecteur BitLocker. Le chiffrement de lecteur BitLocker fournit un démarrage sécurisé pour le système d’exploitation, ainsi qu’un chiffrement total du volume pour le système d’exploitation, les volumes fixes ou les volumes amovibles. Ce service permet à BitLocker d’inviter les utilisateurs à effectuer diverses actions liées aux volumes montés, et déverrouille les volumes automatiquement sans intervention de l’utilisateur. En outre, il stocke les informations de récupération dans Active Directory, s’il est disponible, et, si nécessaire, garantit que les certificats de récupération les plus récents sont utilisés.
 Désactivez si vous n’utilisez pas BitLocker.
 sc config "BDESVC" start= disabled

Service de démo du magasin
RetailDemo	Le service de démo du magasin contrôle l’activité du périphérique pendant que celui-ci est en mode démo.
 sc config "RetailDemo" start= disabled

Service de géolocalisation
lfsvc	Ce service surveille l’emplacement actuel du système et gère les limites géographiques (un emplacement géographique accompagné d’événements associés).
 sc config "lfsvc" start= disabled

Service de l’Assistant Compatibilité des programmes
PcaSvc	Ce service fournit une prise en charge de l’Assistant Compatibilité des programmes. Cet Assistant surveille les programmes installés et exécutés par l’utilisateur et détecte les problèmes de compatibilité connus.
 sc config "PcaSvc" start= disabled

Service de mise en réseau Xbox Live
XboxNetApiSvc	Ce service prend en charge l’interface de programmation d’application Windows.Networking.XboxLive.
 sc config "XboxNetApiSvc" start= disabled

Service de partage de ports Net.Tcp
NetTcpPortSharing	Fournit la possibilité de partager des ports TCP sur le protocole net.tcp.
 sc config "NetTcpPortSharing" start= disabled

Service de plateforme des appareils connectés
CDPSvc	Ce service est utilisé pour les scénarios plateforme d’appareils connectés.
 sc config "CDPSvc" start= disabled

Service de prise en charge Bluetooth
bthserv	Le service Bluetooth prend en charge la découverte et l’association d’appareils Bluetooth distants. L’arrêt ou la désactivation de ce service peut entraîner un dysfonctionnement des appareils Bluetooth déjà installés et peut empêcher la découverte et l’association de nouveaux appareils.
 Désactivez si vous n’utilisez pas de périphérique Bluetooth.
 sc config "bthserv" start= disabled

Service de rapport d’erreurs Windows
WerSvc	Autorise le signalement des erreurs lorsque des programmes cessent de fonctionner ou de répondre, ainsi que la fourniture de solutions existantes. Autorise également la génération de journaux pour les services de diagnostic et de réparation.
 sc config "WerSvc" start= disabled

Service de stratégie de diagnostic
DPS	Le service de stratégie de diagnostic permet la détection, le dépannage et la résolution de problèmes pour les composants de Windows. Si ce service est arrêté, les diagnostics ne fonctionnent plus.
 sc config "DPS" start= disabled


Service du clavier tactile et du volet d’écriture manuscrite
TabletInputService	Active les fonctionnalités de stylet et d’entrée manuscrite du clavier tactile et du volet d’écriture manuscrite.
 Désactivez si votre ordinateur n’est pas une tablette.
 sc config "TabletInputService" start= disabled

Service d’historique des fichiers
fhsvc	Protège les fichiers utilisateurs des pertes accidentelles en les copiant dans un emplacement de sauvegarde.
 Désactivez si vous n’utilisez pas la Sauvegarde Windows et la Restauration du système.
 sc config "fhsvc" start= disabled

Service d’énumération de périphériques de carte à puce
ScDeviceEnum	Crée des nœuds de périphériques logiciels pour tous les lecteurs de cartes à puce accessibles à une session donnée.
 sc config "ScDeviceEnum" start= disabled

Service Initiateur iSCSI de Microsoft
MSiSCSI	Gère les sessions iSCSI (Internet SCSI) à partir de cet ordinateur sur les périphériques cible iSCSI distants.
 sc config "MSiSCSI" start= disabled

Service Partage réseau du Lecteur Windows Media
WMPNetworkSvc	Partage les bibliothèques du Lecteur Windows Media avec des lecteurs réseau et des appareils multimédias qui utilisent le Plug-and-Play universel.
 sc config "WMPNetworkSvc" start= disabled

Service Point d’accès sans fil mobile Windows
icssvc	Permet de partager une connexion de données cellulaires avec un autre appareil.
 Désactivez si vous ne partagez pas de connexion cellulaire.
 sc config "icssvc" start= disabled

Service Pulsation Microsoft Hyper-V
vmicheartbeat	Surveille l‘état de cet ordinateur virtuel en émettant une pulsation à intervalles réguliers. Ce service vous permet d’identifier les ordinateurs virtuels en cours d’exécution qui ne répondent plus.
 sc config "vmicheartbeat" start= disabled

Service Routeur SMS Microsoft Windows
SmsRouter	Achemine les messages vers les clients appropriés sur la base de règles.
 sc config "SmsRouter" start= disabled

Service Synchronisation date/heure Microsoft Hyper-V
vmictimesync	Synchronise l’heure système de cet ordinateur virtuel avec l’heure système de l’ordinateur physique.
 sc config "vmictimesync" start= disabled

Service téléphonique
PhoneSvc	Gère l’état de téléphonie de l’appareil.
 sc config "PhoneSvc" start= disabled

Service Windows Insider
wisvc	Offre la prise en charge de l’infrastructure pour le programme Windows Insider. Ce service doit rester actif pour que le programme Windows Insider fonctionne.
 Désactivez si vous ne faites pas partie du programme Windows Insider.
 sc config "wisvc" start= disabled

Spouleur d’impression
Spooler	Ce service met en spoule les travaux d’impression et gère l’interaction avec l’imprimante.
 Désactivez si vous n’utilisez pas d’imprimante.
 sc config "Spooler" start= disabled

Stratégie de retrait de la carte à puce
SCPolicySvc	Autorise le système à être configuré pour verrouiller le Bureau de l’utilisateur au moment du retrait de la carte à puce.
 sc config "SCPolicySvc" start= disabled

Télécopie
Fax	Vous permet d’envoyer et de recevoir des télécopies, d’utiliser les ressources de télécopie disponibles sur cet ordinateur ou le réseau.
 sc config "Fax" start= disabled

Téléphonie
TapiSrv	Prend en charge l’interface TAPI (Telephony API) pour les programmes qui contrôlent les périphériques de téléphonie sur l’ordinateur local et, via le réseau local (LAN), sur les serveurs qui exécutent également le service.
 sc config "TapiSrv" start= disabled

WebClient
WebClient	Permet à un programme fonctionnant sous Windows de créer, modifier et accéder à des fichiers Internet.
 sc config "WebClient" start= disabled

Windows Search
WSearch	Fournit des fonctionnalités d’indexation de contenu, de mise en cache des propriétés, de résultats de recherche pour les fichiers, les messages électroniques et autres contenus.
 Désactivez si vous n’utilisez jamais la Recherche Windows (ou si vous utilisez un logiciel de recherche tiers).
 sc config "WSearch" start= disabled
```
## III. Installation des logiciels de travail 

Logiciel de base : https://ninite.com/chrome-filezilla-firefox-notepadplusplus-paint.net-putty-python-winrar-winscp/ninite.exe
```
- Chorm
- FireFox
- Notepad ++
- Paint
- Putty
- Python
- WinRar
- WinScp
```

Adobe Acrobate Reader : https://get.adobe.com/fr/reader/download?os=Windows+10&name=Reader+2024.004.20220+French+Windows%2864Bit%29&lang=fr&nativeOs=Windows+10&accepted=cr&declined=mss&preInstalled=&site=landing

IDE Arduino : https://downloads.arduino.cc/arduino-ide/nightly/arduino-ide_nightly-20241128_Windows_64bit.zip

Rasberry PI Imager : https://downloads.raspberrypi.org/imager/imager_1.8.5.exe
