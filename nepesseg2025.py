import msvcrt
import math

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
    while True:
        telepulesek_szama = 0
        osszes_lakos = 0
        varos_lakossag = 0
        for telep in lakosok:
            if telep["megyekod"] == kod:
                telepulesek_szama += 1
                osszes_lakos += telep["ferfi"]
                osszes_lakos += telep["no"]
                if telep["tipus"] == "város" or telep["tipus"] == "vármegyei jogú város" or telep["tipus"] == "vármegye székhely" or telep["tipus"] == "fővárosi kerület":
                    varos_lakossag += telep["no"]
                    varos_lakossag += telep["ferfi"]
        osszes_lakos = f"{osszes_lakos:_}".replace("_", " ")
        telepulesek_szama = f"{telepulesek_szama:_}".replace("_", " ")
        varos_lakossag = f"{varos_lakossag:_}".replace("_", " ")
        print()
        if osszes_lakos != "0":
            print(f"A települések száma a megyében: {telepulesek_szama}db")
            print(f"Az összes lakos száma: {osszes_lakos}fő")

            if osszes_lakos == varos_lakossag:
                print("Csak városok találhatóak az adott területen.")
            else:
                print(f"Városokban lakók száma: {varos_lakossag}fő")
            print()
        else:
            print(f"{"\033[31m"}Nem található ilyen megyekód{"\033[0m"}")
        print("[1] Még egy kód beírása \n[2] Vissza a menübe \n[X] Kilépés")

        vissza = msvcrt.getch().decode("utf-8", errors="ignore")
        if vissza == "1":
            kod = input("Írja be a megye kódját: ").upper()
            print()
            continue
        elif vissza == "2":
            print()
            return
        elif vissza == "x" or vissza == "X":
            print("Kilépés...")
            return True


def lista_kiirasa(lista, oldal_elemek_szama=20):
    összes_elem = len(lista)

    összes_oldal = math.ceil(összes_elem / oldal_elemek_szama)
    aktualis_oldal = 1

    while True:
        start_i = (aktualis_oldal - 1) * oldal_elemek_szama
        end_i = start_i + oldal_elemek_szama
        oldal_elemei = lista[start_i:end_i]
        print(f"\n--- {aktualis_oldal}. oldal / {összes_oldal} (Elemek: {start_i + 1}-{min(end_i, összes_elem)}) ---")

        for i, elem in enumerate(oldal_elemei, start=start_i + 1):
            print(f"{str(f"{i}.").ljust(5)} {str(elem["telepules"]).ljust(20)} lakosok száma: {elem["lakosszam"]} fő")

        print("-" * 40)
        bemenet = input(f"Írj be egy oldalszámot (1-{összes_oldal}), vagy X-et a kilépéshez a főmenübe: ").strip().lower()
        if bemenet == 'x' or bemenet == "X":
            return
            
        if bemenet.isdigit():
            valasztott_oldal = int(bemenet)
            if 1 <= valasztott_oldal <= összes_oldal:
                aktualis_oldal = valasztott_oldal
            else:
                print(f"{"\033[31m"} Érvénytelen oldalszám, 1 és {összes_oldal} között adj meg számot.{"\033[0m"}")
        else:
            print(f"{"\033[31m"}Számot adj meg, vagy X-et a kilépéshez{"\033[0m"}!")


def telepules_adat_kozseg(lakosok):
    kozsegek = []
    for adat in lakosok:
        if adat["tipus"] == "község" or adat["tipus"] == "nagyközség":
            kozseg = {
                "telepules" : adat["telepules"],
                "lakosszam": adat["ferfi"] + adat["no"]
            }
            kozsegek.append(kozseg)
    if lista_kiirasa(kozsegek) == True:
        return True


def telepules_adat_varos(lakosok):
    varosok = []
    for adat in lakosok:
        if adat["tipus"] == "város" or adat["tipus"] == "vármegyei jogú város" or adat["tipus"] == "vármegye székhely" or adat["tipus"] == "fővárosi kerület":
            varos = {
                "telepules" : adat["telepules"],
                "lakosszam": adat["ferfi"] + adat["no"]
            }
            varosok.append(varos)
    if lista_kiirasa(varosok) == True:
        return True


def menu():
    print("Üdvözöljük a lakossági mutatón! Kérjük válasszon az alábbi opciók közül!: \n[1]: Megye adatai \n[2]: Település típusai \n[X]: Kilépés")
    while True:
        if msvcrt.kbhit():
            betu = msvcrt.getch().decode("utf-8", errors="ignore")
            if betu == "1":
                kod = input("Írja be a megye kódját(pl.: CSO = Csongrád-Csanád): ").upper()
                if megyeadat(kod, lakosok) == True:
                    break
                else:
                    print("Kérjük válasszon az alábbi opciók közül!: \n[1]: Megye adatai \n[2]: Település típusai \n[X]: Kilépés")
            elif betu == "2":
                print()
                print("Írja be a kívánt település típusának betűjelét!: \n[a]: Község \n[b]: Város")
                betu2 = msvcrt.getch().decode("utf-8", errors="ignore")
                if betu2 == "a":
                    telepules_adat_kozseg(lakosok)
                    print("Kérjük válasszon az alábbi opciók közül!: \n[1]: Megye adatai \n[2]: Település típusai \n[X]: Kilépés")
                if betu2 == "b":
                    telepules_adat_varos(lakosok)
                    print("Kérjük válasszon az alábbi opciók közül!: \n[1]: Megye adatai \n[2]: Település típusai \n[X]: Kilépés")
            elif betu == "x" or betu == "X":
                print("Kilépés...")
                break
            else:
                print(f"{"\033[31m"}Hibás bemenet! Nyomjon meg egy érvényes gombot.{"\033[0m"}")
                continue

menu()