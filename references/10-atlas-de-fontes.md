# Atlas de fontes: identificar a da referência e achar a equivalente livre

A ferramenta (`scripts/periciar.py`) recorta as maiores linhas de texto da referência em `refs/frames/tipo-*.png`, a 2x. Abra os recortes e classifique a fonte com as perguntas abaixo; depois escolha a equivalente e baixe com `scripts/fontes.py`. Se a referência usa uma fonte livre, use a mesma fonte, não a equivalente.

## Como olhar um recorte (cinco perguntas, nesta ordem)

1. **Tem serifa?** Serifa (os pezinhos) → vá pra tabela de serifas. Sem serifa → grotesca, geométrica ou humanista. Largura fixa (todas as letras do mesmo tamanho, o "i" igual ao "m") → mono. Parece caneta ou pincel → manuscrita.
2. **Contraste dos traços:** finos e grossos muito diferentes (Didot, Bodoni, as serifas de revista) ou traço quase uniforme (Inter, Helvetica)? Serifa de alto contraste é "display"; de baixo contraste é "de texto".
3. **Forma do O e do G:** O perfeitamente redondo e G sem esporão → geométrica (Futura, Gotham, Circular). O levemente oval, terminais horizontais, "a" de dois andares, "G" com esporão → grotesca (Helvetica, Inter, Switzer, Geist). Terminais inclinados, "a" e "e" abertos, parece caligrafia → humanista (Frutiger, Gill).
4. **Largura e altura de x:** apertada e alta (Druk, Bebas, Anton) ou larga e baixa? Caixa alta sempre? Isso decide entre condensada, normal e estendida.
5. **Peso e tracking:** muito pesada (800/900) com entreletra negativa (o padrão do Alex), ou leve (300) com entreletra aberta? O periciar dá o tamanho; o peso e o tracking são do olho (compare com o recorte depois de renderizar).

Escreva no guia: "Título: grotesca neutra, peso ~800, tracking −0,04em, caixa baixa; parece Söhne → Geist 800" e cole o recorte ao lado.

## Equivalentes livres (comercial → Google Fonts `G` · Fontshare `F` · já na skill `S`)

### Grotescas e neo-grotescas (o grosso dos carrosséis de criador)
| Se parece com | Use | Como reconhecer |
|---|---|---|
| Helvetica, Arial, Neue Haas Grotesk | Inter `G` · Switzer `F` | neutra, terminais horizontais, G com esporão |
| Söhne, Suisse Int'l, Aktiv Grotesk | **Geist** `S` · General Sans `F` · Inter Tight `G` | neutra e apertada, moderna, x alto |
| GT America, Founders Grotesk | Switzer `F` · Public Sans `G` | americana, um pouco mais larga, R com perna reta |
| Aeonik, Basis Grotesque | Manrope `G` · Satoshi `F` | geométrica com alma grotesca, cantos suaves |
| SF Pro, Roboto | Inter `G` (ou Roboto `G`, que é livre) | a do iPhone/Android |
| Univers, Akzidenz | Archivo `G` · Work Sans `G` | mais velha, mais larga, séria |
| Cabinet Grotesk, Clash Grotesk, Satoshi, General Sans, Switzer | elas mesmas `F` (livres) | já são livres: use a própria |

### Geométricas
| Se parece com | Use | Como reconhecer |
|---|---|---|
| Futura | Jost `G` | O redondo perfeito, M pontudo, j e t curtos |
| Avenir, Avenir Next | Nunito Sans `G` · Outfit `G` | geométrica suavizada, muito legível |
| Gotham, Proxima Nova | Montserrat `G` · Figtree `G` | larga, redonda, "corporativa americana" |
| Circular, Graphik | DM Sans `G` · Plus Jakarta Sans `G` · Figtree `G` | redonda e amigável, a das startups |
| Gilroy, Sofia Pro | Outfit `G` · Clash Grotesk `F` · Lexend `G` | geométrica com pesos muito pesados |
| Poppins | Poppins `G` (livre) | a mais usada em carrossel genérico; cuidado com cara de template |

### Humanistas
| Se parece com | Use |
|---|---|
| Frutiger, Myriad | Source Sans 3 `G` · Hind `G` · PT Sans `G` |
| FF Meta, Fira | Fira Sans `G` |
| Gill Sans | Cabin `G` · Lato `G` |

### Condensadas e display pesadas (capas de impacto, "palavra gigante")
| Se parece com | Use | Como reconhecer |
|---|---|---|
| Druk, Tusker Grotesk, Impact | Anton `G` · Bebas Neue `G` | caixa alta, altíssima, apertada, pesadíssima |
| Knockout, Trade Gothic Condensed | Oswald `G` · Barlow Condensed `G` | condensada de jornal, caixa alta e baixa |
| Compressa de pôster | Six Caps `G` · Big Shoulders Display `G` | ainda mais estreita |
| Display geométrica pesada | Clash Display `F` · Unbounded `G` · Syne `G` | larga, estranha de propósito |

### Serifas de display (as "de revista", o itálico de assinatura do Alex)
| Se parece com | Use | Como reconhecer |
|---|---|---|
| Canela, Ogg, PP Editorial New | Instrument Serif `G` · **DM Serif Display** `S` | alto contraste, elegante, itálico caligráfico |
| GT Sectra, Reckless, Recoleta | Fraunces `G` (eixos de "soft" e "wonk") · Young Serif `G` | serifa com personalidade, terminais em gota |
| Didot, Bodoni | Playfair Display `G` · Bodoni Moda `G` | contraste extremo, serifa fina de fio |
| Cooper Black, Windsor | Fraunces 900 "soft" `G` · Young Serif `G` | serifa gorda e redonda, anos 70 |
| Zodiak, Sentient | elas mesmas `F` (livres) | serifas livres do Fontshare |

### Serifas de texto (corpo, citação, editorial calmo)
| Se parece com | Use |
|---|---|
| Tiempos, Times, Georgia | Newsreader `G` · Source Serif 4 `G` · Gelasio `G` |
| Garamond, Minion | EB Garamond `G` · Cormorant `G` · Crimson Pro `G` |
| Freight, Caslon | Lora `G` · Libre Caslon Text `G` |

### Mono (rótulos, telemetria, "voz de máquina")
| Se parece com | Use |
|---|---|
| SF Mono, Söhne Mono, Berkeley Mono | **Geist Mono** `S` · JetBrains Mono `G` |
| Menlo, Monaco, Courier | IBM Plex Mono `G` · Courier Prime `G` |
| Space Mono (livre), Azeret Mono | elas mesmas `G` |

### Manuscritas e marcador (anotação, rabisco, "humano")
Caveat `G` (caneta), Kalam `G`, Permanent Marker `G` (marcador grosso), Rock Salt `G`, Gochi Hand `G`. Use só como etiqueta: nunca como fonte de título.

## Baixar e ligar

```bash
python3 scripts/fontes.py --google "Inter" "Instrument Serif" --fontshare switzer
```

Sai em `assets/fonts/` (arquivos locais, o render não depende de rede) e em `src/kit/fontes.css` (os `@font-face`). Depois, em `src/kit/marca.css`:

```css
:root { --alta: 'Switzer'; --quieta: 'Instrument Serif'; --mono: 'JetBrains Mono'; --tracking-alta: -0.03em; }
.serifa { font-style: normal; }   /* se a palavra-assinatura da referência é reta, não itálica */
```

Confira no render: abra o recorte da referência ao lado do nosso PNG na mesma escala. Peso, tracking e entrelinha se acertam aí, não no chute.

## Licenças
Google Fonts: só fontes livres (OFL, Apache, UFL). Fontshare: ITF Free Font License (uso comercial permitido, redistribuição não; por isso os arquivos ficam no projeto, não na skill). As da skill (Geist, Geist Mono, DM Serif Display) são OFL e vão junto com ela.
