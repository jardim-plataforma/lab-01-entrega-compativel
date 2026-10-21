def resposta_v1(registro):
    """Contrato público existente; o armazenamento contém mais dados."""
    return {campo: registro[campo] for campo in ("id", "nome", "status")}
