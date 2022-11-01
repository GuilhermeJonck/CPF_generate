def mascara(numero):

    cpf = [int(num) for num in numero if num.isdigit()]
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    else:
        return False
