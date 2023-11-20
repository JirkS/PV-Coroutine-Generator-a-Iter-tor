def catch_lunch():
    menu = [
         "vitamínový nápoj",
         "polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko",
    ]
    yield [menu[0]]
    yield [menu[1], menu[2], menu[3]]


try:
    corutina1 = catch_lunch()

    napoje = next(corutina1)
    print(napoje)
    jidla = next(corutina1)
    print(jidla)
except Exception as e:
    print(e)