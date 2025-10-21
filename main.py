
import random
import time

class Boulangerie:
    def __init__(self, nom="Boulangerie Emma"):
        self.nom = nom
        self.argent = 1000
        self.jour = 1
        self.actions_restantes = 5
        self.inventaire = {
            'farine': 50,  # kg
            'levure': 10,  # kg
            'sel': 5,      # kg
            'eau': 50      # kg (litres)
        }
        # Système de stockage par âge de pain (jour 0 = frais, jour 1-2 = vendable, jour 3+ = dur/jeté)
        self.pains_par_age = {
            0: 0,  # Pain frais (jour de fabrication)
            1: 0,  # Pain 1 jour
            2: 0,  # Pain 2 jours
            3: 0   # Pain dur (3 jours ou plus - à jeter)
        }
        self.evenement_jour = None
        self.four_en_panne = False
        self.promotion_ingredients = False
        
    def fabriquer_pain(self):
        if self.four_en_panne:
            print("❌ Le four est en panne! Impossible de fabriquer du pain aujourd'hui!")
            return
            
        if (self.inventaire['farine'] >= 10 and 
            self.inventaire['levure'] >= 2 and 
            self.inventaire['sel'] >= 1 and 
            self.inventaire['eau'] >= 5):
            
            self.inventaire['farine'] -= 10
            self.inventaire['levure'] -= 2
            self.inventaire['sel'] -= 1
            self.inventaire['eau'] -= 5
            
            self.pains_par_age[0] += 30
            print("🥖 30 Pains frais fabriqués avec succès!")
        else:
            print("❌ Pas assez d'ingrédients!")

    def vendre(self):
        total_pains_vendables = self.pains_par_age[0] + self.pains_par_age[1] + self.pains_par_age[2]
        if total_pains_vendables == 0:
            print("❌ Plus de pain vendable en stock!")
            return
        
        # Multiplicateur de prix selon l'événement
        multiplicateur_prix = 1.0
        bonus_prix = 0
        vente_reduite = False
        
        if self.evenement_jour == "clients_riches":
            multiplicateur_prix = 2.0
        elif self.evenement_jour == "fete_village":
            multiplicateur_prix = 1.5
        elif self.evenement_jour == "journee_pluvieuse":
            bonus_prix = -1
        elif self.evenement_jour == "greve_boulangers":
            vente_reduite = True
        
        pains_vendus_total = 0
        limite_vente = total_pains_vendables // 2 if vente_reduite else total_pains_vendables
        
        # Vendre d'abord les pains les plus vieux (jour 2)
        while self.pains_par_age[2] > 0 and pains_vendus_total < limite_vente:
            prix_base = 2  # Prix réduit pour pain de 2 jours
            prix = max(1, int(prix_base * multiplicateur_prix) + bonus_prix)
            self.argent += prix
            self.pains_par_age[2] -= 1
            pains_vendus_total += 1
            print(f"💰 Pain de 2 jours vendu pour {prix}€!")
        
        # Vendre ensuite les pains de 1 jour
        while self.pains_par_age[1] > 0 and pains_vendus_total < limite_vente:
            prix_base = random.randint(3, 4)  # Prix moyen pour pain de 1 jour
            prix = max(1, int(prix_base * multiplicateur_prix) + bonus_prix)
            self.argent += prix
            self.pains_par_age[1] -= 1
            pains_vendus_total += 1
            print(f"💰 Pain de 1 jour vendu pour {prix}€!")
            
        # Vendre enfin les pains frais (meilleur prix)
        while self.pains_par_age[0] > 0 and pains_vendus_total < limite_vente:
            prix_base = random.randint(4, 6)  # Meilleur prix pour pain frais
            prix = max(1, int(prix_base * multiplicateur_prix) + bonus_prix)
            self.argent += prix
            self.pains_par_age[0] -= 1
            pains_vendus_total += 1
            print(f"💰 Pain frais vendu pour {prix}€!")
        
        if vente_reduite and (self.pains_par_age[0] > 0 or self.pains_par_age[1] > 0 or self.pains_par_age[2] > 0):
            print("⚠️ Les clients n'achètent que la moitié des pains à cause de la grève!")
            
    def acheter_ingredients(self):
        cout = 20
        if self.promotion_ingredients:
            cout = 10
            print("🎉 Promotion active! -50% sur les ingrédients!")
            
        if self.argent >= cout:
            self.inventaire['farine'] += 25  # kg
            self.inventaire['levure'] += 5   # kg
            self.inventaire['sel'] += 3      # kg
            self.inventaire['eau'] += 20     # kg (litres)
            self.argent -= cout
            print(f"📦 Ingrédients achetés pour {cout}€")
        else:
            print("❌ Pas assez d'argent!")

    def declencher_evenement(self):
        evenements = [
            "jour_ordinaire",
            "attaque_pigeons",
            "clients_riches",
            "hold_up",
            "critique_culinaire",
            "panne_four",
            "livraison_gratuite",
            "fete_village",
            "greve_boulangers",
            "inspecteur_sanitaire",
            "promotion_ingredients",
            "journee_pluvieuse"
        ]
        
        self.evenement_jour = random.choice(evenements)
        self.four_en_panne = False
        self.promotion_ingredients = False
        
        print("\n" + "="*50)
        print("🎲 ÉVÉNEMENT DU JOUR 🎲")
        print("="*50)
        
        if self.evenement_jour == "jour_ordinaire":
            print("☀️ Jour ordinaire - Rien de spécial aujourd'hui")
            
        elif self.evenement_jour == "attaque_pigeons":
            print("🐦 ATTAQUE DE PIGEONS!")
            print("Les pigeons ont pillé tous vos stocks de pain!")
            self.pains_par_age[0] = 0
            self.pains_par_age[1] = 0
            self.pains_par_age[2] = 0
            self.pains_par_age[3] = 0
            
        elif self.evenement_jour == "clients_riches":
            print("💎 CLIENTS RICHES!")
            print("Des clients fortunés sont en ville - ils paient le double!")
            
        elif self.evenement_jour == "hold_up":
            print("🔫 HOLD UP!")
            print("Des bandits ont volé tout votre argent!")
            self.argent = 0
            
        elif self.evenement_jour == "critique_culinaire":
            print("⭐ CRITIQUE CULINAIRE!")
            print("Un critique a adoré votre pain! Bonus de 100€")
            self.argent += 100
            
        elif self.evenement_jour == "panne_four":
            print("🔧 PANNE DE FOUR!")
            print("Votre four est en panne - impossible de fabriquer du pain aujourd'hui")
            self.four_en_panne = True
            
        elif self.evenement_jour == "livraison_gratuite":
            print("🎁 LIVRAISON GRATUITE!")
            print("Un fournisseur vous offre des ingrédients!")
            self.inventaire['farine'] += 25  # kg
            self.inventaire['levure'] += 5   # kg
            self.inventaire['sel'] += 3      # kg
            self.inventaire['eau'] += 20     # kg (litres)
            
        elif self.evenement_jour == "fete_village":
            print("🎊 FÊTE DU VILLAGE!")
            print("C'est la fête! Les prix de vente sont augmentés de 50%")
            
        elif self.evenement_jour == "greve_boulangers":
            print("✊ GRÈVE DES BOULANGERS!")
            print("Les clients boycottent - ils n'achètent que la moitié des pains")
            
        elif self.evenement_jour == "inspecteur_sanitaire":
            print("👮 INSPECTEUR SANITAIRE!")
            print("Contrôle surprise! Amende de 50€")
            self.argent = max(0, self.argent - 50)
            
        elif self.evenement_jour == "promotion_ingredients":
            print("🏷️ PROMOTION SUR LES INGRÉDIENTS!")
            print("Le fournisseur fait -50% aujourd'hui!")
            self.promotion_ingredients = True
            
        elif self.evenement_jour == "journee_pluvieuse":
            print("🌧️ JOURNÉE PLUVIEUSE!")
            print("Peu de clients - les prix de vente baissent de 1€")
            
        print("="*50 + "\n")
        time.sleep(2)
    
    def vieillir_pains(self):
        """Vieillit tous les pains d'un jour et jette les pains de 3+ jours"""
        pains_jetes = self.pains_par_age[3]
        
        # Déplacer les pains vers la catégorie d'âge suivante
        self.pains_par_age[3] = self.pains_par_age[2]
        self.pains_par_age[2] = self.pains_par_age[1]
        self.pains_par_age[1] = self.pains_par_age[0]
        self.pains_par_age[0] = 0
        
        # Jeter les pains trop vieux
        if pains_jetes > 0:
            print(f"🗑️ {pains_jetes} pain(s) dur(s) jeté(s) (3+ jours)")
        self.pains_par_age[3] = 0
    
    def afficher_status(self):
        print(f"\n=== {self.nom} ===")
        print(f"📅 Jour: {self.jour}/7")
        print(f"🎯 Actions restantes aujourd'hui: {self.actions_restantes}")
        print(f"💶 Argent: {self.argent}€")
        print("\n📝 Inventaire:")
        for item, qte in self.inventaire.items():
            print(f"- {item}: {qte}")
        print("\n🥖 Stock de pains:")
        print(f"- Frais (0 jour): {self.pains_par_age[0]}")
        print(f"- 1 jour: {self.pains_par_age[1]}")
        print(f"- 2 jours: {self.pains_par_age[2]}")
        if self.pains_par_age[3] > 0:
            print(f"- Durs (à jeter): {self.pains_par_age[3]}")
        print("=======================\n")

def main():
    print("🥖 Bienvenue dans votre Boulangerie! 🥖")
    nom = input("Entrez le nom de votre boulangerie (ou appuyez sur Entrée pour garder 'Boulangerie Emma'): ")
    boulangerie = Boulangerie(nom) if nom else Boulangerie()
    
    print("\n📜 RÈGLES DU JEU:")
    print("- Vous avez 7 jours pour faire prospérer votre boulangerie")
    print("- Chaque jour, vous pouvez faire 5 actions")
    print("- Fabriquez du pain en utilisant vos ingrédients")
    print("- Les pains non vendus deviennent des pains secs le jour suivant")
    print("- Les pains secs se vendent 1€ l'unité")
    print("- Vendez votre pain pour gagner de l'argent")
    print("- Achetez des ingrédients quand vous en manquez")
    print("- Objectif: Avoir le plus d'argent possible à la fin des 7 jours!")
    
    input("\nAppuyez sur Entrée pour commencer...")
    
    while boulangerie.jour <= 7:
        # Déclencher un événement aléatoire au début de chaque jour
        if boulangerie.jour == 1:
            print(f"\n=== Jour {boulangerie.jour}/7 ===\n")
        boulangerie.declencher_evenement()
        
        while boulangerie.actions_restantes > 0:
            print("\n=== STATUT ACTUEL ===")
            print(f"📅 Jour: {boulangerie.jour}/7")
            print(f"🎯 Actions restantes: {boulangerie.actions_restantes}")
            print(f"💶 Argent: {boulangerie.argent}€")
            print("🥖 Stock de pains:")
            print(f"  - Frais (0 jour): {boulangerie.pains_par_age[0]}")
            print(f"  - 1 jour: {boulangerie.pains_par_age[1]}")
            print(f"  - 2 jours: {boulangerie.pains_par_age[2]}")
            if boulangerie.pains_par_age[3] > 0:
                print(f"  - Durs (à jeter): {boulangerie.pains_par_age[3]}")
            print("📦 Ingrédients:")
            for item, qte in boulangerie.inventaire.items():
                print(f"  - {item}: {qte}")
            print("====================")
            
            print("\nActions disponibles:")
            print("1. Fabriquer du pain")
            print("2. Vendre")
            print("3. Acheter des ingrédients")
            print("4. Voir le status")
            print("5. Terminer la journée")
            
            choix = input("\nQue voulez-vous faire? (1-5): ")
            
            if choix == "1":
                boulangerie.fabriquer_pain()
                boulangerie.actions_restantes -= 1
            elif choix == "2":
                boulangerie.vendre()
                boulangerie.actions_restantes -= 1
            elif choix == "3":
                boulangerie.acheter_ingredients()
                boulangerie.actions_restantes -= 1
            elif choix == "4":
                boulangerie.afficher_status()
            elif choix == "5":
                break
            else:
                print("Option invalide!")
            
            time.sleep(1)
        
        # Fin de journée : vieillir les pains
        print("\n🌙 Fin de la journée...")
        boulangerie.vieillir_pains()
        boulangerie.jour += 1
        boulangerie.actions_restantes = 5
        if boulangerie.jour <= 7:
            print(f"\n=== Début du jour {boulangerie.jour}/7 ===")
    
    score_final = boulangerie.argent - 1000
    print(f"\n🎮 Fin du jeu! Vous terminez avec {boulangerie.argent}€")
    print(f"Score final: {score_final}€")
    
    with open('scores.txt', 'a') as f:
        f.write(f"{boulangerie.nom}: {score_final}€\n")
    print("Score sauvegardé dans scores.txt!")

if __name__ == "__main__":
    main()
