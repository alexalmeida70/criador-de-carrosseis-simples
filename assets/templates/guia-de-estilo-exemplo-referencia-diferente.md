# Guia de estilo: referência "Flowpilot" (um estilo que não é o do Alex)

Exemplo real de guia escrito a partir de `scripts/periciar.py` numa referência bem diferente do padrão-base: um carrossel de SaaS claro, com UI desenhada, grotesca pesada + serifa itálica fina, magenta e laranja, cartões brancos de canto macio. Serve de modelo pra qualquer referência que a pessoa mandar. Os números abaixo vieram de `docs/pericia-flow.md`; o que é olho está marcado.

Referência: 7 capturas em `refs/referencia-flowpilot/` (6 fatiadas de um mosaico a 218 px de largura + o slide 1 a 568 px). **Resolução baixa**: cores e tamanhos aproximados, confirmados no olho. A referência manda no visual inteiro (a pessoa mandou a referência e pediu "mais parecido com ela, com a Switzer").

---

## 1. A ideia que organiza tudo (olho)
Um carrossel de produto em seis capítulos: problema → produto → o que ele faz (três slides, um por função) → resultado em números → CTA com o "ticket". Cada slide é **um título em duas vozes + uma peça de interface em close** que prova o título. A interface é o argumento; o texto só nomeia. O fundo esquenta do lavanda (problema) ao pêssego (solução): a cor conta a história.

## 2. Formato
4:5, 6 slides, estático. O nosso: 1080×1350, 6 a 8 slides, estático (vivo só se pedido).

## 3. Paleta (medida)
| papel | hex medido | o que fazemos |
|---|---|---|
| fundo, slide 1 (problema) | `#C7C8D2` lavanda-acinzentado | `--papel: #C7C8D2` |
| fundo, slides 2 e 3 | `#E3E2E3` → `#DBE0E3` névoa | tokens por slide via `--papel` |
| fundo, slides 4 a 6 | `#DFDFDC` → `#ECE3D5` → `#ECDCCD` marfim → pêssego | idem; a sequência esquenta, nunca degradê |
| tinta | `#1B2236` marinho | `--tinta: #1B2236` |
| destaque do problema | `#A61764` magenta | `--laranja: #A61764` nos slides 1 e 2 |
| destaque da solução | `#E3834F` laranja | `--laranja: #E3834F` dos slides 3 ao 6 |
| bloco escuro | `#202A46` | `--marinho: #202A46` |
| cartões | `#F8F8F6` | `--creme: #F8F8F6` |
| texto de apoio | `#5C5A6E` | `--mudo` |

Regra medida: por slide, uma cor de fundo + a tinta + **um** destaque (magenta ou laranja, nunca os dois). O destaque aparece em forma (círculo, pílula, botão) e na segunda linha do título (≥ 140 px). Contraste fundo/tinta ≈ 10:1.

## 4. Tipografia (recortes `tipo-flow-*` + atlas)
- **Alta:** grotesca neutra, pesada (~800), tracking apertado, caixa baixa; parece Söhne/Switzer → **Switzer 800** (Fontshare, livre), `--tracking-alta: -0.035em`.
- **Quieta:** serifa de alto contraste, itálica, peso leve, só na segunda linha do título; parece Canela/Ogg itálica → **Instrument Serif itálica** (Google). A assinatura é sempre a **última palavra ou linha** do título ("manual.", "autopilot.").
- **Mono:** rótulos em caixa alta espaçada, relógio, telemetria → **JetBrains Mono 500**, tracking +0,12em.

Escala medida (5 níveis, razão 5,7×): título 142 px (116 a 165) · subtítulo/UI grande 71 px · UI 45 px · apoio 33 px · rótulo 25 px. Entrelinha do título 0,98. Alinhamento à esquerda em 7 de 7 slides.

## 5. Grade e espaçamento (medido)
```
 72 ─┬────────────────────────────────────────────────┬─ 1008
 64  │ Marca                                          │  (nada no canto do contador)
112  │ ───────── fio de 2 px atravessa o carrossel ───│
160  │ (01) — rótulo mono                             │
372  │ TÍTULO PESADO                                  │  ← base da linha 1, 150 px
506  │ segunda linha itálica.                         │  ← base da linha 2
548  │ apoio em 33 px                                 │
660  ├─────────────────────┐        (●196)            │
     │  PEÇA DE INTERFACE  │   selo redondo           │
     │  cartão branco      │                          │
1120 ├─────────────────────┘                          │
1182 │ zigue-zague / trajetória · relógio mono        │
1250 │ legenda mono em caixa alta                     │  (nada no canto do som)
     └────────────────────────────────────────────────┘
```
Margem esquerda 72 px (mediana; desvio 79 por causa da UI interna). Primeiro texto em y≈63; último termina a ≈52 px do pé (nós respeitamos 72). Vazio médio 59 % (de 26 % no CTA a 82 % no slide mais limpo).

## 6. Preenchimento
Curva medida: 56 · 57 · 74 · 82 · 80 · 51 · 27 % de vazio. Os slides de função são os mais vazios (uma peça de UI pequena e muito ar); o CTA é o mais cheio (o ticket ocupa a tela). O nosso mapa copia a curva: internos entre 55 e 80 %, CTA abaixo de 35 %.

## 7. Hierarquia
Cinco níveis, razão 5,7× (o nosso saiu 8,3× na primeira rodada porque o rótulo ficou menor: subir o rótulo pra 25 px). O maior nível é uma frase curta de 3 a 4 palavras em duas linhas, nunca uma palavra só.

## 8. Imagens (olho + medido)
Não há foto: a "imagem" é **interface desenhada** (cartões de notificação, painel com mostrador e chave, chat, mapa de nós, quadro de partidas com letras de aeroporto, ticket com código de barras). Ocupa em média 22 % da tela, nunca sangra, sempre em cartão branco com sombra macia (`0 18px 40px rgba(27,34,54,.12)`), às vezes inclinado 3°. Luminância 0,67, saturação baixa, neutra. **Como reproduzir:** HTML/CSS no slide, nada de Higgsfield (zero créditos). Ícones monocromáticos no destaque. Pra uma marca com elenco, a pessoa entraria só no CTA, em recorte dentro do cartão.

## 9. Formas e dispositivos (medido)
Círculo-selo de 196 px no destaque com número grande dentro; pílula vazada de 2 px com o número do capítulo; cartões brancos de **24 a 27 px de raio** (`--raio: 24px`); bloco escuro `#202A46` de 925×306 com raio 24 (o "quadro de partidas"); fio de 2 px no topo; zigue-zague de 4 px no pé que vira linha calma nos slides de solução; régua de pontinhos. Dispositivo central: **título em duas vozes + peça de UI**. O catálogo do kit não tem "quadro de partidas" nem "ticket": entram como `src/kit/dispositivos/partidas.js` e `ticket.js`.

## 10. Textura e acabamento
Fundo chapado com **grão leve** (std 1,6): `K.fundoLiso` + `K.grao(q, 0.02)`. Sem linho. Curvas de nível finas (10 % de opacidade) atravessando o fundo. Sombras macias só nos cartões.

## 11. Ritmo dos slides
| # | tipo | fundo | destaque | peça |
|---|---|---|---|---|
| 1 | problema | lavanda | magenta | notificações empilhadas + selo "37" |
| 2 | produto | névoa | magenta→laranja | painel com chave |
| 3–5 | funções | névoa → marfim → pêssego | laranja | chat · mapa de nós · relógio |
| 6 | resultado | pêssego | laranja | quadro de partidas + números |
| 7 | CTA | pêssego | laranja | ticket "START FREE" |

Anatomia fixa: marca em cima à esquerda (26 px), fio em y=112, rótulo "0N — capítulo" em mono, legenda mono no pé. A referência põe "1/6" e "SWIPE →" nos dois cantos do Instagram: **não copiamos** (9 invasões medidas; as nossas: 0).

## 12. Movimento e interface
Estático. Ordem de leitura: marca → rótulo → título linha 1 → linha 2 itálica → apoio → peça de UI → selo → trajetória → legenda. No vivo, o título é o quadro 0 e não anima; a peça de UI entra com mola e peso.

## Mecanismos verificáveis
1. Todo título tem duas linhas: a primeira em grotesca 800, a segunda em serifa itálica na cor de destaque, e nada mais usa a serifa.
2. Uma cor de destaque por slide (magenta nos dois primeiros, laranja do terceiro em diante), nunca em texto abaixo de 140 px fora das formas.
3. Cinco tamanhos de texto no carrossel inteiro, razão maior/menor entre 5 e 7×.
4. Fundo chapado com grão leve, sem degradê de tela cheia; o tom esquenta slide a slide (lavanda → pêssego).
5. Cada slide tem uma peça de interface em cartão branco de 24 px de raio com sombra macia, ocupando entre 15 e 30 % da tela.
6. Vazio entre 50 e 80 % nos internos; abaixo de 35 % só no CTA.
7. Margem de 72 px e os dois cantos do Instagram livres em todos os slides.

## Teste numérico (`comparar-pericia.py`, 1ª rodada, 2 slides)
14 OK · 6 REVISAR: razão de níveis (8,3× vs 5,7×: subir o rótulo), grão (forte demais: baixar `K.grao` pra 0,02), ocupação da UI (9 % vs 22 %: a peça precisa crescer), e dois REVISAR de cor que são ruído do OCR na referência pequena. Margem, alinhamento, entrelinha, número de níveis, fundos e cantos: OK na primeira.
