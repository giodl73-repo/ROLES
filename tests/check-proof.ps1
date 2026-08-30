$checker = Join-Path $PSScriptRoot "..\tools\check-roles.ps1"
$pythonChecker = Join-Path $PSScriptRoot "..\tools\check_roles.py"
$minimal = Join-Path $PSScriptRoot "..\examples\minimal"
$invalidSlug = Join-Path $PSScriptRoot "fixtures\invalid-slug"

$accepted = & pwsh -NoProfile -File $checker $minimal
if ($LASTEXITCODE -ne 0 -or $accepted -notmatch '^OK ') {
    throw "minimal panel was not accepted by PowerShell checker"
}

$rejected = & pwsh -NoProfile -File $checker $invalidSlug
if ($LASTEXITCODE -ne 1 -or $rejected -notmatch 'slug must be lowercase kebab-case') {
    throw "invalid slug did not produce the expected PowerShell structured failure"
}

$pythonAccepted = & python $pythonChecker $minimal
if ($LASTEXITCODE -ne 0 -or $pythonAccepted -notmatch '^OK ') {
    throw "minimal panel was not accepted by Python checker"
}

$pythonRejected = & python $pythonChecker $invalidSlug
if ($LASTEXITCODE -ne 1 -or $pythonRejected -notmatch 'slug must be lowercase kebab-case') {
    throw "invalid slug did not produce the expected Python structured failure"
}

Write-Output "PASS accepted minimal panel and rejected invalid slug with both checkers"
