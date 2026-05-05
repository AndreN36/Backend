from celery_app import calcular_soma, calcular_fatorial


def test_calcular_soma_deve_retornar_resultado_correto():
    resultado = calcular_soma(10, 5)

    assert resultado == 15


def test_calcular_soma_com_numeros_decimais():
    resultado = calcular_soma(2.5, 3.5)

    assert resultado == 6.0


def test_calcular_fatorial_deve_retornar_resultado_correto():
    resultado = calcular_fatorial(5)

    assert resultado == 120


def test_calcular_fatorial_de_zero_deve_retornar_um():
    resultado = calcular_fatorial(0)

    assert resultado == 1


def test_calcular_fatorial_de_um_deve_retornar_um():
    resultado = calcular_fatorial(1)

    assert resultado == 1


def test_calcular_fatorial_numero_negativo_deve_gerar_erro():
    try:
        calcular_fatorial(-1)
        assert False
    except ValueError as erro:
        assert str(erro) == "O fatorial não é definido para números negativos."