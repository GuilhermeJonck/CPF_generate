from gerar_cpf import gera_cpf_valido
from valida_cpf import validar


def main():

    choice = 0

    while choice != 3:

        print(
            """
           ## Gerador de CPF's ##

        [ 1 ] gerar CPF valido
        [ 2 ] validar CPF 
        [ 3 ] lista com CPF's
        \n"""
        )
        choice = int(input(" Escolha uma opção ==> "))

        if choice == 1:
            return print(gera_cpf_valido())

        elif choice == 2:
            cpf = input("Digite o CPF ==> ")
            return print(validar(cpf))

        elif choice == 3:
            qtd = int(input("Quantos CPF's ==> "))
            return print([gera_cpf_valido() for _ in range(qtd)])

        else:
            print("\nOpção inválida.Tente novamente")
    print("Fim do programa")


if __name__ == "__main__":
    main()
