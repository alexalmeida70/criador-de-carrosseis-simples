# Camada 2 · Padrão-base (o default do Alex, visual e estrutural)

Use como ponto de partida quando o pedido e o `MARCA.md` não disserem outra coisa. Cada item tem o mecanismo (por que funciona); a forma é trocável, o mecanismo não.

## 1. Anatomia fixa ("The Frame": o que repete é o que lembram)
- **Cabeçalho da capa:** nome da conta + recibo (título real e número real: "235K inscritos", "97 mil curtidas"). Mecanismo: prova antes de ler.
- **Cabeçalho dos internos:** mês e ano · nome · título profissional, em caixa alta pequena. Mecanismo: cara de publicação, reconhecimento no print.
- **Slide final:** "Meu nome é X" e o bordão nos cantos superiores, "comenta PALAVRA" gigante, entregável em 1 ou 2 linhas, "precisa estar seguindo pra receber" pequeno no canto inferior esquerdo. Cena recorrente (o "set" do CTA).
- **Elenco e set:** a pessoa como personagem de uma cena cinematográfica, nunca a cara colada no post. O mesmo tipo de lugar repetido até virar seu (deserto, praia, campo). As capas antigas como props das novas (o "archive").

## 1b. A receita visual padrão (o que a skill usa quando o MARCA.md não diz outra coisa)
Valores aprovados no projeto "a mesma capa, oito layouts" (out/2026), já no `assets/engine/kit.css`:

| Token | Valor | Onde |
|---|---|---|
| Grotesca (título, nomes, números, corpo) | **Geist** 800/900, tracking -0,045em, entrelinha 0,9; 500 no corpo (OFL, em `assets/fonts/`) | nome do layout, número no círculo, lockups da capa, frases, barra |
| Serifa (a palavra-assinatura) | **DM Serif Display** itálica (e romana), 400 | só a palavra de ênfase de cada lockup: "carrossel", "layouts", "LAYOUT". Nunca as duas famílias no mesmo peso visual |
| Mono (rótulos) | **Geist Mono** 500, 20 px, minúsculas | rodapé, cabeçalho, marcadores de tempo |
| papel | `#EDE9E1` + trama de linho desenhada em código (`K.fundoPapel`) | metade dos slides internos |
| marinho | `#181D26` + linho mais fraco (`K.fundoMarinho`) | os slides escuros, em posições irregulares (3º e 6º cartão) |
| tinta | `#15130F` | texto sobre papel; número e barra (tinta sobre laranja) |
| laranja | `#F2511F` | círculo, barra, faixa, metade, UMA palavra gigante (≥ 90 px). Nunca texto pequeno |
| creme | `#FBF4E8` | texto sobre foto e sobre marinho |
| foto | sangrando nos quatro lados, golden hour, céu escuro no alto com espaço pro texto | capa e CTA (e os cartões de prova) |

A capa e o CTA são fotográficos; os internos alternam papel e marinho. Por slide: uma cor principal + o laranja. Os três exemplos mais próximos: `assets/exemplos/aprovado/layouts-de-capa-estatico.jpg` (o carrossel inteiro aprovado), `capa-26-s01` e `regra-20-s03` do Alex.

## 1c. A grade do slide editorial (círculo · nome · cartão · frases · barra), em px no quadro 1080×1350
Já implementada em `assets/engine/dispositivos/layout-slide.js` e no `kit.css`:
- Círculo laranja Ø172 em x=72, y=140, número Geist 800 88 px em tinta. Nome do layout a partir de x=268, linha de base y=236, até 116 px (encolhe até caber em 738 px, nunca quebra). Subtítulo Geist 500 38 px, base y=296.
- Cartão da prova: x=72, y=352, 560×700, sem borda, sem sombra, cantos retos. Coluna da direita a partir de x=676, 332 px de largura, centrada na altura do cartão; três frases Geist 500 31 px separadas por dois fios de 3 px e 250 px.
- Barra de veredito em x=72, y=1096, a largura abraça a frase (Geist 700 36 px), 25 px de respiro, até duas linhas.
- Rodapé em Geist Mono 20 px: `@handle` em x=72 e `criador · [conta]` em x=676, base y=1278 (longe do ícone de som).
- Zonas proibidas: contador do Instagram (x > 880, y < 150) e ícone de som (x > 940, y > 1210). Margem de 72 px.
- Ordem de leitura (que vira a ordem do movimento no vivo): número → nome → subtítulo → cartão → frases de cima pra baixo → barra.

## 2. Tipografia (uma alta, uma quieta, uma etiqueta)
- **Alta (título):** serifa display de alto contraste, muitas vezes itálica, gigante, em minúsculas, encostando nas bordas. Ou uma grotesk pesada em caps fazendo o mesmo papel.
- **Quieta (apoio e corpo):** grotesk neutra (Inter, Switzer), tracking apertado no título, regular no corpo. Linhas curtas.
- **Etiqueta (opcional):** uma terceira voz só como rótulo: script manuscrito, mono, sublinhado ou círculo rabiscado.
- Título em duas ou três vozes empilhadas: pequena / GIGANTE / média. Uma palavra do título na cor de destaque, nunca duas.
- Mecanismo: o contraste de escala entre as duas fontes faz 90% do trabalho. Dois pesos da mesma família também servem.

## 3. Cor
- Paleta travada: um escuro texturizado (tecido, linho, papel amassado), um claro de papel, UM acento quente, um neutro quente. Três ou quatro cores, sempre as mesmas; muda qual lidera (tema sério lidera o escuro, leve lidera o claro, urgente lidera o acento).
- Texto branco sobre escuro, preto sobre claro. Nunca texto em degradê, nunca glow, nunca três cores de texto.
- Fotos quentes (laranja, dourado, entardecer) ou frias de propósito pra contraste (névoa, neve).
- Saturação puxada pra trás e pretos que não são #000. "Barato é saturação máxima; caro é a mesma cor contida."

## 4. Ritmo visual
Alternar a cada slide: claro → escuro → claro → foto de página inteira → escuro. Slide cheio → slide vazio. Dispositivo → frase só. Quem passa rápido sente a troca antes de ler.

## 5. Catálogo de dispositivos de slide (escolha um por slide)
1. **Regra com etiqueta inclinada:** pílula torta com o número por extenso sobre UMA palavra gigante em caps + definição em itálico + 2 linhas + par de imagens com rótulo de 1 palavra + linha de leitura.
2. **Número vertical na margem:** "UM / DOIS / TRÊS" girado na esquerda + título + subtítulo serifa + corpo + imagem anotada.
3. **Pílula "Regra N" + palavra minúscula gigante** + 1 frase + par ruim × bom + fecho.
4. **Círculo numerado + nome + três linhas separadas por fio + barra de veredito** com a MESMA imagem re-renderizada à esquerda.
5. **Tabela de 2 ou 3 colunas** com cabeçalho na cor de destaque + frase de escolha ("escolha a linha que você cumpriria numa semana ruim").
6. **Ficha técnica:** cartões "FONTES / CORES (bolinhas + hex) / USO".
7. **O slide é a resposta:** dois cartões de cor com nome e hex; a palavra de cima numa fonte e a de baixo na outra. 6 a 13 palavras.
8. **Par ✗/✓, antes × depois, genérico × o seu:** a MESMA cena mudando uma variável. O dispositivo de prova mais usado.
9. **Checklist com ✓** · **grade de caixas com borda de destaque** como índice · **diagrama de linhas** (árvore, linha do tempo, radial) · **equação de ícones** · **mockup de celular ou da grade do feed** · **polaroids com moldura**.
10. **Slide de virada:** foto grande + duas frases, sem dispositivo. Muda a forma de propósito.
11. **Slide só texto** sobre papel ou preto, três linhas. Quebra o ritmo.

## 6. Os seis arquétipos e o que cada um ganha (escolha pelo resultado)
| Arquétipo | O que é | Ganha |
|---|---|---|
| **System** (o playbook) | O processo inteiro, numerado, com uma regra inquebrável. | saves |
| **Formula** (o blueprint) | Uma habilidade quebrada em partes NOMEADAS. Nomear é o que torna seu. | saves + autoridade |
| **Teardown** (a autópsia) | Antes × depois mudando UMA coisa. | shares |
| **Vault** (a coleção) | 17 skills, 20 formatos, 50 ganchos. Impossível lembrar. | o maior save |
| **Template** (o preencha) | Não um post que se lê, uma coisa que se usa. | comentários e DMs |
| **Confession** (a cicatriz) | Admissão honesta com a lição. Cicatriz curada, nunca ferida aberta. | follows e comentários |

## 7. Os oito layouts de capa (onde o texto senta)
Stack (tudo numa coluna embaixo à esquerda; o padrão) · Band (faixa chapada no meio segurando o texto) · Split (metade imagem, metade cor; texto na cor) · Overlap (texto sobre a imagem com contraste) · Corner (texto num canto, resto livre) · Low Line (uma linha fina no pé, imagem lidera) · Frame (texto dentro de uma moldura) · Punch (uma palavra-herói gigante, o resto pequeno).

## 8. As cinco regras premium (o anti-slop)
contraste (uma cor herói) · contenção (um efeito só) · paleta travada · duas fontes, sempre as mesmas · espaço. "Caro nunca foi dinheiro ou talento. É direção."

## 9. As seis decisões que criam o sentimento (nomeie o sentimento antes)
Sujeito (uma coisa) · Escala (pequeno = reverência, cheio = proximidade) · Luz (quente convida, fria dá autoridade) · Espaço (cheio = pânico, vazio = confiança) · Tensão (uma coisa sem resolver) · Espelho (a pessoa se vê). "Se não consegue apontar a decisão que causou o sentimento, você decorou."

## 10. Os seis dispositivos da imagem que "aconteceu"
rastro (mostrar a pessoa pelo que deixou) · intruso (uma coisa que não devia estar ali) · olhar fora de quadro · consequência (o carro queimado, não a batida) · meio da ação (nunca em repouso) · escala (o sujeito pequeno demais). Mesma locação, muda só o que está no quadro.
