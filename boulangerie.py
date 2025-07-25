
class Boulangerie:
    def __init__(self, nom="MaBoulangerie"):
        self.nom = nom
        self.jour = 1
        self.actions_restantes = 4
        self.argent = 1000
        self.produits_frais = {"pain": 0, "viennoiserie": 0}
        self.produits_secs = {"pain": 0, "viennoiserie": 0}

    def afficher_status(self):
        print(f"\n=== {self.nom} ===")
        print(f"📅 Jour: {self.jour}/7")
        print(f"🎯 Actions restantes: {self.actions_restantes}")
        print(f"💶 Argent: {self.argent}€")
        print(f"🥖 Pains frais: {self.produits_frais['pain']}")
        print(f"🥐 Viennoiseries fraîches: {self.produits_frais['viennoiserie']}")
        print(f"🥖 Pains secs: {self.produits_secs['pain']}")
        print(f"🥐 Viennoiseries sèches: {self.produits_secs['viennoiserie']}")

    def fabriquer_produits(self, type_produit):
        try:
            quantite = int(input(f"Combien de {type_produit}s voulez-vous fabriquer ? (max 100): "))
        except ValueError:
            print("❌ Entrée invalide.")
            return

        if quantite < 1 or quantite > 100:
            print("❌ Quantité invalide.")
            return

        cout = quantite * (1 if type_produit == "pain" else 2)
        if self.argent < cout:
            print("❌ Fonds insuffisants.")
            return

        self.argent -= cout
        self.produits_frais[type_produit] += quantite
        self.actions_restantes -= 1
        print(f"✅ {quantite} {type_produit}s fabriqués.")

    def vendre_produits(self):
        total = 0

        for produit in ["pain", "viennoiserie"]:
            frais = self.produits_frais[produit]
            secs = self.produits_secs[produit]
            gain = frais * (4 if produit == "pain" else 5)
            gain += secs * 1
            total += gain
            self.produits_frais[produit] = 0
            self.produits_secs[produit] = 0

        self.argent += total
        self.actions_restantes -= 1
        print(f"💰 Vous avez gagné {total}€ en vendant tous vos produits.")

    def fin_de_journee(self):
        for produit in self.produits_frais:
            self.produits_secs[produit] += self.produits_frais[produit]
            self.produits_frais[produit] = 0
        self.jour += 1
        if self.jour <= 7:
            print(f"\n🌅 Nouveau jour: {self.jour}/7")
        self.actions_restantes = 4
