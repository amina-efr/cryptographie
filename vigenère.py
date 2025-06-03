message = input("Message à chiffrer : ")
cle = input("La clé : ")

def chiffrer(message, cle):
    message = message.upper()
    cle = cle.upper()
    lg = len(message)
    chiffre = ""
    j = 0  

    for i in range(lg):
        if message[i] == ' ':
            chiffre += ' '
        else:
            dec = ord(cle[j % len(cle)]) - 65
            asc = ord(message[i]) + dec
            chiffre += chr(asc + 26 * ((asc < 65) - (asc > 90)))
            j += 1

    return chiffre

chiffre = chiffrer(message, cle)
print("Message chiffré :", chiffre)


messagechiffre = input("Message à déchiffrer : ")
cle = input("La clé : ")

def dechiffrer(messagechiffre, cle):
    messagechiffre = messagechiffre.upper()
    cle = cle.upper()
    lg = len(messagechiffre)
    dechiffre = ""
    j = 0  

    for i in range(lg):
        if messagechiffre[i] == ' ':
            dechiffre += ' '
        else:
            dec = ord(cle[j % len(cle)]) - 65
            asc = ord(messagechiffre[i]) - dec
            dechiffre += chr(asc + 26 * ((asc < 65) - (asc > 90)))
            j += 1

    return dechiffre

dechiffre = dechiffrer(messagechiffre, cle)
print("Message déchiffré :", dechiffre)
