"""Cria a pasta de um carrossel novo com o motor, os dispositivos, as fontes, os scripts e os templates.
  python3 ~/.claude/skills/criador-de-carrosseis-simples/scripts/novo-projeto.py <pasta-do-projeto> [--marca <MARCA.md>]
Estrutura (a mesma do projeto aprovado "layouts de capa"):
  MARCA.md BRIEF.md docs/ refs/ assets/{fonts,geradas,recortes,identidade} src/kit/ src/slides/ audio/ resultados/{estatico,quadros,folhas,testes} scripts/ preview.html
O Playwright vem por link simbólico (PLAYWRIGHT_DIR ou o projeto Orbit), sem instalar nada."""
import argparse, os, shutil, sys, json
SK = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); HOME = os.path.expanduser('~')
ap = argparse.ArgumentParser(); ap.add_argument('dest'); ap.add_argument('--marca'); a = ap.parse_args()
dest = os.path.abspath(a.dest)
if os.path.exists(dest) and os.listdir(dest): sys.exit(f'{dest} já existe e não está vazia; escolha outra pasta')
for d in ['docs', 'refs', 'assets/fonts', 'assets/geradas', 'assets/recortes', 'assets/identidade', 'src/kit/dispositivos', 'src/slides', 'audio', 'resultados/estatico', 'resultados/quadros', 'resultados/folhas', 'resultados/testes', 'scripts', 'build']:
    os.makedirs(os.path.join(dest, d), exist_ok=True)
E = os.path.join(SK, 'assets', 'engine')
for f in ['kit.js', 'anim.js', 'kit.css']: shutil.copy(os.path.join(E, f), os.path.join(dest, 'src', 'kit', f))
for f in os.listdir(os.path.join(E, 'dispositivos')): shutil.copy(os.path.join(E, 'dispositivos', f), os.path.join(dest, 'src', 'kit', 'dispositivos', f))
shutil.copy(os.path.join(E, 'slide-template.html'), os.path.join(dest, 'src', 'slides', 'slide-template.html'))
shutil.copy(os.path.join(E, 'slide-layout-template.html'), os.path.join(dest, 'src', 'slides', 'slide-layout-template.html'))
for f in ['render.mjs', 'folha.py', 'folha-batidas.py', 'preview.py', 'musica.py', 'testes-vivo.py', 'fundo-limpo.py', 'vivo.sh', 'periciar.py', 'comparar-pericia.py', 'fontes.py', 'ocr.swift']: shutil.copy(os.path.join(SK, 'scripts', f), os.path.join(dest, 'scripts', f))
for f in os.listdir(os.path.join(SK, 'assets', 'fonts')): shutil.copy(os.path.join(SK, 'assets', 'fonts', f), os.path.join(dest, 'assets', 'fonts', f))
# as duas folhas que o projeto edita por cima do motor: fontes baixadas (fontes.py) e tokens da marca/referência
open(os.path.join(dest, 'src', 'kit', 'fontes.css'), 'w').write('/* fontes extras do projeto · gerado por scripts/fontes.py (vazio = só as fontes do padrão-base) */\n')
open(os.path.join(dest, 'src', 'kit', 'marca.css'), 'w').write('''/* marca.css · tokens deste projeto por cima do kit.css. Vazio = padrão-base aprovado.
   Com referência (docs/guia-de-estilo.md) ou MARCA.md próprio, descomente e troque os VALORES:
:root {
  --alta: 'Geist';  --quieta: 'DM Serif';  --mono: 'Geist Mono';  --tracking-alta: -0.045em;  --raio: 0px;
  --papel: #EDE9E1; --marinho: #181D26; --tinta: #15130F; --laranja: #F2511F; --creme: #FBF4E8;
}
.serifa { font-style: normal; }   exemplo: a quieta da referência não é itálica
*/
''')
T = os.path.join(SK, 'assets', 'templates')
shutil.copy(os.path.join(T, 'BRIEF.md'), os.path.join(dest, 'BRIEF.md'))
shutil.copy(os.path.join(T, 'STORYBOARD.md'), os.path.join(dest, 'docs', 'STORYBOARD-modelo.md'))
shutil.copy(a.marca if a.marca and os.path.exists(a.marca) else os.path.join(T, 'MARCA.md'), os.path.join(dest, 'MARCA.md'))
pw = os.environ.get('PLAYWRIGHT_DIR') or os.path.join(HOME, 'carroussel/projetos/orbit-saas-02')
nm = os.path.join(pw, 'node_modules')
if os.path.isdir(os.path.join(nm, 'playwright')): os.symlink(nm, os.path.join(dest, 'node_modules'))
else: print('aviso: playwright não encontrado em', nm, '→ npm i playwright na pasta do projeto')
json.dump({'name': os.path.basename(dest), 'private': True, 'type': 'module'}, open(os.path.join(dest, 'package.json'), 'w'), indent=2)
open(os.path.join(dest, '.gitignore'), 'w').write('node_modules\nbuild\n')
print('projeto criado em', dest)
print('fluxo: MARCA.md + BRIEF.md → (fotos em assets/) → src/slides/slide-NN.html → node scripts/render.mjs stills → python3 scripts/folha.py → python3 scripts/preview.py → [OK] → zsh scripts/vivo.sh')
