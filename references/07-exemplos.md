# Exemplos do Alex em `assets/exemplos/` e o que cada um ensina

A skill é autossuficiente como referência de design de carrossel: os **179 slides dos 19 carrosséis** estão em `assets/exemplos/todos/NN-sMM.jpg` (540 px), indexados em `assets/exemplos/indice.md` por post, posição (capa, slide 2, regra, virada, CTA), fundo (claro, escuro, foto) e primeiras palavras do texto. Os 36 abaixo são os destaques, com o que cada um ensina.

Se a pasta `assets/exemplos/` não existir nesta instalação (o acervo não é redistribuído: são imagens do @growithalex), pule a consulta visual e siga só pela receita de `02-padrao-base.md`; o teste de aceite passa a ser a rubrica de `06-critica.md`.

## Acervo próprio (`assets/acervo/`, vai junto com a skill)
Os carrosséis aprovados do autor, no mesmo formato: `assets/acervo/todos/NNN-sMM.jpg` (540 px), `assets/acervo/indice.md` por post, posição e fundo, e `assets/acervo/licoes.md` com o que cada destaque (`posição-NNN-sMM.jpg`) ensina. Os posts contam a partir de 101. Use os dois acervos do mesmo jeito: 3 a 6 exemplos da mesma posição e fundo, um atributo de cada. Quando um carrossel novo passar na crítica e você gostar dele, acrescente-o com `node scripts/acervo.mjs add <pasta-do-projeto> --post NNN --titulo "…" --posicoes capa,slide2,regra,…` e preencha as primeiras palavras no `indice.md` e as lições no `licoes.md`.

## O carrossel aprovado como régua (`assets/exemplos/aprovado/`)
O projeto "a mesma capa, oito layouts" (out/2026) é o melhor resultado até agora e vai junto com a skill: `layouts-de-capa-estatico.jpg` (os 10 slides), `layouts-de-capa-cenas.jpg` (as fotos geradas, com e sem fundo), `layouts-de-capa-slide-02-por-batida.jpg` (a coreografia de um cartão), `layouts-de-capa-teste-quadro0.jpg` e `layouts-de-capa-teste-loop.jpg` (o que "aprovado" quer dizer no vivo). Antes de entregar, compare com eles: é a mesma família?

## Como usar o acervo antes de desenhar
1. Pra cada slide que você vai desenhar, abra 3 a 6 exemplos da **mesma posição e do mesmo fundo** (`indice.md` → `todos/`). Olhe de verdade (Read na imagem).
2. Tire **uma coisa de cada referência**: a escala da palavra gigante de uma, a grade do par de outra, o rodapé de outra. Seis referências, seis atributos, e ninguém rastreia (regra do Alex).
3. Pegue a gramática (grade, escala, dispositivo, ritmo entre slides), nunca o conteúdo, a cena, o rosto nem o cabeçalho dele.
4. A linha "ritmo" de cada post no índice mostra a alternância de fundos que ele usa; copie o princípio da alternância, não a sequência.

Arquivo original em tamanho real (1080×1350), legendas, reels e análises slide a slide: `~/carroussel/referencia/growithalex/` (`galeria.html`, `analise/`).

## Capas (`capa-*`)
| Arquivo | O que ensina |
|---|---|
| capa-02-s01 | Capa de revista: cabeçalho com data · nome · título; três vozes (itálica leve / GIGANTE / bold menor); ele como personagem numa cena (rede de tênis); capas antigas como props 3D. |
| capa-04-s01 | Mundo que não ilustra o tema (pinguim lendo jornal na Antártida pra um post sobre imagem); rodapé em trio; serifa gigante branca. |
| capa-10-s01 | Três camadas (papoulas desfocadas na frente, ele deitado com a ovelha, céu chapado); uma palavra em laranja; rodapé "5 RULES. ONE IMAGE. 97,800 LIKES." |
| capa-16-s01 | "steal my carousel layouts": prova na cena (as capas antigas espalhadas no chão com sombra real). |
| capa-20-s01 | Astronauta abraçando a Terra num campo de flores: sujeito reconhecível, sentimento antes do tema; título cruza o sujeito. |
| capa-22-s01 | O viral (97,9k): "best font Pairings" com o "Pa" em quadrado de tabela periódica; borrow (Breaking Bad). Título simples, prova pela cena. |
| capa-24-s01 | Capa com BLUR: quatro capas desfocadas em primeiro plano (a resposta está ali e você não pode ter); rodapé "4 posts · 1 idea · 12000 SAVES". |
| capa-26-s01 | Carro em chamas no deserto, ele numa cadeira de camping: a cena da "tensão"; duas capas antigas em pé. |
| capa-28-s01 | Binário "cheap v/s expensive" com setas desenhadas à mão e os dois cartões lado a lado. |
| capa-34-s01 | "brand WORLD": palavra gigante em caps na cor de destaque, serifa itálica branca em cima, astronauta em lótus. |
| capa-36-s01 | Intruso: um tomate em cima da TV antiga no deserto; "attention isn't won. it's re-won". |

## Slide 2 (`slide2-*`)
| Arquivo | O que ensina |
|---|---|
| slide2-10-s02 | Tese + "nobody teaches this" + índice de 5 pílulas numeradas. |
| slide2-20-s02 | "Emotion is the story" + 2 parágrafos + grade 3×2 de caixas brancas com borda laranja + ferroada final. |
| slide2-24-s02 | Paga a capa: as 4 capas agora nítidas, conectadas por linhas, com os saves de cada uma e o total. |
| slide2-26-s02 | Tese + grade de 6 caixas conectadas + 3 capas-exemplo embaixo. |
| slide2-28-s02 | Diagnóstico sem insulto: "Two people post the same idea…" + dois mockups de iPhone. |

## Slides de regra (`regra-*`)
| Arquivo | O que ensina |
|---|---|
| regra-20-s03 / s06 | O template de regra: etiqueta laranja inclinada com número por extenso sobre a palavra gigante; definição itálica; par ✗/✓ com a MESMA sala mudando uma variável; rótulos de uma palavra; linha de leitura. Fundo linho × preto. |
| regra-16-s02 | Círculo numerado + nome + três linhas separadas por fio + barra laranja de veredito; a mesma capa re-diagramada à esquerda. |
| regra-06-s02 | Listicle de estéticas: a mesma capa em outro look + "use quando / pule quando" + termo de busca. |
| regra-14-s04 | Tabela de 2 colunas com cabeçalho laranja + frase de escolha. |
| regra-28-s05 | "locked palette": prova com três capas em cores erradas × três na paleta travada. |
| regra-08-s02 | GRADE ONE: mesma foto, uma variável (a luz), par com legenda de leitura. |
| regra-18-s03 | Ficha técnica: FONT PAIRINGS / COLOURS com hex / USE CASES. |
| regra-10-s05 | Checklist com ✓ ao lado da capa + fecho em caixa. |
| regra-26-s04 | Número vertical na margem + nome + "Wins saves and authority" + capa anotada com as partes nomeadas. |

## Listicle (`listicle-*`)
| Arquivo | O que ensina |
|---|---|
| listicle-22-s02 | O par de fontes É o design: a palavra de cima numa fonte, a de baixo na outra, foto de mundo atrás, 3 palavras. |
| listicle-12-s05 | A mesma ideia um mês depois, com pílula branca de rótulo. |
| listicle-17-s04 | Dois cartões de cor com nome e hex ocupando o slide inteiro. |

## Virada (`virada-*`)
| Arquivo | O que ensina |
|---|---|
| virada-20-s09 | Foto grande (Homem-Aranha na rede) + "Don't ask 'does it look good.'" Nenhum dispositivo. |
| virada-26-s09 | "You don't have a content problem" + diagrama radial com o resultado no centro. |
| virada-28-s08 / s09 | "You don't need a designer or a budget" sobre silhueta em movimento; depois o slide só texto em papel: "Expensive was never money or talent." |

## CTA (`cta-*`)
| Arquivo | O que ensina |
|---|---|
| cta-02-s09 | A cena recorrente do CTA (praia + quiosque neon), cantos com nome e bordão, "comment UNCOPY" gigante, "must be following" pequeno. |
| cta-28-s10 | Retrato com prisma + "comment PREMIUM for the checklist" + a nota "'Save this' is weak. 'Comment PREMIUM' is strong." |
| cta-14-s09 | O CTA de listicle: SAVE / SHARE, sem palavra-chave. |

## Referência dada (`assets/exemplos/referencia-dada/`, só local)

Exemplo de ponta a ponta da rota de `09-referencia.md` numa referência de outro estilo (o carrossel "Flowpilot": SaaS claro, UI desenhada, Switzer + serifa itálica): a folha da perícia com as medidas desenhadas (`flowpilot-folha-pericia.jpg`), a perícia em números (`flowpilot-pericia.md`), o lado a lado nosso × referência (`flowpilot-lado-a-lado.png`) e a comparação numérica (`flowpilot-comparacao.md`). Mais a perícia de um post do Alex (`alex-folha-pericia.jpg`) pra ver a ferramenta no padrão-base. O guia escrito a partir disso está em `assets/templates/guia-de-estilo-exemplo-referencia-diferente.md`.
