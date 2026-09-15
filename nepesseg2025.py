import msvcrt

lakosok = []
with open("lakossag_2025.csv", "r", encoding="utf-8") as forras:
    forras.readline()
    for sor in forras:
        adatok = sor.strip().split(";")
        lakos = {
            "megyekod": adatok[0],
            "telepules": adatok[1],
            "tipus": adatok[2],
            "ferfi": int(adatok[3].replace(" ", "")),
            "no": int(adatok[4].replace(" ", ""))
        }
        lakosok.append(lakos)

def megyeadat(kod, lakosok):
    telepulesek_szama = 0
    osszes_lakos = 0
    varos_lakossag = 0
    for telep in lakosok:
        if telep["megyekod"] == kod:
            telepulesek_szama += 1
            osszes_lakos += telep["ferfi"]
            osszes_lakos += telep["no"]
            if telep["tipus"] == "város" or telep["tipus"] == "vármegyei jogú város" or telep["tipus"] == "vármegye székhely":
                varos_lakossag += telep["no"]
                varos_lakossag += telep["ferfi"]
    osszes_lakos = f"{osszes_lakos:_}".replace("_", " ")
    telepulesek_szama = f"{telepulesek_szama:_}".replace("_", " ")
    varos_lakossag = f"{varos_lakossag:_}".replace("_", " ")
    print()
    print(f"A települések száma a megyében: {telepulesek_szama}db")
    print(f"Az összes lakos száma: {osszes_lakos}fő")
    print(f"Városokban lakók száma: {varos_lakossag}fő")
    print()
    print("[1] Még egy kód beírása \n[2] Vissza a menübe \n[X] Kilépés")
    kilepes = False
    vissza = msvcrt.getch().decode("utf-8", errors="ignore")
    if vissza == "1":
        kod = input("Írja be a megye kódját: ").upper()
        print()
        megyeadat(kod, lakosok)
    elif vissza == "2":
        print()
        menu()
    elif vissza == "x" or vissza == "X":
        print("Kilépés...")
        kilepes = True
    return kilepes

def telepules_adat_kozseg(lakosok):
    kozsegek = []
    for kozseg in lakosok:
        if kozseg["tipus"] == "község" or kozseg["tipus"] == "nagyközség":
            kozsegek.append(kozseg["telepules"] ,kozseg["ferfi"] ,kozseg["no"])      
    print(kozsegek)

def telepules_adat_varos(lakosok):
    varos = []


def menu():
    print("[1]: Megye adatai \n[2]: Település típusai \n[X]: Kilépés")
    while True:
        if msvcrt.kbhit():
            betu = msvcrt.getch().decode("utf-8", errors="ignore")
            if betu == "1":
                kod = input("Írja be a megye kódját: ").upper()
                if megyeadat(kod, lakosok) == True:
                    break
            elif betu == "2":
                print()
                print("Írja be a kívánt település típusának betűjelét!: \n[a]: Község \n[b]: Város")
                betu2 = msvcrt.getch().decode("utf-8", errors="ignore")
                if betu2 == "a":
                    telepules_adat_kozseg(lakosok)
                if betu2 == "b":
                    telepules_adat_varos(lakosok)
            elif betu == "x" or betu == "X":
                print("Kilépés...")
                break
            else:
                print(f"{"\033[31m"}Hibás bemenet! Kilépés a főmenübe...{"\033[0m"}")
                menu()

menu()