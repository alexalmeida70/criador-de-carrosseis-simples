param(
    [string]$Slides = "all"
)

$ErrorActionPreference = "Stop"

function Invoke-Step {
    param([string]$Program, [string[]]$Arguments)
    & $Program @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Falha ao executar: $Program $($Arguments -join ' ')"
    }
}

$python = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } elseif (Get-Command python -ErrorAction SilentlyContinue) { "python" } else { throw "Python não encontrado no PATH." }
$pythonPrefix = if ($python -eq "py") { @("-3") } else { @() }

Invoke-Step "node" @("scripts/render.mjs", "cues")
Invoke-Step $python ($pythonPrefix + @("scripts/musica.py"))
Invoke-Step "node" @("scripts/render.mjs", "video", $Slides)

New-Item -ItemType Directory -Force -Path "resultados/folhas" | Out-Null
Get-ChildItem -Directory "resultados/quadros" -Filter "slide-*" | ForEach-Object {
    $out = Join-Path "resultados/folhas" ($_.Name + "-batidas.jpg")
    Invoke-Step $python ($pythonPrefix + @("scripts/folha-batidas.py", $_.FullName, $out))
}

Invoke-Step $python ($pythonPrefix + @("scripts/testes-vivo.py"))
Invoke-Step $python ($pythonPrefix + @("scripts/preview.py"))
Write-Output "vivo pronto: resultados/slide-NN.mp4 · resultados/folhas/ · resultados/testes/ · preview.html"
