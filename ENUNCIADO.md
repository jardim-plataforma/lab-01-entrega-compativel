# Entregar uma mudança compatível sem interromper os consumidores

[Organização](https://github.com/jardim-plataforma) · [Repositório](https://github.com/jardim-plataforma/lab-01-entrega-compativel)

## Demanda

Uma equipe mantém um catálogo consultado pelo portal de operações e por uma integração legada. Ambos usam `GET /api/v1/recursos/{id}`. Para recursos existentes, recebem `id`, `nome` e `status`. O portal exibe os dados; a integração valida estritamente os três campos antes de processar a resposta.

Uma nova equipe precisa integrar um painel de acompanhamento. Ela precisa dos três campos existentes e também de `unidade` e `responsavel`. Esses dados já estão no armazenamento, mas ainda não são expostos pela API. O novo consumidor deve receber os cinco campos preenchidos para os registros da massa de teste.

A integração antiga não poderá ser atualizada nesta entrega. Você precisa disponibilizar a nova capacidade, preservando as consultas existentes. Este contrato e os nomes dos campos são definições fictícias deste kit, não requisitos extraídos de código da RNP.

Paralelamente, outra pessoa está corrigindo a consulta de recursos inexistentes: em vez de HTTP 200 com objeto vazio, ela deverá responder HTTP 404 com um erro estruturado. Essa entrega toca o mesmo módulo de endpoint. Você começa sua implementação sem esperar, mas precisa integrar e validar as duas mudanças antes de concluir.

## Resultado esperado

A linha principal deve conter uma versão utilizável que atenda os consumidores antigos e permita testar o novo consumidor. A revisão precisa demonstrar por que o contrato continua compatível, qual interface o novo consumidor usa e como recuperar uma versão anterior se a mudança causar regressão.

Neste laboratório, “não interromper” significa preservar o comportamento dos consumidores durante a evolução de contrato. Não haverá comprovação de disponibilidade contínua nem deploy sem downtime: isso exige um ambiente de implantação que ainda não está neste escopo.

## Iniciar e trabalhar

Comece da referência `lab01-inicio`, criada conforme `docs/cenario-git.md`. A branch temporária `feat/consulta-ampliada` será sua branch de resolução. Ela recebe commits e um PR para `main`; não é uma segunda linha permanente. O snapshot inicial continuará acessível pela tag.

Primeiro execute o sistema, os clientes e a suíte. Leia o caminho da requisição no diagrama e identifique o contrato de cada consumidor. Experimente consultar um ID ausente para conhecer o defeito já registrado. Depois escolha como expor os dados novos e explique a decisão no PR.

Não há prescrição de solução pronta: avalie uma interface versionada ou uma extensão explicitamente solicitada, por exemplo. Identificar o chamador não substitui definir o contrato. Este kit não implementa autenticação; um nome de consumidor informado na requisição não comprova identidade.

Enquanto a feature estiver em andamento, introduza a correção concorrente seguindo o roteiro. Integre a `main` atualizada à feature, resolva conflitos se houver e examine a compatibilidade mesmo se não houver conflito textual. Preserve os testes dos consumidores existentes e acrescente testes do novo contrato e dos erros da interface escolhida.

## Critérios de aceite

- Portal A e integração B continuam aceitando todos os recursos existentes, sem modificar seus contratos para esconder uma quebra.
- O consumidor C recebe os cinco campos não vazios. A URL e qualquer seleção de versão ficam documentadas; o programa `consumidores/novo_consumidor.py` permite verificar uma URL completa, incluindo query string se adotada.
- Recursos inexistentes retornam HTTP 404 com `erro.codigo = RECURSO_INEXISTENTE` e `erro.id` igual ao ID solicitado, tanto na interface antiga quanto na interface que você entregar.
- A correção concorrente e seu teste sobrevivem à integração. Testes novos validam também o caminho HTTP real, além de funções isoladas.
- O PR registra a escolha de contrato, alterações, verificações e riscos. Quando houver outra pessoa, ela revisa; se trabalhar sozinha, declare a revisão como exercício individual, sem simular uma aprovação independente.
- `main` termina com as entregas integradas e testadas. Registre o commit final e a versão de software utilizada.
- Documente uma recuperação que retire a feature sem apagar a correção de ausência. Explique que o consumidor novo perde a capacidade recém-introduzida se a feature for revertida.

## Seu papel

O código de aplicação é o material de treino para praticar integração, compatibilidade, revisão, diagnóstico e recuperação. Isso não transfere para você a responsabilidade corporativa de desenvolver regras de negócio. Em um trabalho real, a equipe dona da aplicação participaria da decisão do contrato; Plataforma apoiaria o caminho de entrega e os controles aplicáveis.

Sua resolução será escrita quando você executar o trabalho, com as decisões e resultados reais. Não há relatório preenchido nem solução pronta neste pacote.
