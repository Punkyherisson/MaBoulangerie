
import random
import time

class Boulangerie:
    def __init__(self, nom="Boulangerie Emma"):
        self.nom = nom
        self.argent = 1000
        self.jour = 1
        self.actions_restantes = 5
        self.inventaire = {
            'farine': 100,
            'levure': 50,
            'sel': 30,
            'eau': 100
        }
        self.produits = {
            'pain_frais': 0,
            'pain_sec': 0
        }
        
    def fabriquer_pain(self):
        if (self.inventaire['farine'] >= 10 and 
            self.inventaire['levure'] >= 2 and 
            self.inventaire['sel'] >= 1 and 
            self.inventaire['eau'] >= 5):
            
            self.inventaire['farine'] -= 10
            self.inventaire['levure'] -= 2
            self.inventaire['sel'] -= 1
            self.inventaire['eau'] -= 5
            
            self.produits['pain_frais'] += 2
            print("🥖 2 Pains fabriqués avec succès!")
        else:
            print("❌ Pas assez d'ingrédients!")

    def vendre(self):
        ventes = 0
        while ventes < 2:
            if self.produits['pain_sec'] > 0:
                self.argent += 1
                self.produits['pain_sec'] -= 1
                print("💰 Pain sec vendu pour 1€!")
                ventes += 1
            elif self.produits['pain_frais'] > 0:
                prix_vente = random.randint(3, 5)
                self.argent += prix_vente
                self.produits['pain_frais'] -= 1
                print(f"💰 Pain frais vendu pour {prix_vente}€!")
                ventes += 1
            else:
                if ventes == 0:
                    print("❌ Plus de pain en stock!")
                return
            
    def acheter_ingredients(self):
        cout = 20
        if self.argent >= cout:
            self.inventaire['farine'] += 50
            self.inventaire['levure'] += 20
            self.inventaire['sel'] += 10
            self.inventaire['eau'] += 40
            self.argent -= cout
            print(f"📦 Ingrédients achetés pour {cout}€")
        else:
            print("❌ Pas assez d'argent!")

    def afficher_status(self):
        print(f"\n=== {self.nom} ===")
        print(f"📅 Jour: {self.jour}/7")
        print(f"🎯 Actions restantes aujourd'hui: {self.actions_restantes}")
        print(f"💶 Argent: {self.argent}€")
        print("\n📝 Inventaire:")
        for item, qte in self.inventaire.items():
            print(f"- {item}: {qte}")
        print("\n🥖 Produits:")
        for prod, qte in self.produits.items():
            print(f"- {prod}: {qte}")
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
        while boulangerie.actions_restantes > 0:
            print("\n=== STATUT ACTUEL ===")
            print(f"📅 Jour: {boulangerie.jour}/7")
            print(f"🎯 Actions restantes: {boulangerie.actions_restantes}")
            print(f"💶 Argent: {boulangerie.argent}€")
            print(f"🥖 Pains frais: {boulangerie.produits['pain_frais']}")
            print(f"🥖 Pains secs: {boulangerie.produits['pain_sec']}")
            print("📦 Ingrédients:")
            for item, qte in boulangerie.inventaire.items():
                print(f"- {item}: {qte}")
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
        
        # Fin de journée : les pains frais deviennent secs
        boulangerie.produits['pain_sec'] = boulangerie.produits['pain_frais']
        boulangerie.produits['pain_frais'] = 0
        boulangerie.jour += 1
        boulangerie.actions_restantes = 5
        if boulangerie.jour <= 7:
            print(f"\n=== Début du jour {boulangerie.jour} ===")
    
    print(f"\n🎮 Fin du jeu! Vous terminez avec {boulangerie.argent}€")

if __name__ == "__main__":
    main()
