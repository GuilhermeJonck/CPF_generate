from random import randint


while True:
    cpf = [randint(0, 9) for _ in range(9)]
    if cpf != cpf[::-1]:
        break


def dv1_bruto(cpf):
    """Calcula o DV1 do CPF"""

    return sum(((i + 2) * int(d) for i, d in enumerate(cpf[::-1])))


def dv1(cpf):
    """Calcula o DV1 do CPF"""

    resultado = dv1_bruto(cpf) * 10 % 11
    return resultado if resultado < 10 else 0


def dv2_bruto(cpf):
    """Calcula o DV2 do CPF"""

    return sum(((i + 3) * int(d) for i, d in enumerate(cpf[::-1])))


def dv2(cpf):
    """Calcula o DV2 do CPF"""

    resultado = (dv2_bruto(cpf) + dv1(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0

    """Calcula o DV final do CPF"""


digito = str(dv1(cpf)) + str(dv2(cpf))
cpf = "".join(str(x) for x in cpf)
# return f"{gerado[:3]}.{gerado[3:6]}.{gerado[6:9]}-{gerado[9:]}"
print(f"{cpf}{digito}")
