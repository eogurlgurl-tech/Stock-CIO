$ErrorActionPreference = "Stop"

python -m pip install --upgrade pyinstaller
python -m PyInstaller --clean --noconfirm STOCK-CIO.spec

$outputDirectory = Join-Path $PSScriptRoot "dist\STOCK-CIO"
$configSource = Join-Path $PSScriptRoot "10_CONFIG"
$configTarget = Join-Path $outputDirectory "10_CONFIG"

Copy-Item `
    -LiteralPath $configSource `
    -Destination $configTarget `
    -Recurse `
    -Force

Write-Host ""
Write-Host "Build completed."
Write-Host "Executable: dist\STOCK-CIO\STOCK-CIO.exe"
Write-Host "Configuration: dist\STOCK-CIO\10_CONFIG"
