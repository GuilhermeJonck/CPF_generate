def validar(numero):

    cpf = [int(num) for num in numero if num.isdigit()]

    if len(numero) != 11:
        return "CPF invalido"
    elif numero == numero[::-1]:
        return "CPF invalido"
    for i in range(9, 11):
        valor = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[i]:
            return False
    return True
