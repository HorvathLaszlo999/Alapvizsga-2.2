'''
Kedvenc filmjeink
A feladatban elkészítendő program bekéri három film címét, illetve percben kifejezett hosszát. 
Egy‑egy filmcím-filmhossz adatpár megadását követően a program a percben kifejezett időtartamot átszámolja órákra és pecekre – például a 61 percet 1 óra 1 percre. Az eredményt a film címével együtt kiírja.

Egészítse ki a megkapott óraperc() függvényt úgy, hogy az alkalmas legyen percben megadott időtartamot órában és percben visszaadni! A program többi részében használja az így kiegészített függvényt!

A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:.
-----
Add meg egy film címét! Indul a bakterház
Hány perces a film? 66
A(z) Indul a bakterház című film 1 óra 6 perc hosszú.
Add meg egy film címét! Ben-Hur
Hány perces a film? 224
A(z) Ben-Hur című film 3 óra 44 perc hosszú.
Add meg egy film címét! Bérlők
Hány perces a film? 1
A(z) Bérlők című film 0 óra 1 perc hosszú.
'''

def óraperc(ido):
    óra = ido % 60
    perc = ido // 60
    return str(óra) + ' óra ' + str(perc) + ' perc'

film = input("Add meg egy film címét! ")
hossza = int(input("Hány perces a film?"))
print(óraperc(hossza))