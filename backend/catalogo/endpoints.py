from .contratos import resposta_v1


def consultar_recurso(servico, identificador):
    registro = servico.consultar(identificador)
    if registro is None:
        # Correção da outra pessoa: ausência tem resposta explícita.
        return 404, {"erro": {"codigo": "RECURSO_INEXISTENTE", "id": identificador}}
    return 200, resposta_v1(registro)
