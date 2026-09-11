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

print("[1]: Megye adatai \n [2]: Település típusai \n [X]: Kilépés")
valasz = input("")

def megyeadat(kod, lakosok):
    telepulesek_szama = 0
    osszes_lakos = 0
    for telep in lakosok:
        if telep["megyekod"] == kod:
            telepulesek_szama += 1
    print(f"A települések száma a megyében: {telepulesek_szama}db")



while True:
    if valasz == "1":
        kod = input("Írja be a megye kódját: ").upper()
        megyeadat(kod, lakosok)
    elif valasz == "2":
        print("b")
        break
    elif valasz == "x" or valasz == "X":
        break
    else:
        print("Hibás bemenet")
        break