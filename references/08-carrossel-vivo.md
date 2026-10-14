# Carrossel vivo: do estático aprovado ao MP4 em loop

Só depois do estático aprovado. O quadro 0 de cada MP4 é EXATAMENTE o PNG aprovado (diferença zero, pixel por pixel); o resto é o movimento voltando ao repouso. As regras do formato estão na seção seguinte. O projeto aprovado que fixou este método: "a mesma capa, oito layouts" (STORYBOARD em `assets/templates/STORYBOARD-exemplo.md`, folhas e testes em `assets/exemplos/aprovado/`).

## O formato
- Um MP4 por slide, 1080×1350, 30 fps, H.264 yuv420p bt709, com o próprio som em -14 LUFS. Loop sem emenda em compassos inteiros a 120 BPM: capa e CTA com 8 s, cartões internos com 6 s (4 s só pra slides de uma frase).
- Tudo é função pura do tempo t (`window.seek(t)`): sem timers, sem requestAnimationFrame no render, ruído só com semente. O render fotografa fora de ordem de propósito.
- Último quadro = quadro 0: todo efeito termina ou volta ao repouso antes do fim; nenhum acerto nos últimos 0,8 s; a "respiração" da foto termina em 5,5 s num slide de 6 s; molas com `A.mola` (zera exatamente em `dur`).
- Sem HyperFrames, sem Remotion. Um HTML por slide, Playwright fotografa, ffmpeg cola.

## As três regras do movimento
Suavidade (nada linear: `A.outC`, `A.inOutC`, `A.sino`) · Peso (o que cai estica na queda e achata no pouso, volume constante: `A.volume`, `A.carimbo`) · Ritmo (uma batida a cada 0,5 s; todo acerto numa batida; o tempo forte pra o carimbo da barra).

## A ordem de leitura vira a ordem do movimento
Num slide estático o olho já tem um caminho (número → nome → subtítulo → cartão → frases → barra). O vivo percorre esse caminho na grade, uma coisa por batida. É o que faz o movimento "servir à ideia" em vez de enfeitar.

## Catálogo de movimento por tipo de slide (o que funcionou)
| Slide | Coreografia (t em s, 120 BPM) | Som |
|---|---|---|
| **Capa fotográfica** (8 s) | 0,5 a 7,5: a câmera empurra devagar com parallax em três camadas (fundo limpo 4%, pessoa recortada 5,5%, título 7%) e volta ao repouso (`A.parallax`). 1,0: a palavra-assinatura em serifa sobe esticando e carimba. 2,0: as props do chão (folhas, capas) apagam numa varrida; 2,5 a 6,0: imprimem uma por batida, cada uma com o seu conteúdo. 6,5 e 7,0: a seta de swipe pulsa e empurra pra direita. | impacto no carimbo; whoosh na varrida; um clique por folha (escala pentatônica subindo); cliques na seta |
| **Cartão de regra / layout** (6 s, `dispositivos/layout-slide.js`) | 0,25 a 0,5: o círculo levanta (cresce 14%, gira −6°) e carimba no 0,5. 0,55: as palavras do nome caem pra fora por baixo de uma máscara; 1,0 e 1,5: cada parte cai de cima, estica na queda e achata no pouso (pra direita, pra não comer o espaço). 1,75 a 2,05: o cartão acelera pra direita e sai pela borda, apagando as frases; 2,05 a 2,5: volta pela esquerda com sobrepasso, já com o estado ANTERIOR (o erro, ou o layout do slide anterior). 2,5 a 3,0: uma batida mostrando o estado errado. 3,0 a 3,5: o texto SE REORGANIZA pro estado deste slide (cada layout do seu jeito: a Pilha cai e empilha; a Faixa se estende; a Metade sobe; o Soco cresce, fica laranja e cai). 3,5, 4,0, 4,5: as frases sobem de uma máscara, uma por batida, com o fio se desenhando. 4,6 a 5,0: a barra levanta e carimba no tempo forte. 5,2 a 6,0: repouso. | impacto (número), clique ×2 (nome), whoosh (cartão atravessa), clique (cartão pousa), whoosh (reorganiza), clique ×3 (frases), tchac (barra) |
| **Slide de par ✗/✓** | o lado ✗ entra primeiro e fica uma batida; o lado ✓ chega com carimbo; a legenda de cada um desliza de baixo; o fecho carimba no tempo forte. | clique, impacto, clique, tchac |
| **Slide só texto / virada** | a frase entra em duas batidas por palavras pesadas (cada uma cai e achata); a etiqueta-soma desliza em cima; nada mais. | clique por palavra, impacto na última |
| **Slide tabela / checklist** | linhas entram uma por batida de baixo com clip; os ✓ estalam. | clique, pop |
| **CTA fotográfico** (8 s) | 0,5 a 7,5: parallax da cena. 1,0: a luz do quiosque pisca (camada em screen). 1,5: a palavra-chave fica selecionada (caixa laranja atrás); 2,0: é apagada, o cursor pisca; 3,0 a 5,5: digita letra a letra, uma por batida, as luzes piscam junto; 6,0: o cursor some; 6,5 e 7,0: "precisa estar seguindo" pulsa. | clique (seleção, apagar), tecla por letra, cliques no pulso |
| **Entre slides** | algo atravessa a borda: o cartão sai pela direita do slide N e entra pela esquerda do N+1 já começando a se reorganizar; a trajetória do rodapé continua; a música segue nos compassos seguintes. | whoosh |

Proibido (CLAUDE.md): tudo entrando com fade, brilho, neon, partícula. Entradas por carimbo (escala com peso), por deslize com easing, por máscara (clip) e por desenho do fio.

## Som
- Três famílias resolvem um carrossel: **impacto** (carimbo do número, "tchac" da barra), **whoosh** (cartão atravessando, texto deslizando), **clique** (pousos, frases, folhas, teclas). Cada slide declara os seus em `K.slide({ cues: [{ t, tipo, o_que }] })`; `render.mjs cues` escreve `audio/beats.json`; `musica.py` lê e sintetiza.
- Música: uma só, quente e mínima, em ré menor, 120 BPM: pad + piano elétrico em FM + baixo com harmônicos + bumbo macio, sino nos slides da segunda metade. Progressões que resolvem de volta no primeiro acorde em 4, 3 ou 2 compassos, então cada loop fecha e o swipe pro próximo também. Cada slide pega os compassos seguintes. Nesta versão não há escolha de estilo; ajuste fino só em TOM e CLIMA no topo do `musica.py`.
- Loop perfeito: as caudas que passam do fim voltam pro começo; os filtros rodam em círculo (o trecho repetido três vezes, fica o do meio), então a emenda soa como qualquer virada de compasso. Limitador com pico entre amostras; -14 LUFS medido com ffmpeg; energia por banda conferida (o celular precisa de harmônicos no grave e "tapa" no médio).

## Ferramentas (todas em `scripts/`, copiadas pelo `novo-projeto.py`)
1. `node scripts/render.mjs cues` → `audio/beats.json` (duração e acertos de cada slide).
2. `python3 scripts/musica.py` → `audio/slide-NN.wav`, `musica-completa.wav`, `loudness.json`.
3. `node scripts/render.mjs video [all|02]` → `resultados/slide-NN.mp4` (quadros direto no ffmpeg com o áudio) e `resultados/quadros/slide-NN/` (quadro 0, último e um por batida).
4. `python3 scripts/folha-batidas.py resultados/quadros/slide-NN resultados/folhas/slide-NN-batidas.jpg` → folha por batida.
5. `python3 scripts/testes-vivo.py` → `resultados/testes.json` e as duas imagens em `resultados/testes/`: quadro 0 = PNG (diferença e PSNR do MP4), último quadro = quadro 0, som na emenda × compasso interno, formato do MP4.
6. `python3 scripts/preview.py` → `preview.html` com os MP4 em ordem e botão "tocar todos com som".
Tudo de uma vez:

- Windows: `powershell -ExecutionPolicy Bypass -File scripts/vivo.ps1 [all|02,03]`
- macOS/Linux: `zsh scripts/vivo.sh [all|02,03]`

## Storyboard (`assets/templates/STORYBOARD.md`, exemplo real em `STORYBOARD-exemplo.md`)
Pra cada slide: duração em compassos, compassos da música, e uma linha por batida: tempo, o que se mexe, o som. Escreva a partir do catálogo acima e da ordem de leitura do slide. Mostre e espere o OK antes de animar.

## Armadilhas (cada uma custou uma rodada)
1. O pouso da segunda palavra do nome achatando pros dois lados come o espaço entre as palavras: achate pra direita (`transformOrigin: 0% 100%`), com metade da força.
2. O loop não fecha se a foto do cartão ainda "respira" no último quadro: a respiração termina em 5,5 s (`A.sino(t / 5.5)`), e o último quadro tem que dar 0 pixel de diferença.
3. Som com degrau na emenda e abafado no celular: filtros em círculo, grave abaixo de 120 Hz em ~17% da energia (não 54%), agudo acima de 2 kHz em ~3,5%, pico medido entre amostras.
4. Nunca `will-change: transform`: o Chrome reaproveita textura numa escala antiga e o texto borra.
5. Chrome com `--disable-gpu --force-color-profile=srgb`: renders idênticos entre rodadas (o teste quadro 0 = PNG depende disso).
6. `fetch` de JSON e fontes não funcionam por `file://`: o `render.mjs` serve a pasta por HTTP.

## Entrega do vivo
`resultados/slide-NN.mp4`, `resultados/quadros/`, `resultados/folhas/` (por batida), `resultados/testes/` + `testes.json`, `preview.html`, tabela de notas por rodada (gancho no quadro 0, leitura no celular, suavidade, peso, sincronia do som, loop sem emenda, margens) e o relatório de créditos gastos. Lembrar: subir os MP4 na ordem, sem música do Instagram por cima.
