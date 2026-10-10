# Crítica: rubrica, teste de miniatura, anti-aislop

Seja um diretor de arte exigente, não um autor orgulhoso. Olhe a folha de contato e a miniatura de verdade (abra as imagens), não o código.

## Rubrica (nota de 1 a 10 em cada; corrija os 3 piores; repita até tudo ≥ 8)
| Item | O que olhar |
|---|---|
| Gancho na capa | Cria um querer em meio segundo? A palavra gigante lê como forma a 128 px? Tem recibo? |
| Slide 2 paga a capa | Usa a mesma palavra, responde o que a capa abriu, abre o mapa, não insulta, não repete. |
| Espinha | Nenhum slide do meio troca de lugar (fora listicle). Cada um abre o próximo. |
| Ritmo | Passando rápido, a forma muda a cada slide (claro/escuro, cheio/vazio, dispositivo/frase). |
| Virada | Existe um slide que muda o sentido do resto e parece diferente de todos. |
| Payoff e CTA | A crença virou antes do pedido; palavra-chave = tema; entregável com 2 ou 3 partes; sem "segue". |
| Copy | Mediana ≤ 10 palavras por frase; zero pergunta retórica; zero hype; uma linha de print por slide; nomes com artigo. |
| Leitura em miniatura | Todo slide se entende a 390 px; nenhum texto importante abaixo de 36 px no slide (≈ 13 px no celular). |
| Paleta e fontes | Duas fontes; uma cor de destaque por slide; 3 ou 4 cores no total; nada em degradê, glow ou neon. |
| Margens e cantos | 72 px livres; nada nos cantos do contador e do som. |
| Anti-aislop | Veja a lista abaixo. Qualquer item presente derruba a nota pra 5. |
| Semelhança com a referência (só quando houver uma) | Cada mecanismo verificável do `docs/guia-de-estilo.md` está presente? Lado a lado com o quadro equivalente dela: mesma família? `comparar-pericia.py` (nossos PNGs × ela): vazio, margem, níveis, razão, ritmo dos fundos, imagem e cores dentro das tolerâncias? Cada REVISAR é um lugar pra olhar, não uma nota automática. |

## Anti-aislop (o que faz um carrossel parecer "feito por IA")
- Serifa de revista com paleta "bonitinha" e foto fraca ou genérica (o erro da v1 do Orbit).
- Degradê linear de tela cheia, brilho em interface, partículas, neon, ciano.
- Texto em cor de destaque pequeno; mais de uma palavra gigante; três cores de texto.
- Imagem que serviria pra qualquer tema; mockup flutuando num degradê; pessoa "colada" na cena sem sombra nem camada na frente.
- Tudo centralizado e simétrico em todos os slides; nenhum slide muda de forma.
- Frases que explicam em vez de mostrar; adjetivos; pergunta retórica; "no mundo de hoje".
- Ícones genéricos de biblioteca sem função; emojis como decoração.
- Fontes e cores diferentes a cada slide.

## O teste de miniatura (scripts/folha.py gera)
- **Grade de perfil:** a capa recortada em 1:1 a 128 px entre as outras capas do projeto (ou cinza).
- **Feed:** cada slide a 390 px de largura, como no celular.
- Pergunta: em qual deles o olho para? Se a resposta é "nenhum", volte pro passo 4 do fluxo.

## Tabela por rodada (modelo)
| Rodada | Gancho | Slide 2 | Espinha | Ritmo | Virada | CTA | Copy | Miniatura | Paleta | Margens | Aislop |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 8 | 7 | 5 | 8 | 8 | 7 | 6 | 9 | 10 | 8 |
| 2 | 8 | 8 | 8 | 8 | 9 | 8 | 8 | 8 | 9 | 10 | 9 |

Liste os três maiores problemas da rodada com o slide e a correção aplicada.

## As duas perguntas finais (antes de cada entrega)
1. "Isso parece o post de um diretor de arte de primeira linha?" Se não, leve mais longe ou tire.
2. No vivo: "o movimento serve à ideia do slide ou é enfeite?" Tudo que não serve sai. O movimento certo é a tese do post em ação (no post dos layouts, o texto se reorganizando de um layout pro outro É a tese).

## Relatório de entrega (sempre)
Notas por rodada, os três piores problemas corrigidos, os testes (miniatura; no vivo, quadro 0 = PNG com diferença zero, loop e som) e **quanto gastou de créditos no Higgsfield**, cena por cena.
