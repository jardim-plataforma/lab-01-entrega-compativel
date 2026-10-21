# Arquitetura existente

As setas abaixo mostram requisições/chamadas. As respostas retornam pelo mesmo caminho.

```mermaid
flowchart TD
  A["Portal A · navegador"] -->|"GET /api/v1/recursos/id"| H["Entrada HTTP"]
  B["Integração B · cliente legado"] -->|"mesma API v1"| H
  H --> E["Endpoint + contrato v1"]
  E --> S["Serviço de consulta"]
  S --> R["Repositório de dados"]
  R --> D["JSON · dados fictícios"]
```

O portal é um frontend funcional. A integração B é um programa de terminal, representando outro sistema consumidor. Ambos consultam o mesmo backend. O JSON já contém cinco campos por registro; a projeção v1 retorna somente três. Não são três livros nem três serviços obrigatoriamente: são três campos em cada resposta de recurso.

## Mudança solicitada

```mermaid
flowchart TD
  A["Portal A · contrato atual"] --> V["API existente preservada"]
  B["Legado B · contrato estrito"] --> V
  C["Novo painel C · cinco campos"] -.-> N["Interface a definir no exercício"]
  V --> S["Mesmo serviço de catálogo"]
  N -.-> S
  S --> D["Mesmos registros"]
```

As linhas tracejadas representam o que falta implementar. O painel C é representado por uma sonda de contrato, sem frontend pronto. A decisão de interface é parte da sua resolução.

## Duas entregas simultâneas

A feature amplia a consulta. A correção trata ausência. Ambas passam por `endpoints.py`, mas concorrência não garante conflito textual: o Git pode juntar mudanças que, combinadas, estejam semanticamente erradas. A validação dos resultados é indispensável.
