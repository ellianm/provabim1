import re
def validaSenha():
    palavra = input("Informe uma senha")
    if re.search("[_@$]", palavra) and re.search("[0-9]", palavra):
        return print("Senha válida")
    else:
        return print("Senha inválida")

if __name__ == '__main__':
    validaSenha()