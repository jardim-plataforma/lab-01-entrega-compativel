# Contratos do cenário

## API v1 — contrato legado

`GET /api/v1/recursos/svc-001` responde HTTP 200:

```json
{
  "id": "svc-001",
  "nome": "Consulta de unidades",
  "status": "ativo"
}
```

A API v1 mantém exatamente os três campos originais. A integração legada B depende desse formato e rejeita campos extras.

## API v2 — contrato ampliado

`GET /api/v2/recursos/svc-001` responde HTTP 200:

```json
{
  "id": "svc-001",
  "nome": "Consulta de unidades",
  "status": "ativo",
  "unidade": "Operações",
  "responsavel": "Equipe Aurora"
}
```

A API v2 mantém os três campos originais e acrescenta `unidade` e `responsavel`. Os cinco campos devem conter strings não vazias nos registros da massa de teste.

## Consumidores

| Consumidor | Interface utilizada | Contrato esperado |
|---|---|---|
| A — portal | API v2 | Os cinco campos |
| B — integração legada | API v1 | Exatamente os três campos originais |
| C — novo consumidor de teste | API v2 | Os cinco campos |

Os campos pertencem à resposta da API. O usuário da consulta informa o identificador do recurso; ele não preenche os campos do cadastro.

Não altere o consumidor B para aceitar campos extras: ele representa um sistema legado fora do alcance da entrega.

## Ausência de recurso

Quando a rota é válida, mas o identificador não existe, tanto a API v1 quanto a API v2 respondem HTTP 404 com este formato:

```json
{
  "erro": {
    "codigo": "RECURSO_INEXISTENTE",
    "id": "ausente"
  }
}
```

O valor de `erro.id` deve corresponder ao identificador solicitado.

Uma rota desconhecida tem outro erro, `ROTA_INEXISTENTE`. Não confunda uma rota inválida com um recurso inexistente em uma rota válida.

## Validar o novo consumidor

Com o servidor em execução, execute:

```sh
python -m consumidores.novo_consumidor --url "http://127.0.0.1:8080/api/v2/recursos/svc-001"
```

Para testar outro recurso, substitua `svc-001` pelo identificador desejado. A opção `--url` recebe a URL completa; isso também permite testar parâmetros de query string caso sejam adotados futuramente.

A sonda é um smoke test, não substitui a suíte automatizada. Os testes devem cobrir os registros existentes, os contratos v1 e v2 e a ausência de recursos por HTTP.

## Compatibilidade

A API v2 permite ampliar os dados entregues ao portal e ao novo consumidor sem adicionar campos à resposta estrita consumida por B. A existência de duas versões não garante compatibilidade por si só: as rotas, os formatos das respostas e os testes precisam continuar coerentes.