# A capa: cinco passos, dois testes, três rotas de elenco

A capa é vista do tamanho de um selo, sem som, sem movimento, sem autoplay. Alguém precisa decidir apertar. Os cinco passos vêm do vídeo "How I Create Visual Hooks" do Alex; cada passo gera um asset e eles se empilham.

## Os cinco passos (nesta ordem; o texto entra por último)
1. **Mundo (o fundo).** O lugar onde a capa vive, ainda sem ninguém e sem texto. Nunca a ilustração do tema: pares de fontes → deserto de sal; storytelling → campo ao entardecer; arquétipos → carro em chamas no meio do nada. A distância entre o que se vê e o que a palavra diz é o que faz parar. Decida AGORA onde o texto vai sentar: o fundo precisa de espaço vazio pra ele (céu limpo no topo, chão liso embaixo). Objetos que fazem parte do lugar (a cadeira, a mesa) entram aqui. Inspiração por palavras do CENÁRIO (não do tema) em cosmos.so, Pinterest, capas de disco, pôsteres de cinema, capas de revista; anote quatro referências e o que gosta em cada uma (horizonte baixo, dois tons, sol duro, sombra nítida); a lista vira o prompt.
2. **Sujeito.** UMA coisa que as pessoas olham, reconhecível antes de ler (reconhecer é mais rápido que ler). Personagem famoso é difícil na IA: use o cenário ou um objeto do universo (um dragão, uma cadeira de cozinha, um tomate em cima da TV). Gere a partir da imagem do passo 1 como referência, pra que luz, chão e céu fiquem iguais.
3. **Contraste e profundidade.** Começa com "onde vai o texto?" e constrói contraste entre texto e fundo (branco sobre branco some). Puxe a cor por referência + prompt (laranja escuro embaixo, azul no topo). Profundidade: algo NA FRENTE do sujeito, fora de foco, cortado pela borda inferior (flores, capim, uma mesa). "Duas camadas é gráfico. Três camadas é fotografia."
4. **Prova na cena.** O trabalho ou o produto entra como objeto dentro da cena, com sombra e luz reais: capas antigas no chão, penduradas num varal, flutuando como cartões. Nunca um mockup num degradê. Gere referenciando a cena + as imagens da prova; escolha a saída limpa. Tamanho e posição se ajustam depois, em código ou na ferramenta de camadas do Higgsfield.
5. **Tipo.** As palavras vão no espaço que a imagem deixou. Duas fontes. Uma palavra grande demais; o resto cai pra pequeno. Em código, sempre: texto de verdade. "Se precisa ser lido pra funcionar, não funciona."

## Os dois testes (antes de aprovar)
1. **Miniatura:** `scripts/folha.py` gera a capa a 128 px dentro de uma grade e a 390 px como no feed. A palavra gigante lê como forma? O sujeito separa do fundo?
2. **Troca de tema:** esta imagem serviria pra qualquer outro tema? Se sim, é foto de banco com palavras. Um astronauta numa cadeira de cozinha no deserto de sal só funciona ali.

## Fórmula de prompt pra imagem (do reel dele sobre o ChatGPT Image 2.5)
1. **O que fica igual**, nomeado um por um (o homem, o céu, a ovelha, a cor, o enquadramento). "Mantenha a imagem igual" é ignorado; a lista não.
2. **A cena** com coisas reais, não adjetivos: iPhone, 16 mm, Kodak Portra, golden hour, blue hour, horizonte baixo, sombra dura. "Cinematográfico" sozinho é o que deixa fake.
3. **O layout em números:** "o sujeito ocupa o terço inferior", "céu vazio nos 40% de cima". "Em destaque" é ignorado; número é seguido.
4. **Nunca peça texto.** Todo texto é desenhado em código.
Gere em 1K ou 2K (upscale depois). Duas variações por cena; escolha a limpa (sombra boa, nada estranho).

## As três rotas de elenco
| Rota | Quando | Como |
|---|---|---|
| **Sem rosto** | marca que não é pessoa, tom premium, ou quando o tema pede objeto/personagem | sujeito = objeto do universo ou figura anônima (de costas, pequena, de capacete). É a rota do astronauta e do pinguim. |
| **Foto de referência** | a pessoa vai aparecer em poucas capas; teste de direção | uma foto boa da pessoa como referência no Nano Banana Pro ou GPT Image 2.5: "a mesma pessoa desta foto, [cena]". Se o rosto vier diferente, gere de novo só aquela. |
| **Soul (Higgsfield)** | a pessoa é o personagem recorrente da conta (capas e CTA por meses) | `higgsfield soul-id create` com 10 a 15 fotos variadas (skill `higgsfield-soul-id`); depois `--soul-id` em toda geração. Variante cinematic serve pro vivo. |

Em qualquer rota: duas variações por cena, folha de contato das escolhidas em `assets/`, versão com fundo removido quando a pessoa vai ser animada em camadas (`higgsfield-generate` remove fundo por 1 crédito). Custos de referência (out/2026): GPT Image 2.5 high 2k ≈ 2,75 créditos; Nano Banana Pro 2k ≈ 2; remover fundo 1.

## Sem Higgsfield (ou sem créditos)
Capa tipográfica: cor chapada de papel ou escuro texturizado (o motor desenha grão com semente), uma palavra gigante, a linha editorial de prova acima da assinatura institucional e um elemento gráfico só (uma linha, um círculo, uma etiqueta). Funciona pra listicle e pra tom institucional. Não funciona pra "mundo": aí a capa precisa de imagem.

## As cenas (quando há elenco): os três briefs que funcionaram
No projeto aprovado "a mesma capa, oito layouts" as fotos foram geradas no Higgsfield pela rota **foto de referência** (quatro fotos da pessoa em `assets/identidade/` do projeto: frontal, perfil, três quartos, corpo). Luz de fim de tarde, quente, cinematográfica, 4:5 ou maior, duas variações por cena. O molde de cada cena:

1. **A capa (mundo + sujeito + prova):** a pessoa sentada ou agachada no chão de uma paisagem aberta (estrada deserta, descampado de terra), golden hour, céu escurecendo pro marinho no alto (o espaço do título), segurando uma folha, com as outras folhas em leque no chão à frente. As folhas podem vir em branco: o conteúdo delas é desenhado em código por cima, em perspectiva. Roupa escura simples, olhando pra câmera, sem sorriso forçado. A prova (o trabalho) entra como objeto na cena, com sombra real.
2. **A "mesma capa" (a foto que recebe os layouts / a prova em par):** a pessoa em movimento, pequena no quadro, muito céu e espaço vazio em cima, embaixo e dos lados: correndo num campo contra o sol, pulando do teto de um carro antigo, de perfil numa rocha, no fim de um píer. Precisa de espaço limpo porque o texto vai sentar em oito lugares diferentes. Uma foto a cada dois slides dá variedade sem perder a comparação.
3. **O CTA (o set recorrente de fechamento):** a pessoa sentada numa cadeira, de perfil ou três quartos, na frente de um quiosque ou bar de praia com a luz quente acesa, céu de fim de tarde, espaço livre pro texto no alto. A luz do quiosque vira uma camada que pisca na batida no vivo.

Escreva cada cena assim no BRIEF: lugar · hora e luz · pose e roupa · o que está na mão ou no chão (a prova) · onde fica o espaço vazio pro texto · o que NÃO pode aparecer (texto, logos). Depois o prompt segue a fórmula acima (o que fica igual, coisas reais, layout em números, nunca texto).

## O set recorrente (o "mundo" da conta)
Toda capa volta ao mesmo tipo de lugar até ele virar da conta (regra "world" do Alex). No `MARCA.md` fica o set e a cena do CTA; se a conta ainda não tem, proponha um no BRIEF a partir do tema e registre como "a confirmar". No exemplo do `MARCA.md` (a conta do autor), o set aprovado é a paisagem aberta ao entardecer (estrada, campo, descampado, píer) e o CTA é o quiosque de praia.

## Preparo das fotos pro vivo (camadas)
- **Recorte sem fundo** da pessoa (Higgsfield remove fundo, 1 crédito) → `assets/recortes/cenaN-pessoa-sem-fundo.png`.
- **Fundo limpo** (a cena sem a pessoa, pro parallax descobrir só o entorno): `python3 scripts/fundo-limpo.py foto recorte saída [manter.json]` pinta o buraco com o entorno; `manter.json` protege regiões que não podem ser pintadas (as folhas no chão).
- **Camada de luz** (opcional, CTA): só os pontos quentes do quiosque com halo, salva como PNG com alpha, entra em `mix-blend-mode: screen` e pisca na batida.
- **Upscale** do que vier mole; **folha de contato** das escolhidas em `assets/folha-fotos-escolhidas.jpg`; as descartadas ficam em `assets/geradas/`.

## Perguntar ou inferir
Infira sozinho: o set (do tema e do MARCA), a pose, a luz, o layout da capa, a prova na cena, quantas variações. Pergunte só quando mudar o resultado: se a pessoa aparece ou não (e qual rota de elenco), e o teto de créditos se o pedido não disser. Com a resposta, gere tudo de uma vez e mostre a folha de contato das escolhidas; a pessoa troca uma cena se quiser.
