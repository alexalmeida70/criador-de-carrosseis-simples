# Quando o pedido traz uma referência (link, capturas, um post, um vídeo)

## O princípio

Sem referência, a skill entrega o padrão-base (a receita aprovada de `02-padrao-base.md` §1b) e isso já é um resultado bom. **Com referência, a referência manda em tudo que é visível**: fonte, cor, grade, espaçamento, quanto da tela é preenchida, como as imagens são feitas, formas, textura, ritmo. O padrão-base só preenche o que a referência não mostra (um slide de virada que ela não tem, um rodapé que ela não usa). As camadas 1 e 3 continuam mandando no que **não** é visível: estratégia, estrutura em seis posições, copy, legenda, CTA e a rubrica da crítica.

Pega-se a **gramática**. Nunca o conteúdo, as fotos, o nome, o @, os personagens, a legenda ou o copy.

A referência não é um "mood". É uma coisa que se mede. Por isso o caminho é: guardar → medir com a ferramenta → desmontar em doze dimensões num guia com números → ligar os números no motor → testar contra ela em número e no olho.

## 0. O que vem de onde (fixo, não pergunte)

| De onde | O quê |
|---|---|
| **da referência** | tudo que é visível: as 12 dimensões (fonte, cor, grade, espaçamento, preenchimento, hierarquia, imagens e como são feitas, formas, textura, ritmo, movimento) |
| **do MARCA** | @, rodapé, elenco (o rosto é o nosso), idioma, tom |
| **das camadas 1 e 3** | estratégia, estrutura em seis posições, copy, legenda, CTA, rubrica da crítica |

Nesta versão não existe modo "no espírito" nem "só o dispositivo": veio referência, ela manda. Se a conta tem identidade no MARCA e a referência é de outro estilo, siga a referência e escreva no BRIEF: "a referência mandou no visual". Não pergunte "o que você quer da referência": a resposta é tudo.

## 1. Guardar (`refs/`)

| Veio como | Faça |
|---|---|
| Link de post ou carrossel do Instagram | `python3 scripts/baixar-ig.py URL --nome x` → cada slide em `refs/referencia-x/slide-NN.jpg` + `LEIA.md` com autor, data e legenda. Usa o gallery-dl com os cookies do Chrome logado no Instagram (sem login o Instagram não entrega o post; na primeira vez o macOS pode pedir acesso ao Keychain: "Sempre permitir"). Outro navegador: `--navegador safari`. Nunca tente abrir o link com fetch, Playwright ou curl sem cookies: volta HTML vazio. |
| Capturas de tela, imagens soltas | `refs/referencia-<nome>/slide-NN.png` na ordem do carrossel. Se vieram num mosaico, fatie (a largura dividida pelo número de slides). |
| Reel do Instagram | o mesmo `scripts/baixar-ig.py` → `refs/referencia-x/slide-01.mp4`. Rode o periciar no `.mp4`: ele extrai um quadro a cada 0,5 s. |
| Vídeo de outro lugar (YouTube, TikTok) | `yt-dlp -o refs/referencia-<nome>.mp4 URL`. |
| O script falhou (navegador sem login, Keychain negado) | Diga o erro que o script imprimiu e faça a única pergunta permitida nesta rota: "o link não abre aqui; me manda as capturas dos slides?" Só depois de tentar o script. |
| Referência pequena (< 600 px de largura) | Siga, mas avise no BRIEF que cores e tamanhos são aproximados e peça a original se existir. Não espere a resposta pra continuar. |

Escreva em `refs/LEIA.md` o que a pessoa disse sobre a referência, palavra por palavra ("quero esse ritmo", "gostei da fonte"): isso vira os mecanismos verificáveis.

## 2. Medir (`scripts/periciar.py`)

```bash
python3 scripts/periciar.py refs/referencia-x --nome x        # pasta de imagens
python3 scripts/periciar.py refs/referencia-x.mp4 --nome x    # vídeo, um quadro a cada 0,5 s
```

Sai `docs/pericia-x.md` (as tabelas), `docs/pericia-x.json` (tudo), `refs/frames/ref-x-NN.png` (os quadros a 1080 de largura), `refs/frames/pericia-x-NN.jpg` (cada quadro com as medidas desenhadas por cima: caixas de texto com tamanho e nível, área de foto em magenta, formas em laranja, margem, as duas zonas do Instagram em vermelho), `refs/frames/folha-pericia-x.jpg` (tudo numa folha) e `refs/frames/tipo-x-NN-k.png` (as maiores linhas de texto recortadas a 2x, pra identificar a fonte).

O que ela mede: paleta por slide e consolidada (hex, cobertura, papel de cada cor: fundo, tinta, destaque, neutro); texto (linhas, tamanho estimado em px, níveis, caixa alta, alinhamento, margem esquerda, entrelinha, cor e contraste por linha); preenchimento (foto %, texto %, vazio %, bandas vazias nas quatro bordas); imagem (onde, quanto ocupa, se sangra, luminância, saturação, temperatura, grão, nitidez, se há texto em cima); textura do fundo; formas chapadas (tipo, cor, tamanho, raio do canto, se sangra); textos que repetem na mesma posição (a anatomia fixa); invasões dos cantos do Instagram.

O que ela não mede e é olho: **qual é a fonte** (recortes + `10-atlas-de-fontes.md`), **como a imagem foi feita** (foto, 3D, ilustração, colagem, captura de tela), **o dispositivo** de cada slide e **a ideia** que organiza o carrossel. Abra a folha e os recortes de verdade antes de escrever o guia. Se uma máscara ficou errada (a ferramenta chamou de foto um bloco chapado, ou perdeu um texto), diga no guia e corrija o número no olho.

## 3. Desmontar → `docs/guia-de-estilo.md` (modelo real: `assets/templates/guia-de-estilo-exemplo.md`)

Doze dimensões, nesta ordem. Cada uma com o número da perícia, o que o olho viu, e **como vai ser reproduzida no motor**. Adjetivo não serve ("premium", "clean"); número e mecanismo servem.

| # | Dimensão | O que medir / olhar | Onde está | O que escrever no guia | Como reproduzir |
|---|---|---|---|---|---|
| 1 | **A ideia** | o que o carrossel faz em uma frase e por que a estrutura funciona; qual é o dispositivo que repete | olho (a folha) | uma frase + o mapa de slides | estrutura em seis posições (01) com o dispositivo dela |
| 2 | **Formato** | proporção, nº de slides, se é estático ou vídeo | `meta` | 4:5 ou 1:1; quantos slides; estático/vivo | o nosso é sempre 1080×1350; se a referência é 1:1, a grade dela se estende em altura, não se estica |
| 3 | **Paleta** | hex do fundo claro, fundo escuro, tinta, destaque, neutros; quantas cores por slide; onde o destaque aparece (forma ou palavra) e em que tamanho | `paleta consolidada`, coluna `destaque` por slide | tabela hex → papel → regra de uso; contraste fundo/tinta | `src/kit/marca.css`: `--papel --marinho --tinta --laranja --creme` recebem os hex dela (os nomes dos tokens não mudam, só os valores) |
| 4 | **Tipografia** | famílias (recortes + atlas), escala em px por nível, razão maior/menor, pesos, tracking, caixa, alinhamento, entrelinha, qual palavra leva a serifa/itálico (a assinatura) | `escala tipográfica`, `grade`, recortes `tipo-*` | tabela nível → px → peso → caixa → uso; as famílias escolhidas com a equivalente livre e o porquê | `scripts/fontes.py` baixa; `marca.css`: `--alta --quieta --mono --tracking-alta`; `.serifa{font-style}` se a assinatura é reta; os px da escala viram os `fs` de `K.place` |
| 5 | **Grade e espaçamento** | margem esquerda/direita, onde começa o primeiro texto e termina o último, colunas, respiro entre blocos, alinhamento dominante, o que alinha com o quê | `grade`, bandas vazias, sobreposições | diagrama ASCII com px, como em §4 do exemplo | `--margem` e as coordenadas de `K.place`; `.frases`, `.cartao`, `.barra` reposicionados por CSS no slide ou num dispositivo novo |
| 6 | **Preenchimento** | vazio % médio e por tipo de slide; quanto a capa enche vs os internos; texto % e foto % | `preenchimento (curva)` | "capa 5 % de vazio, internos 55 a 65 %"; a curva | a mesma curva no nosso mapa de slides: a crítica confere com o periciar nos nossos PNGs |
| 7 | **Hierarquia** | quantos níveis existem de verdade (3? 6?), a razão entre o maior e o menor, quantas palavras no maior nível, se o maior é uma palavra só ou uma frase | `escala` (níveis, razão), `max_palavras_linha` | "três níveis: 180 / 48 / 22 px, razão 8×; a palavra gigante é uma só" | `K.fit` com o `fs` de cada nível; proibição de nível extra |
| 8 | **Imagens** | quantos slides têm imagem, quanto ocupam, se sangram, luz (luminância), saturação, temperatura, grão, nitidez, se o texto senta em cima e onde; **como foi feita** (foto real: lente, hora do dia, pose; 3D: material, luz de estúdio, sombra; ilustração flat; colagem/recorte; captura de tela de UI; nenhuma) e se há elenco recorrente | `imagens`, bbox por slide, olho | ficha da imagem + **o prompt-molde** (os 4 passos de `05-capa.md`: o que fica igual, a cena com coisas reais, o layout em números, nunca texto) com a luz e o grão medidos ("luminância 0,42, quente, grão de filme"); pra UI e flat: "é código, não imagem" | Higgsfield pela rota de elenco do MARCA com o prompt-molde; `fundo-limpo.py` e recorte pro vivo; UI/flat desenhados em HTML/SVG |
| 9 | **Formas e dispositivos** | barras, pílulas, círculos, cartões, molduras, fios, setas, ícones: cor, tamanho, raio dos cantos, borda, sombra, se sangram; o dispositivo de cada slide (par, tabela, checklist, cartão, frase só) | `formas chapadas`, olho | lista das formas com px e raio; o catálogo de dispositivos dela × o nosso (02 §5) | `--raio`; classes `.pilula .barra .caixa .faixa .par .tabela .check .polaroid` com os valores dela; **dispositivo que o catálogo não tem → arquivo novo em `src/kit/dispositivos/`** |
| 10 | **Textura e acabamento** | liso, grão, linho, papel, ruído, sombra dura ou macia, cantos retos ou redondos, borda | `textura do fundo` (std), olho | "liso" / "grão leve" / "linho"; sombras; cantos | `K.fundoLiso` (liso), `K.grao(host, forca)` (grão), `K.fundoPapel/Marinho` (linho) |
| 11 | **Ritmo dos slides** | sequência de fundos (claro/escuro/foto), onde caem os escuros, tipo por slide, anatomia fixa (cabeçalho, rodapé, numeração: texto e posição) | `ritmo`, `anatomia fixa` | tabela slide × tipo × fundo + a anatomia com px | o mapa de slides do BRIEF copia o compasso; `K.rodape/K.cabecalho` com as posições dela |
| 12 | **Movimento e interface** | se é vídeo: duração dos cortes, o que entra primeiro, easing, o que atravessa a emenda; sempre: o que ela faz nos dois cantos do Instagram | quadros a 0,5 s, `cantos IG` | ordem de leitura (estático) ou tempos medidos (vídeo); o que mudar por causa dos cantos | STORYBOARD (08) com os tempos dela; nunca copiar uma invasão de canto |

Feche o guia com **"Mecanismos verificáveis"**: de 5 a 7 afirmações que qualquer pessoa confere olhando o nosso PNG, sem saber o que você quis fazer. Exemplos bons: "o título tem 7× o tamanho do rodapé e só existem três tamanhos"; "uma única cor de destaque, no máximo duas vezes por slide, nunca abaixo de 90 px"; "a foto ocupa o quadro inteiro na capa e no CTA e 0 % nos internos"; "margem de 96 px, texto alinhado à esquerda em todos os slides"; "vazio entre 55 e 65 % em todo slide interno"; "cantos de 24 px em todo cartão, sombra nenhuma". Esses mecanismos entram na rubrica da crítica (06) como a linha "semelhança com a referência".

## 4. Ligar no motor (sem reescrever o kit)

1. **Fontes:** `python3 scripts/fontes.py --google "..." --fontshare ...` → `assets/fonts/` + `src/kit/fontes.css`.
2. **Tokens:** `src/kit/marca.css` sobrescreve o `:root` do kit: cores, `--alta --quieta --mono --tracking-alta --raio --margem`. Os nomes dos tokens não mudam (o `laranja` pode valer `#B4126A`; o `marinho` pode ser um cinza). Se a referência não tem fundo escuro, o `--marinho` recebe o segundo fundo claro dela e o ritmo do BRIEF não usa "escuro".
3. **Fundo:** `K.fundoLiso(q, 'papel')` pra chapado, `K.grao` pra grão, `K.fundoPapel` pra linho. Nunca imagem de textura.
4. **Grade:** as coordenadas de `K.place` vêm do diagrama do guia. Reaproveite os dispositivos do kit mudando CSS no slide; se o dispositivo dela não existe (uma tabela de três colunas, um "chat", um ticket), escreva `src/kit/dispositivos/<nome>.js` seguindo o padrão de `layout-slide.js` (função que monta e, no vivo, devolve `aplica(u)`).
5. **Imagens:** o prompt-molde do guia é o prompt do Higgsfield; pra UI e ilustração flat, HTML/SVG. Elenco: o rosto é sempre o do MARCA, nunca o da referência.
6. **Interface do Instagram:** as duas zonas e a margem de 72 px valem mesmo quando a referência invade (anote a diferença no guia).

## 5. Plugar no fluxo

- O passo 0 do fluxo (SKILL.md) é este arquivo inteiro: guardar, medir, guia, ligar. Só depois vem a estratégia.
- O BRIEF ganha a seção **1b. Referência**: caminho do guia e a tabela "o que | da referência | do MARCA | do padrão-base". Cada item do padrão-base que ficou (ex.: a virada em frase só, que a referência não tem) é uma variação com motivo.
- No passo 5 (design), os exemplos a abrir antes de cada slide são os **quadros dela** (`refs/frames/ref-x-NN.png`), não o acervo do Alex. O acervo entra só pra resolver o que a referência não mostra.
- No passo 6 (crítica), a rubrica ganha a linha "semelhança com a referência" (06) e o teste numérico abaixo.

## 6. Testes de aceite (número e olho)

1. **Número:** rode o periciar nos nossos PNGs e compare com o dela:
   ```bash
   python3 scripts/periciar.py resultados/estatico --nome nosso
   python3 scripts/comparar-pericia.py docs/pericia-x.json docs/pericia-nosso.json
   ```
   O comparador imprime lado a lado vazio médio, margem, entrelinha, níveis e razão, ritmo dos fundos, ocupação de foto, textura e as cores principais, com OK ou REVISAR por linha (tolerâncias: vazio ±12 pontos, margem ±16 px, razão ±25 %, cor ΔRGB ≤ 34). REVISAR não é reprovação automática: é onde olhar.
2. **Olho:** o nosso slide ao lado do quadro equivalente dela, na mesma escala (`scripts/folha.py` aceita `--lado refs/frames`). Mesma família? Se não, não está pronto. Depois a miniatura a 128 px dos dois lados.
3. **Mecanismos:** cada um dos 5 a 7 do guia, marcado presente ou ausente.
4. **Troca de tema:** a nossa capa serviria pra outro tema? Então a imagem é fraca, mesmo que a gramática esteja igual.

## 7. O que nunca vem da referência

Conteúdo, frases, fotos, o rosto, o nome, o @, o cabeçalho, a legenda, os números de prova. Copy e legenda vêm de `03-copy.md`; a prova vem da conta. Se a referência é de um concorrente direto, a gramática ainda pode ser usada: o que não pode é ficar reconhecível como cópia (o teste: alguém olhando os dois lado a lado diria "é o mesmo post"? Então mudou pouco a ideia, não só o texto).
