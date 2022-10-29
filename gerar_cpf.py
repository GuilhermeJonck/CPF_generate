from random import randint

# def gera_cpf_valido():
def gera_cpf_valido():
    while True:
        cpf = [randint(0, 9) for _ in range(9)]
        if cpf != cpf[::-1]:
            break

    for _ in range(2):
        valor = sum([(len(cpf) + 1 - x) * v for x, v in enumerate(cpf)]) % 11
        cpf.append(11 - valor if valor > 1 else 0)
        valido = "".join(str(x) for x in cpf)

    return (f'{valido[:3]}.{valido[3:6]}.{valido[6:9]}-{valido[9:]}')