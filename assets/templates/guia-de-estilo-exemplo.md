# Guia de estilo: "a mesma capa, oito layouts"

Perícia da referência em `refs/referencia-alex/` (10 capturas + legenda em `LEIA.md`).
Os quadros normalizados em 1080x1350 estão em `refs/frames/ref-01.png` a `ref-10.png`,
com a folha `refs/frames/folha-referencia.jpg`. A referência é um carrossel estático
(capturas, não vídeo): por isso há um quadro por slide, e o movimento vem do nosso
STORYBOARD, não dela.

Pegamos a gramática. Não pegamos o conteúdo, as fotos, o nome nem o @ dele.

---

## 1. A ideia que organiza tudo

Um post-aula. A capa promete ("rouba os meus layouts"), oito cartões idênticos na estrutura
ensinam um layout cada, e o CTA fecha com a pessoa, de novo fotográfico. O que muda de um
cartão pro outro é **só onde o texto senta** dentro da mesma foto. A estrutura repetida é
o que faz o leitor comparar: ele aprende pela diferença, não pela explicação.

## 2. Paleta (hex)

| papel | cor | de onde veio |
|---|---|---|
| Papel de linho (fundo claro) | `#EDE9E1` | a referência mede `#F0EFEF`, um cinza-papel frio; esquentamos um passo pro bege de papel que você pediu |
| Fio do linho (textura) | `#D9D3C8` a 0 a 7% | trama horizontal e vertical, só perceptível de perto |
| Marinho (fundo escuro, slides 3 e 6) | `#181D26` | medido `#191F28` / `#171C24` |
| Tinta (título, número, frases) | `#15130F` | medido `#181611` |
| Laranja (círculo, barra, destaque) | `#F2511F` | medido `#F55226` |
| Creme (texto sobre foto e sobre marinho) | `#FBF4E8` | o branco quente do texto da capa e do CTA |

Regras de uso:
- Por slide: **uma cor principal** (a tinta no papel, ou o marinho como chão no escuro)
  **+ uma de destaque** (o laranja). Creme e papel são neutros.
- O laranja nunca é texto abaixo de 90 px. Ele é forma (círculo, barra, faixa, metade) e,
  quando é palavra, é palavra enorme (o "CAPA" do Soco).
- Na barra e no círculo, o texto é tinta sobre laranja, como na referência.

## 3. Tipografia

A referência usa duas famílias: uma grotesca pesada e uma serifa de alto contraste.
Você pediu também uma mono nos rótulos. Pra respeitar "uma fonte de título, uma de apoio",
a mono é da mesma família da grotesca:

| papel | fonte (livre, OFL) | uso |
|---|---|---|
| Título | **Geist** 800/900, tracking −0,045em, entrelinha 0,9 | nome do layout, número, "CAPA", lockups da capa e do CTA |
| Título, variante mono | **Geist Mono** 500, 20 px, minúsculas | rodapé e rótulos pequenos |
| Apoio | **DM Serif Display** itálica (e romana) | "carrossel", "layouts", "LAYOUT" |

Escala no slide de layout (1080x1350):
- Número no círculo: Geist 800, 86 px, tinta sobre laranja.
- Nome do layout: Geist 800, até 116 px (encolhe até caber na largura, nunca quebra).
- Subtítulo: Geist 500, 38 px, logo abaixo do nome.
- Três frases da direita: Geist 500, 31 px, entrelinha 1,14.
- Barra de veredito: Geist 700, 36 px.
- Dentro do cartão da capa: Geist 600 pro sobretítulo pequeno, Geist 900 pro "CAPA",
  DM Serif itálica pro "layouts", Geist 500 pro "onde o texto senta".

Leitura da referência: o nome do layout é sempre "artigo + substantivo" em caixa
alta e baixa ("The Stack"), muito pesado e apertado. A serifa aparece **só** como a
palavra-assinatura de cada lockup ("carousel", "layouts", "LAYOUT"): é ela que dá o tom
editorial. Nunca as duas famílias no mesmo peso visual.

## 4. A grade

### Slide de layout (2 a 9), em px num quadro de 1080x1350

```
 72 ─┬───────────────────────────────────────────────┬─ 1008
     │ (●86)  Nome do Layout                         │  ← zona do contador do IG:
     │ círculo  subtítulo em 38 px                   │    nada acima de y=150 à direita
 352 ├──────────────────────┐                        │
     │                      │   frase 1              │
     │   CARTÃO DA CAPA     │   ───────              │
     │   560 x 700 (4:5)    │   frase 2              │
     │   a mesma foto,      │   ───────              │
     │   texto no layout    │   frase 3              │
1052 ├──────────────────────┘                        │
1096 │ [ barra laranja de veredito ]                 │
1278 │ @handle         criador · fala ia             │  ← rodapé em mono
     └───────────────────────────────────────────────┘  ← zona do ícone de som: x>940, y>1210
```

- Círculo laranja: diâmetro 172, em x=72, y=132. O nome começa 28 px depois do círculo e
  o subtítulo alinha com ele.
- Cartão: x=72, y=352, 560x700, sem borda, sem sombra, cantos retos (a referência é seca).
- Coluna da direita: começa em x=676, 332 px de largura, centrada na altura do cartão.
  Três frases curtas, separadas por dois fios de 3 px em tinta, 250 px de comprimento.
- Barra: começa em x=72, a largura abraça o texto (como na referência, a barra é do tamanho
  da frase), 26 px de respiro em cima e embaixo, até duas linhas.
- Rodapé: "@handle" em x=72 e "criador · fala ia" começando em x=676 (alinhado com a coluna
  da direita), linha de base em y=1278. Assim fica à direita sem entrar no ícone de som.

### Capa e CTA
- Foto sangrando nos quatro lados. Texto em creme sobre o céu escuro.
- Capa: lockup de três linhas como na referência: grotesca pequena em cima à esquerda,
  a serifa enorme no meio, grotesca pequena embaixo à direita.
- CTA: lockup centrado no céu: grotesca ("comenta"), serifa romana enorme ("LAYOUT"),
  grotesca menor com a promessa. "precisa estar seguindo pra receber" no pé, à esquerda.

## 5. Ritmo dos slides

| # | tipo | fundo |
|---|---|---|
| 1 | capa fotográfica | foto |
| 2 | A Pilha | papel |
| 3 | A Faixa | papel |
| 4 | A Metade | **marinho** |
| 5 | A Sobreposição | papel |
| 6 | O Canto | papel |
| 7 | A Linha Baixa | **marinho** |
| 8 | A Moldura | papel |
| 9 | O Soco | papel |
| 10 | CTA fotográfico | foto |

A referência quebra a sequência de papel com dois slides escuros em posições irregulares
(3º e 6º layout). É o que impede os oito cartões de virarem um bloco monótono no swipe.
Mantemos exatamente esse compasso.

## 6. O cartão de cada layout (quatro fotos, cada uma em dois slides)

Na referência a foto é a mesma nos oito. Aqui, a pedido, ela troca a cada dois slides
(corrida, pulo do carro, rocha, píer): cada par ainda compara dois layouts sobre a mesma
imagem, e o carrossel ganha variedade no swipe.

Texto do cartão, sempre o mesmo: sobretítulo "a mesma capa, oito vezes", "CAPA",
"layouts", e a linha "onde o texto senta".

| layout | onde o texto senta | cor do texto |
|---|---|---|
| A Pilha | uma coluna só, embaixo à esquerda | creme |
| A Faixa | faixa laranja sólida atravessando a parte de baixo do meio; foto em cima e embaixo | tinta e creme sobre laranja |
| A Metade | metade de cima foto, metade de baixo laranja; todo texto na metade laranja | tinta e creme sobre laranja |
| A Sobreposição | "CAPA" grande atrás de mim no pulo, "layouts" embaixo: a palavra vira parte da cena | creme |
| O Canto | tudo apertado no canto de cima à esquerda; o resto livre | creme |
| A Linha Baixa | uma linha fina só, no pé | creme |
| A Moldura | fio creme fino em volta, texto dentro da moldura em cima e embaixo | creme |
| O Soco | "CAPA" enorme em laranja (≥ 90 px), o resto minúsculo | laranja + creme |

## 7. Textura

- Fundo de papel com trama de linho desenhada em código (fios horizontais e verticais com
  ruído de semente fixa). Nunca imagem de textura, nunca grão por cima das fotos.
- A textura também existe no marinho, mais fraca.
- As fotos têm o grão de filme delas; não somamos nada.

## 8. Como o texto entra e sai

A referência é estática, então não há entrada nem saída pra copiar. O que ela ensina é
a **ordem de leitura**, e é ela que vai virar a ordem do movimento no vivo:
1. número no círculo,
2. nome do layout,
3. subtítulo,
4. o cartão,
5. as três frases, de cima pra baixo,
6. a barra laranja, por último, como conclusão.

Proibido no vivo, pelo CLAUDE.md: entrar tudo com fade, brilho, neon, partícula.
Entradas por carimbo (escala com peso), por deslize com easing e por desenho do fio.

## 9. Interface do Instagram

- Canto superior direito (contador "1/10"): nada de texto acima de y=150 depois de x=880.
- Canto inferior direito (ícone de som): nada de texto depois de x=940 abaixo de y=1210.
- Margem de 72 px em todas as bordas.
