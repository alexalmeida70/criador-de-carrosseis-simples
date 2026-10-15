# Roteamento de skills de carrossel

Registro consolidado em 14 de outubro de 2026 para impedir que regras de copy, marca, aprovação e renderização de skills diferentes sejam misturadas no mesmo projeto.

## Precedência

1. Propspeed explicitamente identificada como marca ou cliente → `carousel-propspeed`.
2. MktOps, Plugue ou método de quatro atos explicitamente solicitado → `carousel-mktops`.
3. Grupo MR, Máquina de Resultados, MRCA, MRD, MRE ou projeto no `OS-da-Empresa` → `criador-de-carrosseis-simples`.
4. Projeto externo que peça somente copy genérica → `carousel-writer`.
5. Projeto externo que peça design, crítica, PNG, MP4 ou pipeline completo → `criador-de-carrosseis-simples`.

## Regra de isolamento

- Exatamente uma skill principal por projeto.
- Não combinar estruturas narrativas, paletas, templates, portões de aprovação ou pipelines.
- Uma rota especializada só é substituída quando o usuário pedir outra skill explicitamente pelo nome.
- Dentro do `OS-da-Empresa`, `carousel-writer` não deve ser usada.

## Arquivos sincronizados

- `SKILL.md` desta skill.
- `carousel-writer/SKILL.md` na instalação local do Codex.
- `carousel-mktops/SKILL.md` na instalação local do Codex.
- `carousel-propspeed/SKILL.md` na instalação local do Codex.
- `AGENTS.md` na raiz do `OS-da-Empresa`.

