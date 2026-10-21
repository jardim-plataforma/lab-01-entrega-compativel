# Preparação e colaboração em GitHub Flow

Este roteiro não executa push nem merge por você. Os comandos pressupõem o clone do seu repositório, `origin` apontando para ele e branch principal `main`. Se ela tiver outro nome, substitua `main`. Não renomeie nem apague branches existentes apenas para reproduzir o exemplo.

## Registrar a base

Copie o conteúdo de `repositorio/` deste kit para a raiz do clone. Revise as substituições de README e enunciado. A pasta externa `repositorio` não deve ser publicada como uma subpasta. Preserve arquivos seus que não estejam no kit.

Para adicionar a base a uma `main` já existente, use uma branch de preparação e um PR. O repositório precisa ter um commit inicial; se estiver vazio, inicialize-o com README pelo GitHub e clone-o antes.

```sh
git switch main
git pull --ff-only
git switch -c chore/base-lab01
```

Depois de copiar os arquivos, rode os testes e examine `git status` e `git diff`. Selecione os arquivos desta base, faça commit e abra o PR de preparação. Após integrar esse PR:

```sh
git switch main
git pull --ff-only
git tag lab01-inicio
git push origin lab01-inicio
git switch -c feat/consulta-ampliada
```

Crie a tag uma única vez no commit que contém a base. Se já existir, confira sua origem e não a sobrescreva. A tag é uma referência estável para refazer o exercício; `main` continua evoluindo.

## Sua feature

Trabalhe em `feat/consulta-ampliada`, faça commits e abra um PR para `main`. Ela é a sua branch de resolução. Não há necessidade de criar outra branch permanente chamada `resolucao`. Antes de trocar de branch, faça commit das mudanças ou guarde-as conscientemente; não execute comandos de descarte para limpar o diretório.

## Simular a outra pessoa

Quando a feature já tiver trabalho, parta da mesma base para criar a correção. O patch contém somente a correção e um teste de regressão, não a solução da feature.

```sh
git switch -c fix/recurso-inexistente lab01-inicio
git apply --check cenario/colega-correcao.patch
git apply cenario/colega-correcao.patch
python -m unittest discover -s tests -v
git add backend/catalogo/endpoints.py tests/test_ausencia.py
git commit -m "fix: retorna 404 para recurso inexistente"
git push -u origin fix/recurso-inexistente
```

Abra um segundo PR para `main`, revise e integre essa correção antes de concluir o PR da feature. Aqui você representa dois papéis por estar estudando sozinha; em equipe seriam duas pessoas. Escolhemos deliberadamente essa ordem para treinar uma atualização concorrente.

## Incorporar a correção à feature

Com o diretório de trabalho limpo:

```sh
git fetch origin
git switch feat/consulta-ampliada
git merge origin/main
```

Se houver conflito, leia as duas intenções, edite o resultado, rode os testes e conclua o merge. Não aceite simplesmente “meu lado” ou “lado deles”. Se não houver conflito, teste mesmo assim. Reinicie o servidor antes dos testes manuais: o servidor deste kit não recarrega o código sozinho.

Atualize o PR da feature, revise as evidências e integre quando os critérios forem satisfeitos. A branch poderá ser excluída depois; PR, commits e tag conservam o histórico.

## Recuperação a documentar

Identifique o commit de integração da feature e proponha sua reversão em uma branch nova baseada na `main` atual. Para squash ou commit comum, `git revert SHA_DA_FEATURE` cria a reversão; para um merge commit, inspecione os pais e use `git revert -m 1 SHA_DO_MERGE` somente se o primeiro pai representar a principal que deseja preservar.

Não use literalmente esses marcadores. Escolha o SHA real, abra PR e teste a correção de ausência e os consumidores antigos. Não faça reset forçado da principal para a tag inicial: isso também retiraria a correção concorrente. Como não há deploy automatizado neste laboratório, a recuperação do processo local inclui parar e reiniciar o servidor na revisão escolhida. Explique o impacto sobre C antes de executar.

Se quiser ensaiar a reversão sem torná-la o resultado final do exercício, valide na branch de recuperação e registre as evidências no PR sem integrar essa reversão.
