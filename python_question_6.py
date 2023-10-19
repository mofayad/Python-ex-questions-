txt=input("Taper des caractères:").lower().replace(" ", "").replace(",", "").replace(".", "")
if txt == txt[::-1]:
    print(f"La chaîne '{txt}' est un palindrome.")
else:
    print(f"La chaîne '{txt}' n'est pas un palindrome.")
