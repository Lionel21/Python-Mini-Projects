# TODO : afficher le message de bienvenue
print("Welcome to the tip calculator")

# TODO : calcul total de la facture
bill = float(input("What was the total bill?"))

# TODO : sélectionner le pourcentage de pourboire 
tip_choice = int(input("What percentage tip would you like to give? 10, 12 or 15?"))

# TODO : choisir le nombre de personnes qui partagent la facture
people_division = int(input("How many people to split the bill?"))

# TODO : effectuer l'ensemble des calculs
tip_as_percent = tip_choice / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_division = total_bill / people_division
final_amount = round(bill_division, 2)

# TODO : afficher le résultat final
print(f"Each person should pay: {final_amount}£")
