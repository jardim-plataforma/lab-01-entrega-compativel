# Resolução — Laboratório 01: Entrega compatível

## 1. Objetivo

Evoluir o contrato de consulta de recursos sem quebrar o consumidor legado, integrar uma correção concorrente para recursos inexistentes e verificar o resultado na branch `main-resolução`.

Repositório: https://github.com/jardim-plataforma/lab-01-entrega-compativel

Branch de integração utilizada: `main-resolução`

## 2. Como o trabalho foi organizado

O trabalho utilizou branches para separar mudanças com objetivos diferentes:

- `main`: mantida como referência original.
- `fix/recurso-inexistente`: usada para corrigir a resposta de consultas a recursos inexistentes.
- `feat/consulta-ampliada`: usada para evoluir o contrato da API e, posteriormente, atualizar o portal.
- `main-resolução`: usada para integrar as entregas revisadas.

A correção concorrente foi integrada antes da conclusão da evolução do contrato. Depois, a branch de funcionalidade incorporou as alterações necessárias para que as entregas coexistissem.

## 3. Correção de recursos inexistentes

Foi implementado o retorno HTTP 404 para recursos inexistentes, com um erro estruturado contendo:

- `erro.codigo`: `RECURSO_INEXISTENTE`;
- `erro.id`: identificador solicitado.

A correção foi desenvolvida na branch `fix/recurso-inexistente`, no commit `076cbc8`, e integrada à linha de resolução.

## 4. Evolução do contrato

A API passou a disponibilizar duas versões:

- **API v1:** mantém os campos `id`, `nome` e `status`, preservando o contrato legado.
- **API v2:** disponibiliza `id`, `nome`, `status`, `unidade` e `responsavel`.

O consumidor legado continua utilizando a v1 e validando os três campos esperados. O novo consumidor utiliza a v2 para receber os cinco campos.

A versão do contrato foi separada da implementação interna. Isso permite acrescentar a capacidade necessária ao novo consumidor sem exigir que o consumidor antigo passe a aceitar campos adicionais.

## 5. Atualização do portal e consumidores

O portal foi atualizado para consumir a API v2 e apresentar os cinco campos. A integração legada permaneceu vinculada à v1.

O novo consumidor também foi preparado para verificar a resposta ampliada. A decisão e os contratos foram registrados na documentação do projeto.

## 6. Histórico de integração

Os principais commits identificados no histórico são:

| Commit | Alteração |
|---|---|
| `076cbc8` | Correção do retorno 404 para recurso inexistente |
| `21680ea` | Integração da correção de recurso inexistente |
| `1ef4310` | Implementação do contrato ampliado na API v2 |
| `69c304e` | Atualização da documentação de contratos e arquitetura |
| `7bce56e` | Merge do PR #1 |
| `ae27169` | Atualização do portal para consumir a API v2 |
| `e46ab09` | Merge do PR #2 |

O PR #1 integrou a primeira etapa da evolução do contrato. Depois, a atualização do portal e dos testes foi enviada em uma nova proposta e integrada pelo PR #2.

## 7. Verificação final

Após atualizar a branch local `main-resolução` com o repositório remoto, executei:

```bash
python -m unittest discover -s tests -v
```

Resultado observado:

- 13 testes executados;
- todos os testes passaram;
- resultado final: `OK`.

O terminal apresentou um `ResourceWarning` relacionado ao fechamento de um `HTTPError` no teste de recurso inexistente. O aviso não impediu a aprovação da suíte, mas deve ser tratado como um ponto de melhoria.

Também verifiquei o histórico com:

```bash
git log --all --graph --decorate --oneline -30
```

E o estado do repositório com `git status`, que indicou árvore de trabalho limpa e branch `main-resolução` sincronizada com `origin/main-resolução`.

## 8. O que aprendi

### Compatibilidade é um contrato explícito

Adicionar campos a uma resposta pode afetar consumidores que validam sua estrutura estritamente. Por isso, a evolução do contrato precisa considerar como cada consumidor interpreta a resposta, e não apenas se o JSON continua válido.

### Versionamento permite evoluir sem forçar a migração de todos os consumidores

Manter a v1 para o legado e disponibilizar a v2 para o novo consumidor separa as necessidades dos dois contratos. A versão usada precisa estar clara na URL e na documentação.

### Ausência de conflito textual não garante ausência de conflito funcional

Duas branches podem alterar partes diferentes do código e ainda produzir incompatibilidades quando integradas. É necessário revisar a intenção de cada mudança e testar o comportamento conjunto.

### Testes precisam verificar o caminho real

Testar funções isoladas não é suficiente para validar uma API. Os testes HTTP ajudam a verificar o status, a estrutura da resposta e o comportamento que os consumidores realmente recebem.

### Integração não é implantação

Os merges colocaram as mudanças na branch de resolução. Isso não demonstra, por si só, um deploy em produção nem disponibilidade contínua do serviço.

## 9. Limitações e próximos passos

A verificação registrada demonstra que a suíte passou no estado integrado. O `ResourceWarning` permanece como melhoria técnica.

A recuperação de uma regressão deve ser demonstrada separadamente, com evidência da falha provocada, da ação de recuperação e da preservação da correção concorrente. O histórico disponível nesta resolução não é suficiente, por si só, para afirmar que esse ensaio foi concluído.

A revisão foi conduzida como exercício individual; os PRs registram a integração, mas não devem ser apresentados como prova de revisão independente por outra pessoa.

## 10. Evidências

As capturas de tela serão associadas a esta resolução para demonstrar:

1. histórico do Git com branches e merges;
2. PR #1 integrado;
3. PR #2 integrado;
4. execução dos 13 testes;
5. estado final da branch e árvore de trabalho limpa.

Cada imagem deve ter uma legenda que explique o que comprova. As evidências devem corresponder às saídas reais do repositório e do GitHub.