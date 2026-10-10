#!/usr/bin/env node
// Acervo próprio da skill (assets/acervo/): slides dos seus carrosséis aprovados, no mesmo formato do
// acervo de referência (todos/NNN-sMM.jpg a 540 px, indice.md por posição e fundo, licoes.md).
//
//   node scripts/acervo.mjs add <pasta-do-projeto> --post 104 --titulo "nome do carrossel" \
//        --posicoes capa,slide2,regra,regra,regra,virada,cta [--destaques 1,2,3,6,7] [--padrao "resultados/estatico/slide-*.png"]
//   node scripts/acervo.mjs list
//
// Posições: capa · slide2 · regra · listicle · virada · cta. O fundo (claro / escuro / foto) é medido por
// luminância e variação; confira na imagem. Depois de adicionar, escreva as primeiras palavras de cada
// slide no indice.md e a lição de cada destaque no licoes.md (uma linha por arquivo, como no 07-exemplos.md).
// Só macOS por enquanto: usa o `sips` do sistema pra redimensionar e medir.
import fs from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..", "assets", "acervo");
const POSITIONS = ["capa", "slide2", "regra", "listicle", "virada", "cta"];
const labels = { capa: "capa (open)", slide2: "slide 2 (hold)", regra: "regra/interno (spine)", listicle: "listicle (item)", virada: "virada ou fecho", cta: "CTA (payoff)" };
const patterns = ["resultados/estatico/slide-*.png", "slide-*.jpg", "slide-*.png", "carousel-preview/*/[0-9]*.png", "build/frames/s*/f_0000.png"];

const args = process.argv.slice(2);
const command = args.shift();
const option = name => { const i = args.indexOf(`--${name}`); return i >= 0 ? args[i + 1] : undefined; };

async function glob(folder, pattern) {
  // Minimal glob: one wildcard segment per path part.
  const parts = pattern.split("/");
  let current = [folder];
  for (const part of parts) {
    const next = [];
    for (const dir of current) {
      let names = [];
      try { names = await fs.readdir(dir); } catch { continue; }
      const re = new RegExp("^" + part.replace(/[.+^${}()|\\]/g, "\\$&").replace(/\*/g, ".*").replace(/\[0-9\]/g, "[0-9]") + "$");
      for (const name of names.sort()) if (re.test(name)) next.push(path.join(dir, name));
    }
    current = next;
  }
  return current;
}
async function findPages(folder, pattern) {
  for (const p of pattern ? [pattern] : patterns) {
    let files = await glob(folder, p);
    if (p.startsWith("carousel-preview")) {
      // The newest preview folder only, pages in numeric order.
      const byFolder = new Map();
      for (const f of files) { const k = path.dirname(f); (byFolder.get(k) || byFolder.set(k, []).get(k)).push(f); }
      const newest = [...byFolder.keys()].sort().at(-1);
      files = newest ? byFolder.get(newest).sort((a, b) => parseInt(path.basename(a)) - parseInt(path.basename(b))) : [];
    }
    if (files.length) return files;
  }
  return [];
}
function sips(...a) { return execFileSync("/usr/bin/sips", a, { stdio: ["ignore", "pipe", "ignore"] }).toString(); }
async function convert(src, out) {
  await fs.mkdir(path.dirname(out), { recursive: true });
  sips("-z", "675", "540", src, "--setProperty", "format", "jpeg", "--setProperty", "formatOptions", "85", "--out", out);
}
// Background class from a 24x30 BMP thumbnail. A flat page (paper or dark cloth) concentrates its
// pixels in one luminance band even with cards and photos on it; a full-bleed photo spreads them out.
async function background(file) {
  const tmp = path.join(os.tmpdir(), `acervo-${process.pid}-${Date.now()}.bmp`);
  sips("-z", "30", "24", file, "--setProperty", "format", "bmp", "--out", tmp);
  const bmp = await fs.readFile(tmp); await fs.rm(tmp, { force: true });
  const offset = bmp.readUInt32LE(10), width = bmp.readInt32LE(18), height = Math.abs(bmp.readInt32LE(22)), bpp = bmp.readUInt16LE(28) / 8;
  const rowSize = Math.ceil(width * bpp / 4) * 4;
  const bins = new Array(12).fill(0);
  let count = 0;
  for (let y = 0; y < height; y++) for (let x = 0; x < width; x++) {
    const i = offset + y * rowSize + x * bpp, b = bmp[i] / 255, g = bmp[i + 1] / 255, r = bmp[i + 2] / 255;
    const lum = 0.2126 * r + 0.7152 * g + 0.0722 * b;
    bins[Math.min(11, Math.floor(lum * 12))]++; count++;
  }
  // Share of the dominant band plus its neighbours: the "flat" area of the page.
  const mode = bins.indexOf(Math.max(...bins));
  const flat = (bins[mode] + (bins[mode - 1] || 0) + (bins[mode + 1] || 0)) / count;
  if (flat < 0.55) return "foto";
  return mode < 5 ? "escuro" : "claro";
}

async function add() {
  const folder = args.find((a, i) => !a.startsWith("--") && !(i > 0 && args[i - 1].startsWith("--")));
  const post = option("post"), title = option("titulo"), positions = (option("posicoes") || "").split(",").map(s => s.trim()).filter(Boolean);
  const highlights = (option("destaques") || "").split(",").map(s => parseInt(s)).filter(Number.isInteger);
  if (!folder || !/^\d+$/.test(post || "") || !title) throw Error("Use: add <pasta> --post NNN --titulo \"…\" --posicoes capa,slide2,regra,…");
  const pages = await findPages(path.resolve(folder), option("padrao"));
  if (!pages.length) throw Error(`Nenhuma página encontrada em ${folder} (padrões: ${patterns.join(", ")}).`);
  if (positions.length && positions.length !== pages.length) throw Error(`${pages.length} páginas e ${positions.length} posições.`);
  for (const p of positions) if (!POSITIONS.includes(p)) throw Error(`Posição inválida: ${p}`);
  const auto = i => i === 0 ? "capa" : i === pages.length - 1 ? "cta" : i === 1 ? "slide2" : i === pages.length - 2 && pages.length >= 5 ? "virada" : "regra";
  const rows = [], rhythm = [];
  for (const [i, src] of pages.entries()) {
    const n = String(i + 1).padStart(2, "0"), file = `${post}-s${n}.jpg`, out = path.join(root, "todos", file);
    await convert(src, out);
    const bg = await background(out), position = positions[i] || auto(i);
    rhythm.push(bg);
    rows.push(`- \`${file}\` · ${labels[position]} · fundo ${bg} · (primeiras palavras do slide)`);
    const first = !rows.slice(0, -1).some(r => r.includes(labels[position]));
    if (highlights.includes(i + 1) || (!highlights.length && first)) await fs.copyFile(out, path.join(root, `${position}-${file}`));
  }
  const indexFile = path.join(root, "indice.md");
  let index = "";
  try { index = await fs.readFile(indexFile, "utf8"); } catch { index = `# Acervo próprio · slides dos carrosséis aprovados a 540 px (\`todos/NNN-sMM.jpg\`)\n\nMesmo uso do acervo de referência: escolha exemplos por posição e fundo antes de desenhar e tire um atributo de cada. Legenda: **fundo** claro / escuro / foto (medido; confira na imagem); **texto** = primeiras palavras do slide. Lições de cada destaque em \`licoes.md\`.\n`; }
  if (index.includes(`## Post ${post} ·`)) throw Error(`O post ${post} já está no índice.`);
  index = index.trimEnd() + `\n\n## Post ${post} · ${title} · ${pages.length} slides · ritmo: ${rhythm.join(" → ")}\n${rows.join("\n")}\n`;
  await fs.writeFile(indexFile, index, "utf8");
  const lessonsFile = path.join(root, "licoes.md");
  let lessons = "";
  try { lessons = await fs.readFile(lessonsFile, "utf8"); } catch { lessons = "# O que cada destaque do acervo próprio ensina\n\nUma linha por arquivo de destaque (`posição-NNN-sMM`), no formato do 07-exemplos.md.\n\n| Arquivo | O que ensina |\n|---|---|\n"; }
  const added = (await fs.readdir(root)).filter(f => new RegExp(`^(${POSITIONS.join("|")})-${post}-s\\d+\\.jpg$`).test(f)).sort();
  lessons = lessons.trimEnd() + "\n" + added.map(f => `| ${f.replace(/\.jpg$/, "")} | (escreva a lição) |`).join("\n") + "\n";
  await fs.writeFile(lessonsFile, lessons, "utf8");
  console.log(`Post ${post} · ${pages.length} slides → ${path.relative(process.cwd(), root)} · ritmo ${rhythm.join(" → ")} · destaques: ${added.join(", ")}\nAgora preencha as primeiras palavras em indice.md e as lições em licoes.md.`);
}
async function list() {
  let index = ""; try { index = await fs.readFile(path.join(root, "indice.md"), "utf8"); } catch { console.log("Acervo próprio vazio."); return; }
  for (const line of index.split("\n")) if (line.startsWith("## Post")) console.log(line.slice(3));
}
try {
  if (command === "add") await add();
  else if (command === "list") await list();
  else { console.log("Use: node scripts/acervo.mjs add <pasta> --post NNN --titulo \"…\" --posicoes … | list"); process.exit(1); }
} catch (error) { console.error(error.message); process.exit(1); }
