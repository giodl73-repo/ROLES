param()

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot

function Read-RepoFile {
  param([string]$Path)
  Get-Content -LiteralPath (Join-Path $repoRoot $Path) -Raw
}

function Assert-Contains {
  param(
    [string]$Text,
    [string]$Needle,
    [string]$Label
  )

  if (-not $Text.Contains($Needle)) {
    throw "Missing '$Needle' in $Label."
  }
}

function Normalize {
  param([string]$Text)
  ($Text -replace '`', '' -replace '\s+', ' ').Trim()
}

$pitfalls = Read-RepoFile ".pitfall\roles-pitfalls.md"
foreach ($needle in @(
  "ROLES-PF-04",
  "ROLES-PF-05",
  "MITIGATED",
  "docs/pitfall-boundaries.v1.json",
  "tests/check-pitfall-policy.ps1"
)) {
  Assert-Contains $pitfalls $needle ".pitfall\roles-pitfalls.md"
}

$manifest = Read-RepoFile "docs\pitfall-boundaries.v1.json"
foreach ($needle in @(
  "ROLES-PF-04",
  "ROLES-PF-05",
  "mandatory global governance",
  "required parliament/editorial/stakeholders tiers",
  "generic checks replace repository evidence",
  "independent open-source proof",
  "organizational behavior proof",
  "external ecosystem generalization"
)) {
  Assert-Contains $manifest $needle "docs\pitfall-boundaries.v1.json"
}

$spec = Read-RepoFile "SPEC.md"
Assert-Contains $spec "Repos may add other tiers when local names are clearer." "SPEC.md"
Assert-Contains $spec "recommendations, not a required voice" "SPEC.md"
Assert-Contains $spec "not a package manager, workflow runner, or mandatory global role catalog" "SPEC.md"

$adoption = Read-RepoFile "docs\adoption-guide.md"
Assert-Contains $adoption "The goal is not to copy a universal panel." "docs\adoption-guide.md"
Assert-Contains (Normalize $adoption) "You can stop there. That is a useful .roles panel." "docs\adoption-guide.md"
Assert-Contains $adoption "Do not add roles just to look complete." "docs\adoption-guide.md"

$improving = Read-RepoFile "docs\improving-panels.md"
Assert-Contains $improving "This is a starting point, not a universal catalog." "docs\improving-panels.md"
Assert-Contains $improving "replace generic checks with local evidence" "docs\improving-panels.md"

$researchReadme = Read-RepoFile "research\README.md"
Assert-Contains $researchReadme "one portfolio's habits" "research\README.md"
Assert-Contains $researchReadme "not proof that the same distributions hold across independent" "research\README.md"

$roleStudy = Read-RepoFile "research\portfolio-role-quality-study.md"
Assert-Contains $roleStudy "Single portfolio" "research\portfolio-role-quality-study.md"
Assert-Contains $roleStudy "Correlated role files" "research\portfolio-role-quality-study.md"

$tensionStudy = Read-RepoFile "research\productive-tension-study.md"
Assert-Contains $tensionStudy "Future research" "research\productive-tension-study.md"

Write-Output "ROLES PITFALL policy passed: ROLES-PF-04 and ROLES-PF-05 are covered."
