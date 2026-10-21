# Contratos do cenário

## API existente

`GET /api/v1/recursos/svc-001` responde HTTP 200:

```json
{"id":"svc-001","nome":"Consulta de unidades","status":"ativo"}
```

| Consumidor | Campos necessários | Campos extras |
|---|---|---|
| A — portal | id, nome, status: strings não vazias | Tolera |
| B — integração legada | Exatamente id, nome, status: strings não vazias | Rejeita |
| C — novo painel | id, nome, status, unidade, responsavel: strings não vazias | Tolera |

Todos os campos desta tabela pertencem à RESPOSTA da API. O usuário da consulta informa o identificador; ele não preenche os campos do cadastro.

Um campo opcional pode estar ausente. Um campo anulável pode estar presente com `null`. São decisões diferentes. Para C, os dois campos novos são obrigatórios. Torná-los opcionais em uma especificação não fará o legado B passar a aceitá-los.

Não edite B para aceitar campos extras: ele representa um consumidor que está fora do alcance da sua entrega. Essa restrição permite avaliar compatibilidade de verdade.

## Ausência

Estado inicial conhecido: ID ausente retorna HTTP 200 e `{}`. O portal acusa resposta inválida.

Contrato da correção concorrente, a ser preservado:

```json
{"erro":{"codigo":"RECURSO_INEXISTENTE","id":"ausente"}}
```

Status HTTP: 404. Rotas desconhecidas têm outro erro, `ROTA_INEXISTENTE`. Não confunda rota inexistente com recurso inexistente em uma rota válida.

## Validar o novo consumidor

Após implementar, com o servidor reiniciado para carregar o código atualizado:

```sh
python -m consumidores.novo_consumidor --url "http://127.0.0.1:8080/SUA-INTERFACE/svc-001"
```

Substitua a URL pelo contrato escolhido. Esse comando não é esperado passar na base: não há endpoint pronto para C. Não coloque uma falha esperada de preparação como se fosse uma falha da entrega final.

A sonda é um smoke test; acrescente testes automatizados da interface que você escolher, cobrindo os demais IDs e ausência. Executar apenas a sonda de um ID não certifica toda a entrega.
