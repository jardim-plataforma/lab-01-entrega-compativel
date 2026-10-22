# Lab 01 · Entrega compatível

[Organização Jardim Plataforma](https://github.com/jardim-plataforma) · [Repositório](https://github.com/jardim-plataforma/lab-01-entrega-compativel)

Serviço fictício de consulta a um catálogo interno. Este repositório contém o backend, o portal web, a integração legada, os consumidores de teste, dados locais e testes automatizados.

O laboratório pratica evolução de contratos HTTP, compatibilidade entre consumidores, integração de mudanças concorrentes, testes e recuperação.

Leia a [demanda](ENUNCIADO.md), a [arquitetura](docs/arquitetura.md), os [contratos](docs/contratos.md) e o [cenário Git](docs/cenario-git.md).

## Executar

Requisitos: Python 3.11 ou superior e Git. Não há pacotes externos para instalar. Execute os comandos na raiz do repositório. No Windows, use `py` no lugar de `python` se necessário.

```sh
python -m unittest discover -s tests -v
python -m backend.server
```

Abra http://127.0.0.1:8080 para acessar o portal. O portal consulta a API v2 e exibe os cinco campos do recurso.

Em outro terminal, na mesma pasta, valide a integração legada:

```sh
python -m consumidores.verificar
```

Para validar o novo contrato, com o servidor em execução:

```sh
python -m consumidores.novo_consumidor --url "http://127.0.0.1:8080/api/v2/recursos/svc-001"
```

Os consumidores devem aceitar `svc-001`. Para conferir a resposta HTTP diretamente, consulte as rotas descritas em [Contratos](docs/contratos.md).

Encerre o servidor com Ctrl+C. Se a porta estiver ocupada, inicie-o com:

```sh
python -m backend.server --port 8081
```

Nesse caso, informe a nova porta aos consumidores:

```sh
python -m consumidores.verificar --base-url http://127.0.0.1:8081

python -m consumidores.novo_consumidor --url "http://127.0.0.1:8081/api/v2/recursos/svc-001"
```

## Onde procurar

| Pasta/arquivo | Responsabilidade |
|---|---|
| `backend/server.py` | Entrada HTTP, rotas e arquivos do frontend |
| `backend/catalogo/endpoints.py` | Consulta de recursos e tratamento de erros |
| `backend/catalogo/contratos.py` | Projeções públicas dos contratos v1 e v2 |
| `backend/catalogo/servico.py` | Camada de serviço |
| `backend/catalogo/repositorio.py` | Leitura dos registros |
| `backend/catalogo/dados.json` | Massa fictícia de dados |
| `frontend/` | Portal consumidor A |
| `consumidores/` | Integração legada e novo consumidor de teste |
| `tests/` | Testes de contrato, erros e integração HTTP |
| `cenario/` | Materiais para simular a correção concorrente |

## Limites deste ambiente

A estrutura separa responsabilidades como um projeto maior, mas utiliza servidor local da biblioteca padrão e JSON no lugar de banco. Não há autenticação, infraestrutura de produção, deploy, Docker ou pipeline de execução fornecidos nesta etapa. Não é um backend de produção.

A aprovação humana e as verificações no GitHub dependem da configuração do repositório; o template de PR não as impõe.

A API v1 mantém os três campos originais. A API v2 expõe cinco campos. As duas interfaces retornam HTTP 404 com erro estruturado para recursos inexistentes.

`VERSION` identifica a versão do software; `/api/v1` e `/api/v2` identificam versões do contrato HTTP. São coisas diferentes.