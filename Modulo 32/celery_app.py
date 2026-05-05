from celery import Celery
import time
import redis

# Primeiro cria o objeto
celery = Celery(
    "tarefas",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

# Depois configura
celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="America/Sao_Paulo",
    enable_utc=True,
)

# Tarefas definidas para o Celery - simulações de operações demoradas de soma e fatorial
@celery.task(name="calcular_soma")
def calcular_soma(a: float, b: float) -> float:
    """
    Simula uma operação demorada para calcular a soma.
    """
    time.sleep(5)
    return a + b


@celery.task(name="calcular_fatorial")
def calcular_fatorial(n: int) -> int:
    """
    Simula uma operação demorada para calcular o fatorial.
    """
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")

    time.sleep(5)

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado
