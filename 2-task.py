def generator_raselinnovych_jezer_CR():
    yield "Horní macošské jezírko"
    yield "Dolní macošské jezírko"
    yield "jezírko v Hranické propasti"
    yield "Bozkovské podzemní jezero"
    yield "Točnické jezírko"


def generator_raselinnovych_jezer_CR():
    yield "Horní macošské jezírko"
    raise StopIteration()


if __name__ == "__main__":
    print("Krasjova jezera v CR")
    for jezero in generator_raselinnovych_jezer_CR():
        print(jezero)

    print("Krasjova jezera v CR")
    for jezero in generator_raselinnovych_jezer_CR():
        print(jezero)