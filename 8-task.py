def catch_your_lunch():
    napoj = yield
    yield f"Dostanete: {napoj}"

    volba = yield
    yield f"Vybráno jídlo: {volba}"

    if volba == "A":
        jidlo = ["polévka česneková s bramborem", "segedínský guláš, houskové knedlíky", "jablko"]
    else:
        jidlo = ["polévka česneková s bramborem", "kaše s bramborem", "hruška"]

    yield f"Jídlo: {jidlo}"

    yield "Konec"


corutina1 = catch_your_lunch()   # nastartuje corutinu
print(next(corutina1))            # spusti prvni cast, dostanete nápoj
print(corutina1.send("vitamínový nápoj"))  # posle data (nápoj) a provede druhou část
print(corutina1.send("A"))        # posle data (volbu) a provede třetí část
print(next(corutina1))            # provede poslední část (vypíše jídlo)