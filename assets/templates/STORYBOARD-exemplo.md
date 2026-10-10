# STORYBOARD: o carrossel vivo

120 BPM: uma batida a cada 0,5 s, um compasso a cada 2 s. 30 fps.
O quadro 0 de cada slide é o PNG aprovado em `resultados/estatico/`. Todo movimento sai do
repouso e volta ao repouso antes do fim; nenhum acerto nos últimos 0,8 s.

Sons (três famílias, como manda o CLAUDE.md):
- **impacto**: o carimbo do número e o "tchac" da barra (grave curto + tapa no médio).
- **whoosh**: o cartão atravessando a borda e o texto deslizando.
- **clique**: palavras pousando, frases entrando, teclas do CTA, folhas imprimindo.

Música: uma só, quente e mínima, em ré menor, 64 s (32 compassos). Cada slide pega os
compassos seguintes: capa 1 a 4, slides de layout 3 compassos cada (5 a 28), CTA 29 a 32.
Cada trecho começa em Rém9 e termina num acorde que resolve de volta nele, então o loop
de cada slide fecha e o swipe pro próximo também.
- 4 compassos: Rém9 | Si♭maj7 | Solm9 | Dó6/9
- 3 compassos: Rém9 | Si♭maj7 | Dó6/9

---

## 01 · Capa · 8 s · 4 compassos (16 batidas)

| t (s) | batida | o que se mexe | som |
|---|---|---|---|
| 0,0 | 1 | repouso: o PNG da capa | música entra (pad + piano elétrico + bumbo macio) |
| 0,5 | 2 | a câmera começa a empurrar devagar: fundo 4%, eu 5,5%, título 7% (parallax), volta ao repouso em 7,5 s | |
| 1,0 | 3 | "carrossel" sobe esticando e **carimba**: achata e volta (o volume não muda) | impacto |
| 2,0 | 5 | as oito folhas apagam numa varrida da direita pra esquerda (o papel fica em branco) | whoosh |
| 2,5 | 6 | folha 1 imprime (A Pilha) | clique |
| 3,0 | 7 | folha 2 imprime (A Faixa) | clique |
| 3,5 | 8 | folha 3 imprime (A Metade) | clique |
| 4,0 | 9 | folha 4 imprime (A Sobreposição) | clique |
| 4,5 | 10 | folha 5 imprime (O Canto) | clique |
| 5,0 | 11 | folha 6 imprime (A Linha Baixa) | clique |
| 5,5 | 12 | folha 7 imprime (A Moldura) | clique |
| 6,0 | 13 | folha 8 imprime (O Soco) | clique |
| 6,5 | 14 | a seta de swipe pulsa e empurra pra direita | clique |
| 7,0 | 15 | a seta pulsa de novo | clique |
| 7,2–8,0 | 16 | repouso, câmera de volta ao lugar | só música |

## 02 a 09 · os oito layouts · 6 s · 3 compassos (12 batidas)

A mesma coreografia nos oito, na ordem de leitura da referência. O que muda de um pro
outro é a reorganização do texto dentro do cartão: as palavras saem do layout anterior
(ou do "erro", no primeiro) e deslizam pro lugar que este layout manda. É a tese do post.

| t (s) | batida | o que se mexe | som |
|---|---|---|---|
| 0,0 | 1 | repouso: o PNG do slide | música |
| 0,25 | | o círculo levanta (cresce 14%, gira −6°) | |
| 0,5 | 2 | o círculo **carimba**: achata e volta ao redondo | impacto |
| 0,55 | | as palavras do nome caem pra fora, por baixo da máscara | |
| 1,0 | 3 | 1ª parte do nome cai de cima, estica na queda, achata no pouso | clique |
| 1,5 | 4 | 2ª parte do nome cai e pousa | clique |
| 1,75 | | o cartão acelera pra direita e **sai pela borda**; ao passar, apaga as frases | whoosh |
| 2,05 | | o cartão volta **entrando pela esquerda**, já com o texto no layout anterior | (whoosh) |
| 2,5 | 6 | o cartão pousa, com um leve passo além e volta | clique |
| 2,5–3,0 | | uma batida inteira mostrando o texto no lugar errado | |
| 3,0–3,5 | 7–8 | o texto **se reorganiza** pro layout deste slide (cada layout do seu jeito, abaixo) | whoosh (deslizar) |
| 3,5 | 8 | o texto pousa; a 1ª frase sobe da máscara e o 1º fio se desenha | clique |
| 4,0 | 9 | 2ª frase + 2º fio | clique |
| 4,5 | 10 | 3ª frase | clique |
| 4,6 | | a barra laranja levanta | |
| 5,0 | 11 | a barra **carimba** no tempo forte, achata e volta | impacto ("tchac") |
| 5,2–6,0 | 12 | repouso; a foto do cartão, que respirou 2,5%, volta ao tamanho | só música |

A reorganização de cada um (3,0 a 3,5 s):
- **A Pilha** (vem do "erro": texto centrado em cima de mim): as peças caem e se empilham
  na coluna de baixo à esquerda, uma depois da outra, cada uma achatando no pouso.
- **A Faixa** (vem da Pilha): a faixa laranja se estende da esquerda pra direita e o texto
  desliza pra dentro dela.
- **A Metade** (vem da Faixa): a metade laranja sobe de baixo e empurra a foto pra cima.
- **A Sobreposição** (vem da Metade): a metade desce e some; o "CAPA" cresce e sobe até
  ficar atrás de mim no pulo.
- **O Canto** (vem da Sobreposição): tudo encolhe e corre pro canto de cima à esquerda.
- **A Linha Baixa** (vem do Canto): o texto desce e se estende numa linha só no pé.
- **A Moldura** (vem da Linha Baixa): o fio da moldura se desenha e o texto sobe pra
  dentro dela, em cima e embaixo.
- **O Soco** (vem da Moldura): a moldura se apaga, o "CAPA" cresce, fica laranja e cai
  enorme no pé do cartão.

## 10 · CTA · 8 s · 4 compassos (16 batidas)

| t (s) | batida | o que se mexe | som |
|---|---|---|---|
| 0,0 | 1 | repouso: o PNG do CTA | música (com a melodia) |
| 0,5 | 2 | a câmera empurra devagar com parallax (céu e praia, eu e a cadeira), volta em 7,5 s | |
| 1,0 | 3 | as luzes do quiosque piscam | |
| 1,5 | 4 | "LAYOUT" fica selecionado (caixa laranja atrás da palavra) | clique |
| 2,0 | 5 | a palavra é apagada; o cursor pisca | clique |
| 3,0 | 7 | digita **L** (as luzes piscam) | clique (tecla) |
| 3,5 | 8 | digita **A** | tecla |
| 4,0 | 9 | digita **Y** | tecla |
| 4,5 | 10 | digita **O** | tecla |
| 5,0 | 11 | digita **U** (as luzes piscam) | tecla |
| 5,5 | 12 | digita **T** | tecla |
| 6,0 | 13 | o cursor some | |
| 6,5 | 14 | "PRECISA ESTAR SEGUINDO" pulsa | clique |
| 7,0 | 15 | pulsa de novo; as luzes piscam | clique |
| 7,2–8,0 | 16 | repouso | só música |
