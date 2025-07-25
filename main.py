
import time
from boulangerie import Boulangerie

def main():
    print("🥖 Bienvenue dans votre Boulangerie! 🥖")
    nom = input("Entrez le nom de votre boulangerie (ou appuyez sur Entrée pour garder 'MaBoulangerie'): ")
    boulangerie = Boulangerie(nom) if nom else Boulangerie()

    print("\n📜 RÈGLES DU JEU SIMPLIFIÉES:")
    print("- Le jeu dure 7 jours.")
    print("- Chaque jour, vous avez droit à 4 actions.")
    print("- Vous pouvez fabriquer jusqu'à 100 pains et 100 viennoiseries par jour.")
    print("- Chaque pain coûte 1€, chaque viennoiserie coûte 2€ à fabriquer.")
    print("- Les produits deviennent secs après 1 jour et ne valent plus qu'1€.")
    print("- Essayez de maximiser vos revenus !")
    input("\nAppuyez sur Entrée pour commencer...")

    while boulangerie.jour <= 7:
        while boulangerie.actions_restantes > 0:
            boulangerie.afficher_status()
            print("\nActions disponibles:")
            print("1. Fabriquer des pains")
            print("2. Fabriquer des viennoiseries")
            print("3. Vendre les produits")
            print("4. Terminer la journée")

            choix = input("\nQue voulez-vous faire ? (1-4): ").strip()
            if choix == "1":
                boulangerie.fabriquer_produits("pain")
            elif choix == "2":
                boulangerie.fabriquer_produits("viennoiserie")
            elif choix == "3":
                boulangerie.vendre_produits()
            elif choix == "4":
                break
            else:
                print("❌ Choix invalide.")
            time.sleep(1)

        boulangerie.fin_de_journee()

    print(f"\n🎉 Fin du jeu ! Vous avez terminé avec {boulangerie.argent}€. Bravo !")

if __name__ == "__main__":
    main()
