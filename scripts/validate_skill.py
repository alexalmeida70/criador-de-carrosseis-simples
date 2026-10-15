#!/usr/bin/env python3
"""Valida a estrutura portátil da skill sem dependências externas."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
AUTHORSHIP = """## Autoria

- Autor: Alex Almeida
- E-mail: alex@maquinaderesultados.com.br
- Site: https://www.maquinaderesultados.com.br
- LinkedIn: https://br.linkedin.com/in/alexalmeida70
- Instagram: https://www.instagram.com/alexalmeida70/"""
REQUIRED = [
    "SKILL.md",
    "README.md",
    "assets/engine/kit.js",
    "assets/templates/BRIEF.md",
    "assets/templates/PROJECT-RULES.md",
    "references/01-invariantes.md",
    "references/10-atlas-de-fontes.md",
    "scripts/novo-projeto.py",
    "scripts/render.mjs",
    "scripts/vivo.sh",
    "scripts/vivo.ps1",
]


def fail(message):
    print(f"ERRO: {message}", file=sys.stderr)
    return 1


def validate_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return fail("SKILL.md não começa com frontmatter YAML")
    try:
        end = lines.index("---", 1)
    except ValueError:
        return fail("frontmatter YAML não foi fechado")
    keys = [m.group(1) for line in lines[1:end] if (m := re.match(r"^([A-Za-z][\w-]*):", line))]
    if keys != ["name", "description"]:
        return fail(f"frontmatter deve conter somente name e description; encontrado: {keys}")
    body = "\n".join(lines[end + 1 :])
    expected = "# Criador de carrosséis (versão simples)\n\n" + AUTHORSHIP
    if expected not in body:
        return fail("a seção de autoria não está exatamente após o título")
    return 0


def validate_markdown_links():
    errors = 0
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for raw in link_re.findall(text):
            target = raw.strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            resolved = (md.parent / unquote(target)).resolve()
            if not resolved.exists():
                errors += fail(f"link relativo inexistente em {md.relative_to(ROOT)}: {raw}")
    return errors


def validate_python_syntax():
    errors = 0
    for source in (ROOT / "scripts").glob("*.py"):
        try:
            compile(source.read_text(encoding="utf-8"), str(source), "exec")
        except SyntaxError as exc:
            errors += fail(f"sintaxe Python inválida em {source.name}:{exc.lineno}: {exc.msg}")
    return errors


def main():
    errors = 0
    text = SKILL.read_text(encoding="utf-8")
    errors += validate_frontmatter(text)
    required_business_context = [
        "Grupo MR | Máquina de Resultados",
        "Para qual unidade de negócio do Grupo MR | Máquina de Resultados este carrossel será criado: Consultores Associados, Marketing Digital ou Eventos?",
        "Nunca infira a unidade",
        "Nunca omita, inverta, una ou exiba mais de uma unidade",
    ]
    for token in required_business_context:
        if token not in text:
            errors += fail(f"regra de unidade de negócio ausente no SKILL.md: {token}")
    novo_projeto = (ROOT / "scripts" / "novo-projeto.py").read_text(encoding="utf-8")
    for token in ["--unidade", "'MRCA'", "'MRD'", "'MRE'", "projeto.json", "PROJECT-RULES.md"]:
        if token not in novo_projeto:
            errors += fail(f"integração por unidade ausente em novo-projeto.py: {token}")
    for relative in REQUIRED:
        if not (ROOT / relative).exists():
            errors += fail(f"arquivo obrigatório ausente: {relative}")
    errors += validate_markdown_links()
    errors += validate_python_syntax()
    forbidden = ["/Library/Caches/ms-playwright", "carroussel/projetos/orbit-saas-02"]
    for token in forbidden:
        if token in (ROOT / "scripts" / "render.mjs").read_text(encoding="utf-8"):
            errors += fail(f"caminho específico de plataforma ainda presente: {token}")
    if errors:
        print(f"Validação falhou com {errors} erro(s).", file=sys.stderr)
        return 1
    print("Skill válida: frontmatter, autoria, estrutura, links e Python conferidos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
