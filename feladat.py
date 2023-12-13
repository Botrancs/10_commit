lab_szam=input("Hány lábad van?")
kerdes=print("Biztos", lab_szam, "lábad van?")
if kerdes == "Igen" or "igen":
    print("Szerintem ez nem normális menj dokihoz")
helyes= True
kerdes_2=print("Legalább szereted a tejet?")
if kerdes_2 == "nem" or "Nem":
    helyes = False
while not helyes:
    ujra_proba=print("Na ezt próbáld meg mégegyszer.")
    if ujra_proba == "Igen" or "igen":
        helyes = True