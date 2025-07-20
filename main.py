
import random
import time

class Boulangerie:
    def __init__(self, nom="Boulangerie Emma"):
        self.nom = nom
        self.argent = 1000
        self.jour = 1
        self.actions_restantes = 5
        self.inventaire={
            'farine': 100,
            'levure': 50,
            'sel': 30,
            'eau': 100,
            'beurre': 50,
            'sucre': 30,
            'chocolat': 20,
            'oeufs': 12,
            'raisins': 20
    }

        self.produits = {
            'pain_frais': 0,
            'pain_sec': 0,
            'croissant': 0,
            'pain_au_chocolat': 0,
            'brioche': 0,
            'pain_aux_raisins': 0
        }
        self.recettes = {
            'pain_frais': {'farine': 10, 'levure': 2, 'sel': 1, 'eau': 5},
            'croissant': {'farine': 12, 'beurre': 5, 'levure': 2},
            'pain_au_chocolat': {'farine': 12, 'beurre': 5, 'levure': 2, 'chocolat': 3},
            'brioche': {'farine': 15, 'beurre': 7, 'levure': 3, 'sucre': 5, 'oeufs': 2},
            'pain_aux_raisins': {'farine': 14, 'beurre': 6, 'levure': 2, 'sucre': 4, 'raisins': 5}
    }
        self.prix_vente = {
            'pain_frais': (3, 5),
            'pain_sec': (1, 1),
            'croissant': (4, 5),
            'pain_au_chocolat': (5, 6),
            'brioche': (4, 6),
            'pain_aux_raisins': (5, 7)
}
        
    def fabriquer_produit(self, nom_produit):
        if nom_produit not in self.recettes:
           print("❌ Produit inconnu.")
           return
    
        recette = self.recettes[nom_produit]
        if all(self.inventaire.get(ing, 0) >= qte for ing, qte in recette.items()):
            for ing, qte in recette.items():
                self.inventaire[ing] -= qte
            self.produits[nom_produit] += 2
            print(f"✅ 2 {nom_produit.replace('_', ' ').title()} fabriqués avec succès!")
        else:
            print(f"❌ Pas assez d'ingrédients pour {nom_produit.replace('_', ' ')}.")

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
        produits_ordres = sorted(self.prix_vente.items(), key=lambda x: x[1][1], reverse=True)

        while ventes < 2:
            produit_vendu = False
            for produit, (prix_min, prix_max) in produits_ordres:
                if self.produits.get(produit, 0) > 0:
                    prix = random.randint(prix_min, prix_max)
                    self.argent += prix
                    self.produits[produit] -= 1
                    nom_affiche = produit.replace("_", " ").title()
                    print(f"💰 {nom_affiche} vendu pour {prix}€!")
                    ventes += 1
                    produit_vendu = True
                    break  # Vendre un seul à la fois pour mieux répartir
            if not produit_vendu:
                if ventes == 0:
                    print("❌ Aucun produit à vendre.")
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
            print("🥐 Produits en stock :")
            for produit, quantite in boulangerie.produits.items():
                if quantite > 0:
                    nom_affiche = produit.replace("_", " ").title()
                    print(f"- {nom_affiche} : {quantite}")
            print("📦 Ingrédients:")
            for item, qte in boulangerie.inventaire.items():
                print(f"- {item}: {qte}")
            print("====================")
            
            print("\nActions disponibles:")
            print("1. Fabriquer un produit")
            print("2. Vendre")
            print("3. Acheter des ingrédients")
            print("4. Voir le status")
            print("5. Terminer la journée")
            
            choix = input("\nQue voulez-vous faire? (1-5): ")
            
            if choix == "1":
                print("\nProduits disponibles :")
                produits_disponibles = list(boulangerie.recettes.keys())
                for i, prod in enumerate(produits_disponibles, 1):
                    print(f"{i}. {prod.replace('_', ' ').title()}")
    
                selection = input("Quel produit voulez-vous fabriquer ? (nom ou numéro) : ").strip().lower()

                # Vérifier si c’est un chiffre
                if selection.isdigit():
                    index = int(selection) - 1
                    if 0 <= index < len(produits_disponibles):
                        produit_choisi = produits_disponibles[index]
                    else:
                        print("❌ Numéro invalide.")
                        continue
                else:
                    # Transformer 'pain au chocolat' → 'pain_au_chocolat'
                    produit_choisi = selection.replace(" ", "_")
                    if produit_choisi not in boulangerie.recettes:
                        print("❌ Produit inconnu.")
                        continue

                boulangerie.fabriquer_produit(produit_choisi)
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
