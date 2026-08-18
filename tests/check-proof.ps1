$checker = Join-Path $PSScriptRoot "..\tools\check-roles.ps1"
$accepted = & pwsh -NoProfile -File $checker (Join-Path $PSScriptRoot "..\examples\minimal")
if ($LASTEXITCODE -ne 0 -or $accepted -notmatch '^OK ') {
    throw "minimal panel was not accepted"
}

$rejected = & pwsh -NoProfile -File $checker (Join-Path $PSScriptRoot "fixtures\invalid-slug")
if ($LASTEXITCODE -ne 1 -or $rejected -notmatch 'slug must be lowercase kebab-case') {
    throw "invalid slug did not produce the expected structured failure"
}
Write-Output "PASS accepted minimal panel and rejected invalid slug"
