# Lab 01 · Entrega compatível

[Organização Jardim Plataforma](https://github.com/jardim-plataforma) · [Repositório](https://github.com/jardim-plataforma/lab-01-entrega-compativel)

Serviço fictício de consulta a um catálogo interno. Este repositório contém o backend, o portal web, a integração legada, dados locais e testes. A mudança para o novo consumidor ainda NÃO está implementada.

Leia [a demanda](ENUNCIADO.md), [a arquitetura](docs/arquitetura.md) e [os contratos](docs/contratos.md). A colaboração paralela está em [cenário Git](docs/cenario-git.md).

## Executar

Requisitos: Python 3.11 ou superior e Git. Não há pacotes externos para instalar. Execute os comandos na raiz do repositório. No Windows, use `py` no lugar de `python` se necessário.

```sh
python -m unittest discover -s tests -v
python -m backend.server
```

Abra http://127.0.0.1:8080. O portal consulta o backend do mesmo endereço. Em outro terminal, na mesma pasta:

```sh
python -m consumidores.verificar
```

Os dois consumidores devem aceitar `svc-001`. Encerre o servidor com Ctrl+C. Se a porta estiver ocupada, use `python -m backend.server --port 8081` e `python -m consumidores.verificar --base-url http://127.0.0.1:8081`.

## Onde procurar

| Pasta/arquivo | Responsabilidade |
|---|---|
| `backend/server.py` | Entrada HTTP, rotas e arquivos do frontend |
| `backend/catalogo/endpoints.py` | Resposta da consulta; região compartilhada pelas duas entregas |
| `backend/catalogo/contratos.py` | Formato público dos dados |
| `backend/catalogo/servico.py` | Camada de serviço |
| `backend/catalogo/repositorio.py` | Leitura dos registros |
| `backend/catalogo/dados.json` | Massa fictícia, somente leitura |
| `frontend/` | Portal consumidor A, HTML/CSS/JavaScript |
| `consumidores/` | Clientes e sonda do consumidor futuro |
| `tests/` | Contratos existentes e integração HTTP |
| `cenario/` | Correção concorrente ainda não aplicada |

## Limites deste ambiente

A estrutura separa responsabilidades como um projeto maior, mas usa servidor local da biblioteca padrão e JSON no lugar de banco. Não há autenticação, infraestrutura, deploy, Docker ou pipeline de execução fornecidos nesta etapa. Não é um backend de produção. A aprovação humana e as verificações no GitHub dependem da configuração do seu repositório; o template de PR não as impõe.

O defeito de recurso inexistente é intencional: hoje a consulta retorna HTTP 200 e `{}`. Os testes iniciais cobrem recursos existentes e não certificam esse comportamento incorreto. A outra entrega inclui o teste de regressão da ausência.

`VERSION` identifica a versão do software; `/api/v1` identifica o contrato HTTP. São coisas diferentes.
