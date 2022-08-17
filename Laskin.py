print("*" *30)
print("Tervetuloa laskin-ohjelmaan!")
print("*" *30)
print("")
kysymys = input("Laske yhteenlasku (y), miinuslasku (m) tai kertolasku (k).")
if kysymys == "y":
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    print(luku1+luku2)
elif kysymys == "m":
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    print(luku1-luku2)
elif kysymys == "k":
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    print(luku1*luku2)
    