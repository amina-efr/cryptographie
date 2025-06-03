message = input("Le message à crypter: ")
cle = int(input("La clé (nombre de décalage): "))


def chiffrer(message, cle):
    acrypter = message.upper()
    lg = len(acrypter)
    message = ""

    for i in range(lg):
        if acrypter[i] == ' ':
            message += ' '
        else:
            asc = ord(acrypter[i]) + cle
            message += chr(asc + 26 * ((asc < 65) - (asc > 90)))
    return message

chiffre = chiffrer(message, cle)
print("Message chiffré:", chiffre)


messagechiffre = input("Le message à décrypter: ")
cle = int(input("La clé (nombre de décalage): "))


def dechiffrer(messagechiffre, cle):
    lg = len(messagechiffre)
    messagedechiffre = ""

    for i in range(lg):
        if messagechiffre[i] == ' ':
            messagedechiffre += ' '
        else:
            asc = ord(messagechiffre[i]) - cle
            messagedechiffre += chr(asc + 26 * ((asc < 65) - (asc > 90)))
    return messagedechiffre

dechiffre = dechiffrer(messagechiffre, cle)
print("Message déchiffré:", dechiffre)
