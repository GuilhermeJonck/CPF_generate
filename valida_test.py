from gerar_cpf import digito1, digito2, cpf_valido, mascara
from lista_cpf import lista_c
from valida_cpf import validar


def test_digito1():

    assert digito1("") == False
    assert digito1("123456789") == 0
    assert digito1("762912890") == 8
    assert digito1("000000000") == 0


def test_digito2():

    assert digito2("") == False
    assert digito2("123456789") == 9
    assert digito2("762912890") == 3
    assert digito2("00000000") == 0


def test_cpf_valido():

    assert validar("24130780379") == True
    assert validar("24130780379") == True
    assert validar("359.829.936-20") == True
    assert validar("288.047.287-36") == True
    assert validar("") == False


def teste_lista_cpf():

    assert len(lista_c(0)) == 0
    assert len(lista_c(5)) == 5
    assert len(lista_c(10)) == 10
    assert len(lista_c(100)) == 100


def test_cpf_mascara():

    assert validar(mascara(cpf_valido())) == True
