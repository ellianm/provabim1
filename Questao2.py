def removeCaracteresPosicaoPar():
    listLetras = list(input("Informe uma palavra"))
    palavra = ""
    for letra in range(len(listLetras)):
        if (letra % 2):
            listLetras[letra] = ""
        else:
            palavra = palavra + listLetras[letra]
    print(palavra)

if __name__ == '__main__':
    removeCaracteresPosicaoPar()