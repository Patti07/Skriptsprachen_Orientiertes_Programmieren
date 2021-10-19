from Modul_Kreis import berechne_flaeche as flaeche, berechne_umfang as umfang

eingabe = float(input("Bitte den Radius eingeben: "))

print("Die Fläche beträgt: " + str(flaeche(eingabe)) + "\n")
print("Der Umfang beträgt: " + str(umfang(eingabe)))

