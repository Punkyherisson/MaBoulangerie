🥖 Jeu de Gestion de Boulangerie
Un jeu de simulation textuel où vous gérez votre propre boulangerie pendant 7 jours avec des événements aléatoires quotidiens !

📋 Description
Gérez votre boulangerie, fabriquez du pain, vendez vos produits et achetez des ingrédients pour maximiser vos profits en 7 jours ! Attention aux événements aléatoires qui peuvent chambouler votre stratégie !

🎮 Comment jouer
Installation
Clonez ce projet
Lancez le jeu avec :
python main.py
Règles du jeu
Durée : 7 jours pour faire prospérer votre boulangerie
Actions : 5 actions disponibles par jour
Objectif : Maximiser votre argent à la fin des 7 jours
Événements : Chaque jour, un événement aléatoire peut se produire
Actions disponibles
Fabriquer du pain 🥖

Coût : 10 kg farine, 2 kg levure, 1 kg sel, 5 L eau
Production : 30 pains de 500g (≈15 kg de pain cuit)
Taux d'hydratation : 50%
Vendre 💰

Pain frais (0 jour) : 4-6€
Pain de 1 jour : 3-4€
Pain de 2 jours : 2€
⚠️ Les pains de 3+ jours sont jetés automatiquement
Acheter des ingrédients 📦

Coût : 20€ (10€ pendant la promotion)
Vous recevez : 25 kg farine, 5 kg levure, 3 kg sel, 20 L eau
Voir le statut 📊

Affiche vos ressources, produits et argent
Terminer la journée 🌙

Tous les pains vieillissent d'un jour
Les pains de 3+ jours sont automatiquement jetés
⏰ Système de conservation
Jour 0 (pain frais) : Prix maximum (4-6€)
Jour 1 : Prix moyen (3-4€)
Jour 2 : Prix réduit (2€)
Jour 3+ : Pain dur, jeté automatiquement 🗑️
💡 Astuce : Gérez bien votre production pour éviter le gaspillage !

Ressources de départ
💶 Argent : 1000€
🌾 Farine : 50 kg
🧪 Levure : 10 kg
🧂 Sel : 5 kg
💧 Eau : 50 L
🎲 Événements aléatoires
Chaque jour, un événement aléatoire peut se produire :

Événements Positifs 🎉
☀️ Jour ordinaire : Rien de spécial
💎 Clients Riches : Les clients paient le double du prix !
⭐ Critique Culinaire : Un critique vous donne un bonus de 100€
🎁 Livraison Gratuite : Vous recevez des ingrédients gratuits
🎊 Fête du Village : Les prix de vente augmentent de 50%
🏷️ Promotion Ingrédients : Les ingrédients coûtent -50% aujourd'hui
Événements Négatifs 😰
🐦 Attaque de Pigeons : Tous vos stocks de pain sont pillés !
🔫 Hold Up : Des bandits volent tout votre argent !
🔧 Panne de Four : Impossible de fabriquer du pain aujourd'hui
✊ Grève des Boulangers : Les clients n'achètent que la moitié des pains
👮 Inspecteur Sanitaire : Amende de 50€
🌧️ Journée Pluvieuse : Les prix de vente baissent de 1€
📊 Scores
Les scores sont sauvegardés automatiquement dans scores.txt à la fin de chaque partie.

🛠️ Développement
Prérequis
Python 3.11+
Structure du projet
.
├── main.py          # Code principal du jeu
├── scores.txt       # Fichier de sauvegarde des scores
├── README.md        # Ce fichier
└── LICENSE          # Licence MIT
📝 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

🎯 Conseils de stratégie
Surveillez vos stocks d'ingrédients
Les pains frais rapportent plus que les pains secs
Planifiez vos achats d'ingrédients pour éviter la pénurie
Utilisez toutes vos actions quotidiennes efficacement
Anticipez les événements négatifs en gardant des réserves
Profitez des événements positifs pour maximiser vos profits !
Bon jeu ! 🥖