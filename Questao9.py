
def calculadora():
    primeiroValor = float(input("Informe o primeiro valor"))
    segundoValor = float(input("Informe o segundo valor"))
    operacao = input("Qual a operação que deseja realizar (soma, subtração, multiplicação, divisão, resto divisão)").lower()
    if operacao not in list(['soma','subtração','multiplicação','divisão','resto divisão']):
        print("Operacao inválida")
        return calculadora()
    if operacao == "soma":
        return print(primeiroValor+segundoValor)
    elif operacao == "subtração":
        return print(primeiroValor-segundoValor)
    elif operacao == "multiplicação":
        return print(primeiroValor*segundoValor)
    elif operacao == "divisão":
        return print(primeiroValor/segundoValor)
    elif operacao == "resto divisão":
        return print(primeiroValor%segundoValor)

if __name__ == '__main__':
    calculadora()