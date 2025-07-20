# git_commit.ps1

# Récupère la date au format YYYY-MM-DD
$today = Get-Date -Format "yyyy-MM-dd"

# Récupère la branche actuelle
$currentBranch = git rev-parse --abbrev-ref HEAD

# Demande la branche cible
$branchName = Read-Host "Branch to push to [$currentBranch]"
if ([string]::IsNullOrWhiteSpace($branchName)) {
    $branchName = $currentBranch
}

# Demande le message de commit
$message = Read-Host "What is this version about?"
$fullMessage = "$today $message"

# Remplacer les espaces pour le tag
$tag = $fullMessage -replace ' ', '_'

# Git commit complet
git add .
git commit -m "$fullMessage"
git tag "$tag"
git push origin $branchName
git push origin --tags

Write-Host "✅ Done! Committed to branch [$branchName] and tagged: '$tag'"
