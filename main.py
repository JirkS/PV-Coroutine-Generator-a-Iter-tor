def generatorKrasovychJezerCR():
    yield "Horní macošské jezírko"  # krasove
    yield "Dolní macošské jezírko"  # krasove
    yield "jezírko v Hranické propasti"  # krasove
    yield "Bozkovské podzemní jezero"  # jezerni dom
    yield "Točnické jezírko"  #
    raise StopIteration()


print("Krasjova jezera v CR")
for jezero in generatorKrasovychJezerCR():
    print(jezero)
