def listaParaArquivo():
    listPalavras = []
    for i in range(10):
        listPalavras.append(input(f"Informe uma palavra ({i+1} de 10)") + '\n')
    arquivo = open("listapalavras.txt", "w+")
    arquivo.writelines(listPalavras)

if __name__ == '__main__':
    listaParaArquivo()