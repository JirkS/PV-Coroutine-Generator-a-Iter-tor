def generatorSudychCisel(od, do):
    i = od
    while i < do:
        if i % 2 == 0:
            yield i
        i = i+1


if __name__ == "__main__":
    print("Suda cisla")
    for x in generatorSudychCisel(1, 57):
        print(x)
