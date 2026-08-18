param([Parameter(Mandatory)][string]$Path)

$root = (Resolve-Path $Path -ErrorAction SilentlyContinue).Path
if (-not $root) {
    Write-Output "ERROR repository path does not exist: $Path"
    exit 2
}

$roles = Join-Path $root ".roles"
$errors = [System.Collections.Generic.List[string]]::new()
if (-not (Test-Path $roles -PathType Container)) {
    $errors.Add("missing .roles directory")
} elseif (-not (Test-Path (Join-Path $roles "ROLE.md") -PathType Leaf)) {
    $errors.Add("missing .roles/ROLE.md")
}

if (Test-Path $roles -PathType Container) {
    Get-ChildItem $roles -Filter *.md -File -Recurse |
        Where-Object Name -ne "ROLE.md" |
        ForEach-Object {
            $slugLine = Get-Content $_.FullName |
                Where-Object { $_ -match '^slug:\s*(.+)\s*$' } |
                Select-Object -First 1
            if ($slugLine -and $Matches[1].Trim(" `"'") -notmatch '^[a-z0-9]+(?:-[a-z0-9]+)*$') {
                $relative = [IO.Path]::GetRelativePath($root, $_.FullName)
                $errors.Add("${relative}: slug must be lowercase kebab-case")
            }
        }
}

if ($errors.Count) {
    $errors | ForEach-Object { Write-Output "ERROR $_" }
    exit 1
}
Write-Output "OK $Path"
