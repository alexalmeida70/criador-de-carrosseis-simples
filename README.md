# criador-de-carrosseis-simples

**Versão simples**, a que vai pros alunos. É a mesma skill `criador-de-carrosseis` sem dois seletores: não tem ajuste de fidelidade (sem referência, o visual é o padrão-base; com referência, a referência manda no visual inteiro, sempre) e não tem escolha de estilo de música no carrossel vivo (uma só, a editorial). A versão completa, com os dois seletores, fica no Design OS.

Skill do Claude Code pra criar carrosséis do Instagram de nível de diretor de arte, do tema à entrega: estratégia, estrutura narrativa em seis posições, copy slide a slide com legenda e CTA, capa em cinco passos, design em código puro (um HTML por slide, texto de verdade, PNG 1080x1350), crítica com notas até ficar bom e, opcionalmente, a versão viva (cada slide em MP4 em loop).

A gramática vem do estudo de 19 carrosséis e 17 reels do @growithalex (Alex, Creative Strategist) mais dois vídeos dele, organizada em três camadas:

| Camada | O que é | Peso |
|---|---|---|
| **Invariantes** | O que faz qualquer carrossel funcionar: as seis perguntas das posições, uma ideia por frase, capa legível em miniatura, CTA como continuação. | Sempre. |
| **Padrão-base** | O default visual e de copy: serifa display gigante, grotesk de apoio, um acento, linho e tecido com textura, fórmulas de capa, slide 2, regra, virada, CTA e legenda. | Ponto de partida. |
| **Variações** | Quando sair do padrão (arquétipo, tom, marca, formato) e como derivar uma fórmula nova a partir do mecanismo. | Só com motivo escrito no BRIEF. |

## Instalar

```bash
git clone <repositório desta versão> ~/.claude/skills/criador-de-carrosseis-simples
```

Depois é só pedir um carrossel no Claude Code (ou chamar `/criador-de-carrosseis-simples`).

## Dependências

- Node com Playwright (o `scripts/novo-projeto.py` liga o `node_modules` de um projeto que já tenha o Playwright; ajuste `PLAYWRIGHT_DIR` se precisar) e o Chrome sem janela do Playwright.
- Python 3 com Pillow (folha de contato e teste de miniatura).
- ffmpeg (só pro carrossel vivo).
- Fontes: Geist, Geist Mono e DM Serif Display (todas OFL) vêm junto em `assets/fonts/`.
- Pro carrossel vivo: Python com numpy, scipy e Pillow; opencv-python só pro `fundo-limpo.py`.
- Higgsfield (opcional) pra gerar a imagem da capa.

## O que não está no repositório

O acervo de referência (`assets/exemplos/`, os slides do @growithalex indexados por posição e fundo) é material com direitos autorais de terceiros e não é redistribuído aqui. A skill funciona sem ele; com ele, o passo de design compara cada slide com exemplos da mesma posição. Se você tiver o acervo local, basta colocá-lo em `assets/exemplos/todos/` com um `indice.md` (veja `references/07-exemplos.md`).

## Estrutura

```
SKILL.md                 briefing (prompt simples → inferir, perguntar só o essencial), fluxo em 9 passos, regras
references/01..10        invariantes · padrão-base · copy · variações · capa e cenas · crítica · exemplos · carrossel vivo · referência dada · atlas de fontes
assets/engine/           kit.js (motor: função pura de t, linho, texto pela base, fit) · anim.js (easing, molas que zeram, peso, parallax)
                         · kit.css (tokens aprovados + anatomia + dispositivos) · dispositivos/ (mesma-capa, layout-slide) · templates de slide
assets/templates/        MARCA.md · BRIEF.md · STORYBOARD.md · guia-de-estilo-exemplo.md · STORYBOARD-exemplo.md
assets/fonts/            Geist · Geist Mono · DM Serif Display (OFL)
assets/acervo/           os carrosséis aprovados do autor, indexados por posição e fundo
assets/exemplos/aprovado o carrossel de referência (folha, cenas, testes) que define "pronto"
scripts/                 novo-projeto.py · render.mjs (stills, cues, frames, video) · folha.py (--lado) · folha-batidas.py · musica.py · baixar-ig.py (post, carrossel ou reel do Instagram → refs/, com os cookies do Chrome logado)
                         periciar.py (mede uma referência) · comparar-pericia.py · fontes.py (Google Fonts, Fontshare) · ocr.swift
                         · testes-vivo.py · fundo-limpo.py · preview.py · vivo.sh · acervo.mjs
evals/                   quatro casos de teste
```

## Carrossel vivo

Depois do estático aprovado: storyboard na grade de 120 BPM, `seek(t)` em cada slide com os acertos declarados, e `zsh scripts/vivo.sh` faz o resto: beats → música sintetizada em numpy (uma só, a editorial: nesta versão não há escolha de estilo) (-14 LUFS, loop circular) → MP4 por slide (quadros direto no ffmpeg) → folhas por batida → testes (quadro 0 = PNG com diferença zero, último quadro = quadro 0, som na emenda) → preview.

Rota: código puro. Sem HyperFrames, sem Remotion, sem Canva.

## Referência dada

Sem referência a skill entrega o padrão-base. Com referência (post, capturas, vídeo), a referência manda no visual inteiro: `scripts/baixar-ig.py URL --nome x` baixa o post do Instagram (precisa de `python3 -m pip install --user gallery-dl` e do Chrome logado no Instagram); `scripts/periciar.py` mede paleta, texto (tamanhos, níveis, alinhamento, margem, entrelinha), preenchimento, área e luz das imagens, textura, formas e anatomia fixa, com as medidas desenhadas por cima dos quadros e recortes das maiores linhas pra identificar a fonte (`references/10-atlas-de-fontes.md`); `scripts/fontes.py` baixa a equivalente livre; `src/kit/marca.css` e `fontes.css` ligam tudo no motor sem reescrever o kit; `scripts/comparar-pericia.py` mede os nossos PNGs contra ela e diz onde olhar; `folha.py --lado refs/frames` põe os dois lado a lado. O protocolo das doze dimensões está em `references/09-referencia.md`, e um guia real de uma referência de outro estilo em `assets/templates/guia-de-estilo-exemplo-referencia-diferente.md`.
