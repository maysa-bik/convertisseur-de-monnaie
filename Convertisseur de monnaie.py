from forex_python.converter import CurrencyRates

historique_conversions = []
devises_ajoutees = []

def sauvegarder_historique():
    with open("historique_conversions.txt", "w") as fichier:
        for conversion in historique_conversions:
            fichier.write(f"{conversion[0]} {conversion[1]} -> {conversion[3]:.2f} {conversion[2]}\n")

def enregistrer_conversion(depart, arrivee, montant, resultat):
    with open('historique_conversions.txt', 'a') as fichier:
        fichier.write(f"{depart} -> {arrivee} : {montant} -> {resultat:.2f}\n")

def ajouter_devise(devise_initiale):
    nouvelle_devise = input("Veuillez saisir le code de la nouvelle devise : ")
    if nouvelle_devise == devise_initiale:
        nouveau_taux = 1.0
    else:
        nouveau_taux = float(input(f"Veuillez saisir le taux de conversion de {devise_initiale} vers {nouvelle_devise} : "))
        # Vérifier que le taux de conversion est raisonnable
        while nouveau_taux < 0.01:
            print("Le taux de conversion doit être supérieur à 0.01.")
            nouveau_taux = float(input(f"Veuillez saisir le taux de conversion de {devise_initiale} vers {nouvelle_devise} : "))

    devises_ajoutees.append((nouvelle_devise, nouveau_taux))

def afficher_devises_preferees():
    print("Devises préférées :")
    for devise, taux in devises_ajoutees:
        print(f"{devise} - Taux : {taux}")    
def main():
    # Saisie des données de l'utilisateur
    valeur = float(input("Veuillez saisir la valeur à convertir : "))
    devise_initiale = input("Veuillez saisir la devise initiale : ")
    devise_souhaitee = input("Veuillez saisir la devise souhaitée : ")

    # Conversion de la valeur
    c = CurrencyRates()
    try:
        taux_de_change = c.get_rate(devise_initiale, devise_souhaitee)
    except:
        print("La conversion n'est pas possible pour les devises fournies.")
        return    
    valeur_convertie = valeur * taux_de_change

    # Sauvegarde de l'historique des conversions
    historique_conversions.append((valeur, devise_initiale, devise_souhaitee, valeur_convertie))
    

    # Affichage du résultat
    print(f"La valeur {valeur} {devise_initiale} correspond à {valeur_convertie:.2f} {devise_souhaitee}.")
    # Sauvegarder l'historique et l'afficher
    sauvegarder_historique()
    print("\nHistorique des conversions :")
    for conversion in historique_conversions:
        print(f"{conversion[0]} {conversion[1]} -> {conversion[3]:.2f} {conversion[2]}")

    # Option pour ajouter une devise
    ajouter_devise(devise_initiale)

    # Option pour afficher les devises préférées
    afficher_devises_preferees()    
if __name__ == "__main__":
    main()

