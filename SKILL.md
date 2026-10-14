---
name: criador-de-carrosseis-simples
description: >
  Cria CARROSSÉIS do Instagram de nível de diretor de arte, do tema à entrega:
  estratégia (arquétipo pelo resultado que se quer: save, share, comentário,
  follow), estrutura narrativa em 6 posições (capa, slide 2, espinha, ritmo,
  virada, payoff), copy slide a slide + legenda + CTA, capa em 5 passos (mundo,
  sujeito, contraste, prova, tipo) com imagens no Higgsfield quando houver,
  design em código puro (um HTML por slide, texto de verdade, PNG 1080x1350),
  crítica com notas até ficar bom, e opcionalmente a versão VIVA (cada slide em
  MP4 em loop) em código puro. É a VERSÃO SIMPLES: sem seletor de fidelidade
  (sem referência, o visual é o padrão-base; com referência, ela manda) e sem
  seletor de música (uma só, a editorial). A gramática vem dos carrosséis do
  @growithalex (Alex, Creative Strategist) em três camadas: invariantes (sempre),
  padrão-base (o default dele) e variações (quando e como sair do padrão). Use
  SEMPRE que a pessoa pedir um carrossel, "post em carrossel", "slides pro
  Instagram", "carrossel vivo", "capa de carrossel", "legenda pro carrossel",
  "transforma esse tema/vídeo/aula em carrossel", "no estilo do Alex /
  growithalex", "um listicle de X", "um carrossel pra lançar Y", ou quiser
  revisar/criticar um carrossel pronto, mesmo sem citar a skill. NÃO use para
  roteiro de vídeo, thumbnail do YouTube, material de aula nem motion graphics
  de vídeo. Esta skill não usa HyperFrames nem Remotion: carrossel vivo é
  HTML + seek(t) + Playwright + ffmpeg.
---

# Criador de carrosséis (versão simples)

## Autoria

- Autor: Alex Almeida
- E-mail: alex@maquinaderesultados.com.br
- Site: https://www.maquinaderesultados.com.br
- LinkedIn: https://br.linkedin.com/in/alexalmeida70
- Instagram: https://www.instagram.com/alexalmeida70/

## Compatibilidade de execução

Esta skill pode ser lida por Codex, ChatGPT e Claude Code. Para executar os scripts de renderização, use um ambiente com acesso ao terminal, como Codex ou Claude Code. No ChatGPT sem terminal, produza o briefing, a estrutura, a copy e as instruções de design, mas não afirme que PNGs ou MP4s foram renderizados.

Antes de rodar comandos, detecte o sistema operacional e escolha a variante disponível:

- Python: `py -3` ou `python` no Windows; `python3` no macOS/Linux.
- Carrossel vivo: `powershell -ExecutionPolicy Bypass -File scripts/vivo.ps1` no Windows; `zsh scripts/vivo.sh` no macOS/Linux.
- Instalação da skill: `.codex/skills/` para Codex e `.claude/skills/` para Claude Code.
- Playwright: prefira a dependência local do projeto. Se ela não existir, rode `npm install playwright` e `npx playwright install chromium`. `PLAYWRIGHT_DIR` continua disponível como alternativa explícita.

Nos exemplos abaixo, `python3` representa o executável Python disponível na plataforma.

Esta é a versão sem seletores. O que muda em relação à completa: não existe ajuste de fidelidade (sem referência, o visual é o padrão-base; com referência, a referência manda no visual inteiro, sempre) e não existe escolha de música no vivo (uma só, a editorial do `musica.py`). Tudo o mais é igual.

Um carrossel não é um recipiente de informação. É uma máquina de querer: a capa faz a pessoa querer algo que não queria cinco segundos antes, o slide 2 paga essa promessa, o meio segura, a virada muda o sentido do que veio antes e o último slide pede o próximo passo. Tudo nesta skill serve a isso.

A gramática foi levantada em 8 out 2026 a partir de 19 carrosséis e 17 reels do @growithalex mais dois vídeos dele (o viral de 97,9k curtidas foi um listicle de seis pares de fontes). Os slides originais dele não vêm com a skill (direitos de terceiros); a gramática está destilada em `references/`. Pegue a gramática, nunca o conteúdo, as cenas, o rosto ou o cabeçalho dele.

## As três camadas (leia antes de decidir qualquer coisa)

| Camada | O que é | Peso |
|---|---|---|
| **1. Invariantes** | O que faz qualquer carrossel funcionar, em qualquer estilo. São as seis perguntas das posições, uma ideia por frase, capa legível em miniatura, CTA como continuação. | Sempre. É a régua da crítica. |
| **2. Padrão-base** | O default do Alex: fórmulas de capa, slide 2, slide de regra, virada, CTA, legenda, dispositivos, anatomia fixa, duas fontes, uma cor de destaque. | Ponto de partida quando o pedido não diz outra coisa. Funcionou; não é obrigação. |
| **3. Variações** | Quando sair do padrão (arquétipo, tom, marca, público, formato) e como derivar uma fórmula nova a partir do mecanismo, não da frase. | Só com motivo nomeado no BRIEF. Variar sem motivo vira genérico. |

Referências, na ordem em que você vai precisar:
- `references/01-invariantes.md` · camada 1, as seis perguntas e os portões.
- `references/02-padrao-base.md` · camada 2 visual e estrutural: anatomia, tipografia, cor, catálogo de dispositivos, arquétipos, layouts de capa, regras premium.
- `references/03-copy.md` · camadas 2 e 3 da copy: voz, fórmulas por posição (mecanismo → forma-base → quando trocar → como variar), legenda, anti-padrões, adaptação pro português.
- `references/04-variacoes.md` · camada 3: sinais de troca por arquétipo, tom, marca e formato.
- `references/05-capa.md` · os cinco passos da capa, os dois testes, a fórmula de prompt de imagem, as três rotas de elenco (sem rosto, foto de referência, Soul).
- `references/06-critica.md` · a rubrica de notas, o teste de miniatura, o checklist anti-aislop.
- `references/07-exemplos.md` · como usar os acervos como referência de design: o de referência (`assets/exemplos/`, 179 slides do Alex, só local) e o próprio (`assets/acervo/`, os carrosséis aprovados do autor, vai junto com a skill), com os destaques e o que cada um ensina.
- `references/08-carrossel-vivo.md` · a passagem pra versão em movimento: catálogo de movimento por tipo de slide, som, música, storyboard, as ferramentas (`scripts/vivo.sh` ou `scripts/vivo.ps1`) e os testes de diferença zero.
- `references/09-referencia.md` · quando o pedido traz uma referência (post, capturas, vídeo): a referência manda no visual inteiro. Guardar, medir com `scripts/periciar.py`, desmontar em 12 dimensões no `docs/guia-de-estilo.md` (fonte, cor, grade, espaçamento, preenchimento, hierarquia, imagens e como são feitas, formas, textura, ritmo, movimento), ligar no motor e testar contra ela em número e no olho.
- `references/10-atlas-de-fontes.md` · identificar a fonte da referência pelos recortes e achar a equivalente livre (Google Fonts, Fontshare); `scripts/fontes.py` baixa.

## O briefing (prompt simples na entrada, resultado completo na saída)

O pedido pode vir numa linha ("faz um carrossel sobre X"). A carga de pensar é sua, não da pessoa: preencha tudo que dá pra inferir, registre cada inferência no BRIEF como "assumido", e pergunte só o que muda o resultado e não dá pra adivinhar. No máximo três perguntas, numa mensagem só, antes de começar; o resto vai pra parada do BRIEF.

Todo projeto pertence ao **Grupo MR | Máquina de Resultados** e precisa declarar uma **unidade de negócio**. No início de cada novo projeto, faça esta pergunta antes da estratégia: **"Para qual unidade de negócio do Grupo MR | Máquina de Resultados este carrossel será criado?"** Se a unidade já estiver explicitamente informada no pedido, considere a pergunta respondida e apenas registre a resposta no BRIEF. Nunca infira a unidade pelo tema, pela conta ou por um projeto anterior.

| Item | Default (infira) | Pergunte só se |
|---|---|---|
| Tema e a frase única | do pedido; a frase você escreve | o pedido não diz o tema |
| Grupo | `Grupo MR | Máquina de Resultados` | nunca; é fixo |
| Unidade de negócio | nenhuma; deve ser declarada a cada projeto | sempre que não estiver explícita no pedido; não inferir |
| Conta e marca | `MARCA.md` da unidade/conta; sem MARCA, crie um a partir do pedido e marque "a confirmar" | é uma conta nova sem nenhum dado |
| Resultado desejado → arquétipo | save (Formula ou System) se é ensino; share (Teardown) se é antes × depois; DM (Template) se há material | o pedido mistura objetivos |
| Público e tom | o do MARCA; sem MARCA, direto/criador | a marca é de outro (clínica, loja) e o tom não está claro |
| Elenco | o do MARCA (foto de referência da pessoa em `assets/identidade/` do projeto, ou Soul treinado); marca sem pessoa: sem rosto | a pessoa aparece ou não (muda a capa inteira) |
| Set e cenas | o set do MARCA; sem set, proponha a partir do tema (05-capa.md) | nunca; mostre as fotos e deixe trocar |
| Entrega | estático; "vivo" ou "os dois" se o pedido disser | o pedido não diz E a conta publica carrossel vivo |
| Referência | nenhuma → padrão-base. Se vier (link, capturas, vídeo): `09-referencia.md` (ela manda em fonte, cor, grade, preenchimento, imagens; o MARCA entra só com @, rodapé, elenco e tom) | `scripts/baixar-ig.py` falhou, navegador sem login no Instagram (peça as capturas) |
| Créditos do Higgsfield | até 30 sem perguntar; 60 se for capa + cenas + CTA com elenco | a lista passar do teto: mostre a lista com o custo antes |
| Slides | 8 a 10 (listicle 6 a 8; o editorial de 10: capa foto + 8 cartões + CTA foto) | nunca |
| Idioma | português do Brasil | o pedido vier em outra língua |

Pergunta boa: "A sua cara aparece nas capas (fotos suas com o Higgsfield) ou faço sem rosto?". Pergunta ruim: "qual fonte você prefere?" (isso é seu).

## O fluxo (cada passo tem uma parada ou um portão)

### 0. Referência (só se veio uma)
Tudo como manda `09-referencia.md`: guarde em `refs/` (link do Instagram: `python3 scripts/baixar-ig.py URL --nome x`, baixa post, carrossel ou reel com os cookies do Chrome logado; nunca diga que o link não abre sem rodar o script); rode `python3 scripts/periciar.py refs/referencia-x --nome x`; abra a folha com as medidas e os recortes `tipo-*` de verdade; identifique a fonte pelo atlas (`10`) e baixe com `scripts/fontes.py`; escreva `docs/guia-de-estilo.md` nas doze dimensões, cada uma com número e com o jeito de reproduzir no motor, fechando com 5 a 7 mecanismos verificáveis; ligue os valores em `src/kit/marca.css` e `fontes.css`. A referência manda no que é visível; estratégia, estrutura, copy e crítica continuam das camadas 1 e 3. O BRIEF ganha a seção 1b com a tabela "da referência / do MARCA / do padrão-base".

### 1. Estratégia (10 linhas, no BRIEF.md)
Resultado → arquétipo. Sentimento em uma palavra (calmo, urgente, certo). A frase única que o carrossel defende. O teste de tema antes de qualquer copy: alguém procuraria isso daqui a um ano, e alguém mandaria um slide pra um amigo? Se a resposta honesta é não, diga à pessoa antes de continuar. Estrutura não salva tema fraco: o Alex arquivou um carrossel perfeito por isso.

### 2. Estrutura (o mapa de slides)
Uma linha por slide com a posição que ocupa (open, hold, spine, rhythm, turn, payoff) e o dispositivo. Rode o teste de ordem: se dois slides do meio podem trocar de lugar, não há história (listicle é a exceção declarada). Marque onde está a virada e que forma ela tem.

### 3. Copy
Escreva todos os slides e a legenda seguindo `03-copy.md`. A capa se escreve por último, com a linha mais forte do carrossel. Passe pelos portões de copy de `01-invariantes.md` antes de mostrar. **Parada: mostre BRIEF.md com estrutura e copy e espere o OK.**

### 4. Capa e cenas (Higgsfield)
Mundo → sujeito → contraste e profundidade → prova na cena → tipo por último (`05-capa.md`). Com elenco ou cena: escreva no BRIEF as cenas (capa, a foto da prova em par, o CTA) com lugar, luz, pose, prova no quadro e onde fica o espaço do texto; gere no Higgsfield pelo MCP, pela rota de elenco do MARCA (foto de referência ou Soul), duas variações por cena, 1K ou 2K, nunca pedindo texto; escolha a limpa, regere só o que vier com rosto diferente, faça upscale do que vier mole; gere o recorte sem fundo e o fundo limpo quando houver vivo. Salve em `assets/` com nomes claros e mostre a folha de contato das escolhidas. Anote os créditos gastos. Sem Higgsfield ou sem créditos: capa tipográfica sobre marinho com linho. Rode os dois testes da capa (miniatura a 128 px na grade; "serviria pra outro tema?").

### 5. Design em código
Crie a pasta do projeto com `scripts/novo-projeto.py` (copia o motor `src/kit/` com os dispositivos, as fontes, os scripts e os templates). Um HTML por slide em `src/slides/slide-NN.html` (modelos: `slide-template.html` e, pro cartão editorial, `slide-layout-template.html`), texto desenhado pelo código, fotos como camadas. Tokens da marca em `src/kit/kit.css` (`K.marca({...})` no slide pro handle e rodapé). Toda palavra gigante passa por `K.fit` e toda linha é posicionada pela base com `K.place`. Antes de desenhar cada slide, abra 3 a 6 exemplos da mesma posição e fundo nos acervos (`assets/acervo/indice.md` e, se existir, `assets/exemplos/indice.md` → `todos/`), como manda `07-exemplos.md`, e tire um atributo de cada. **Com referência dada, os exemplos a abrir são os quadros dela (`refs/frames/ref-x-NN.png`) e os tokens vêm do guia (`marca.css`, `fontes.css`); o acervo entra só pro que a referência não mostra.** Siga a anatomia e o catálogo de dispositivos de `02-padrao-base.md`, alternando o fundo a cada slide. Respeite a margem de 72 px e os dois cantos do Instagram (contador no superior direito, som no inferior direito). Renderize com `node scripts/render.mjs stills` → `resultados/estatico/slide-NN.png`, depois `python3 scripts/folha.py` (folha de contato + teste de miniatura) e `python3 scripts/preview.py`. Compare com `assets/exemplos/aprovado/layouts-de-capa-estatico.jpg` antes da crítica.

### 6. Crítica
Olhe a folha e a miniatura de verdade. Dê nota de 1 a 10 em cada item de `06-critica.md` (gancho na capa, slide 2 paga a capa, espinha, ritmo, virada, payoff, copy, leitura em miniatura, paleta e fontes, anti-aislop). Corrija os três piores problemas, renderize de novo, repita até toda nota ser 8 ou mais. Mostre a tabela por rodada. Com referência: some a linha "semelhança com a referência" (os mecanismos do guia) e rode `periciar.py` nos nossos PNGs + `comparar-pericia.py` contra a perícia dela; cada REVISAR é um lugar pra olhar. **Parada: folha de contato final + legenda; espere o OK.**

### 7. Entrega A (estático)
Na pasta do projeto: `BRIEF.md`, `docs/copy.md`, `resultados/estatico/slide-NN.png`, `folha.png`, `miniatura.png`, `legenda.txt`, `preview.html`, mais o relatório (notas por rodada, créditos gastos). Diga em três linhas o que melhoraria em seguida. **Se a entrega inclui o vivo: parada aqui, espere o OK dos PNGs.**

### 8. Entrega B (vivo, só se pedido)
Depois do OK: `STORYBOARD.md` na grade de 120 BPM a partir do catálogo de movimento de `08-carrossel-vivo.md` (capa e CTA 8 s, cartões 6 s), uma linha por batida com o som; mostre e espere o OK. Depois: `seek(t)` em cada slide com os acertos declarados em `K.slide({cues})`, `powershell -ExecutionPolicy Bypass -File scripts/vivo.ps1` no Windows ou `zsh scripts/vivo.sh` no macOS/Linux (beats → música → MP4 → folhas por batida → testes → preview). Entregue `resultados/slide-NN.mp4`, as folhas, os testes (quadro 0 = PNG com diferença zero, loop, som), a tabela de notas e os créditos. Régua: "o movimento serve à ideia do slide ou é enfeite?"

## Regras que não mudam com a camada
- Uma pasta por carrossel. Nunca leia nem sobrescreva o que está fora dela, a não ser as referências desta skill.
- Texto é texto de verdade, desenhado pelo código, nunca imagem de texto. Nunca peça texto pra IA de imagem.
- Uma fonte alta e uma quieta (ou dois pesos da mesma). Uma cor principal e uma de destaque por slide. Paleta de 3 ou 4 cores travada no `MARCA.md`.
- Sem referência, o visual É o padrão-base (receita aprovada em `02-padrao-base.md` §1b: Geist pesada + DM Serif Display na palavra-assinatura + Geist Mono, papel de linho, marinho, laranja, creme, foto de mundo na capa e no CTA). Só saia dela se o `MARCA.md` da conta definir outra identidade, o pedido mandar, **ou se veio uma referência: aí a referência manda no visual inteiro e o teste de aceite é contra ela** (`09-referencia.md`). O teste de aceite visual é pôr o slide ao lado de um exemplo da mesma posição (do acervo, ou da referência quando houver): se não parece da mesma família, não está pronto.
- Proibido: texto em degradê, brilho, neon, degradê de tela cheia, texto em cor de destaque abaixo de 90 px, logo de plataforma ou @ dentro da arte, mais de uma palavra gigante por slide.
- "Salve este post" é fraco. CTA é uma palavra-chave que é o tema do post, com entregável de duas ou três partes nomeadas. Exceção: listicle puro pede SAVE e SHARE.
- Sem HyperFrames, sem Remotion, sem Canva. Código puro, Playwright, ffmpeg.
- Prefira a prova em par (ruim × bom, antes × depois) construída com a MESMA cena mudando uma variável. É a prova mais barata e mais forte.
- Uma v1 serifada com paleta bonitinha e foto fraca foi reprovada como "aislop". O estilo do Alex é serifa mais grotesk: a diferença está na imagem de mundo forte, uma cor, contraste e espaço. Se a imagem for fraca, a mesma gramática vira slop. O portão de qualidade fica na imagem, não na fonte.

## Exemplo rápido de como as camadas decidem

Pedido: "carrossel pra uma clínica de dermatologia sobre protetor solar, tom calmo e premium". Camada 1: seis posições, listicle não serve porque o objetivo é confiança (follow + DM), então arquétipo Formula ou Teardown. Camada 2: estrutura hold → regras com par antes × depois → virada → CTA; dispositivos de par e checklist. Camada 3: "rouba meu" sai (tom premium), par de negação fica ("não é o fator, é o horário"), CTA vira "comenta SOL e eu mando o protocolo de 3 passos", capa sem rosto com objeto na cena (o frasco numa pedra ao sol, sombra real), paleta da clínica. Motivo da variação registrado no BRIEF: tom premium pede menos imperativo.
