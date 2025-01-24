import random
import time

class Boulangerie:
    def __init__(self):
        self.argent = 1000
        self.inventaire = {
            'farine': 100,
            'levure': 50,
            'sel': 30,
            'eau': 100
        }
        self.produits = {}
        
    def fabriquer_pain(self):
        if (self.inventaire['farine'] >= 10 and 
            self.inventaire['levure'] >= 2 and 
            self.inventaire['sel'] >= 1 and 
            self.inventaire['eau'] >= 5):
            
            self.inventaire['farine'] -= 10
            self.inventaire['levure'] -= 2
            self.inventaire['sel'] -= 1
            self.inventaire['eau'] -= 5
            
            if 'pain' in self.produits:
                self.produits['pain'] += 1
            else:
                self.produits['pain'] = 1
            print("🥖 Pain fabriqué avec succès!")
        else:
            print("❌ Pas assez d'ingrédients!")

    def vendre(self):
        if self.produits.get('pain', 0) > 0:
            prix_vente = random.randint(3, 5)
            self.argent += prix_vente
            self.produits['pain'] -= 1
            print(f"💰 Pain vendu pour {prix_vente}€!")
        else:
            print("❌ Plus de pain en stock!")
            
    def acheter_ingredients(self):
        cout = 50
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
        print("\n=== STATUS BOULANGERIE ===")
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
    boulangerie = Boulangerie()
    
    while True:
        print("\nActions disponibles:")
        print("1. Fabriquer du pain")
        print("2. Vendre")
        print("3. Acheter des ingrédients")
        print("4. Voir le status")
        print("5. Quitter")
        
        choix = input("\nQue voulez-vous faire? (1-5): ")
        
        if choix == "1":
            boulangerie.fabriquer_pain()
        elif choix == "2":
            boulangerie.vendre()
        elif choix == "3":
            boulangerie.acheter_ingredients()
        elif choix == "4":
            boulangerie.afficher_status()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Option invalide!")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
