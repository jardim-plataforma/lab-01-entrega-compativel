from .contratos import resposta_v1


def consultar_recurso(servico, identificador):
    registro = servico.consultar(identificador)
    if registro is None:
        # Defeito conhecido: ausência hoje se parece com sucesso.
        return 200, {}
    return 200, resposta_v1(registro)
