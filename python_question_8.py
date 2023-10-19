txt=input("Taper des caractères:").lower()
caractere = input("Entrez le caractère à compter:").lower()
occurrences = txt.count(caractere)
print(f"Le caractère '{caractere}' apparaît {occurrences} fois dans la chaîne.")
