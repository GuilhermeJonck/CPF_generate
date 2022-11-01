from gerar_cpf import cpf_valido, mascara
from valida_cpf import validar
from lista_cpf import lista_c


def main():

    choice = 0

    while choice != 6:

        print(
            """
           ## Gerador de CPF's ##

        [ 1 ] gerar CPF valido (S/Mascara)
        [ 2 ] gerar CPF valido 
        [ 3 ] validar CPF 
        [ 4 ] lista com CPF's (S/Mascara)
        [ 5 ] lista com CPF's 
        \n"""
        )
        choice = int(input(" Escolha uma opção ==> "))

        if choice == 1:
            return print(cpf_valido())

        elif choice == 2:
            return print(mascara(cpf_valido()))

        elif choice == 3:
            cpf = input("Digite o CPF ==> ")
            return print(validar(cpf))

        elif choice == 4:
            qtd = int(input("Quantos CPF's ==> "))
            return print(lista_c(qtd))

        elif choice == 5:
            qtd = int(input("Quantos CPF's ==> "))
            return print([mascara(x) for _, x in enumerate(lista_c(qtd))])

        else:
            print("\nOpção inválida.Tente novamente")
    print("Fim do programa")


if __name__ == "__main__":
    main()
