def poistaDuplikaatit(lista):
    # luodaan uusi lista, johon talletetaan uniikit arvot
    uniikkiLista = []

    # käydään läpi alkiot annetussa listassa
    for alkio in lista:
        # jos alkioa ei ole vielä lisätty uniikkiListaan, lisätään se
        if alkio not in uniikkiLista:
            uniikkiLista.append(alkio)

    # palautetaan uniikki lista
    return uniikkiLista
    
# testataan
lista = [1, 1, 2, 3, 1, 5, 2, 4, 3]
uniikkiLista = poistaDuplikaatit(lista)
print(uniikkiLista)

nimilista = ["Petra", "Heidi", "Janne", "Petra", "Heidi", "Petra", "Petra"]
uniikkiNimilista = poistaDuplikaatit(nimilista)
print(uniikkiNimilista)