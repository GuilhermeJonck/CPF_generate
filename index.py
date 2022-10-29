from gerar_cpf import gera_cpf_valido
from valida_cpf import validar


def main():
    choice = 0
    qtd = 0
    while choice != 3:
        print(
            """
        Gerador de CPF's
        [ 1 ] gerar CPF valido
        [ 2 ] validar CPF 
        [ 3 ] lista com CPF's
        [ 4 ] sair do programa"""
        )
        choice = int(input("Qual é sua opção ?\n"))
        if choice == 1:
            return print(gera_cpf_valido())
        elif choice == 2:
            cpf = input("digite o CPF ==> ")
            return print(validar(cpf))

        elif choice == 3:
            qtd = int(input("Quantos CPF's ==> "))
            return print([gera_cpf_valido() for x in range(qtd)])
        else:
            print("Opção inválida.Tente novamente")
    print("Fim do programa")


if __name__ == "__main__":
    main()
