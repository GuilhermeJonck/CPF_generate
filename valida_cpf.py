def validar(cpf):

    cpf = [int(num) for num in cpf if num.isdigit()]

    if len(cpf) != 11:
        return False
    elif cpf == cpf[::-1]:
        return False
    for i in range(9, 11):
        valor = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[i]:
            return False
    return True
