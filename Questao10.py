from Emprestimo import Emprestimo
from Pessoa import Pessoa


def pessoaEmprestimos():
    pessoa = Pessoa("Joaozinho")
    emprestimo = Emprestimo("Fone de Ouvido", "23/12/2020")
    pessoa.emprestimos.append(emprestimo)
    emprestimo = Emprestimo("Mouse", "21/12/2020")
    pessoa.emprestimos.append(emprestimo)

    for emprestimo in pessoa.emprestimos:
        print(f"Emprestimo do equipamento: {emprestimo.nomeEquipamento} com data de devolução para {emprestimo.dataDevolucao} ")

if __name__ == '__main__':
    pessoaEmprestimos()