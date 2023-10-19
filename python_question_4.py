chaine=input("Entrer la chaine principale:").lower()
sous_chaine=input("Entrer la sous chaine que vous recherchez:").lower()
position=chaine.find(sous_chaine)
if position != -1:
    print(f"La sous-chaîne '{sous_chaine}' se trouve à la position {position} dans la chaîne.")
else:
    print(f"La sous-chaîne '{sous_chaine}' n'a pas été trouvée dans la chaîne.")