from ast import Return



from  random import randrange

def gerar_cpf():
    cpf = [randrange(10) for _ in range(9)]

    for _ in range(2):
        valor = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - valor if valor > 1 else 0)

    return "".join(str(x) for x in cpf)

def lista_c(qtd):
   return[gerar_cpf() for x in range(qtd)]

