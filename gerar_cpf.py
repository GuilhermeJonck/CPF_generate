from random import randint


cpf = [randint(0, 9) for _ in range(9)]

def dv1_bruto(cpf):

    return sum(((i + 2) * int(d) for i, d in enumerate(cpf[::-1])))


def digito1(cpf):

    resultado = dv1_bruto(cpf) * 10 % 11
    return resultado if resultado < 10 else 0


def dv2_bruto(cpf):

    return sum(((i + 3) * int(d) for i, d in enumerate(cpf[::-1])))


def digito2(cpf):

    resultado = (dv2_bruto(cpf) + digito1(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0


def cpf_valido():
    digito = str(digito1(cpf)) + str(digito2(cpf))
    cpf1 = "".join(str(x) for x in cpf)
    cpf_completo = "".join(cpf1+digito)
    return cpf_completo


def mascara(cpf_completo):
    return (
        f"{cpf_completo[:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:]}"
    )


