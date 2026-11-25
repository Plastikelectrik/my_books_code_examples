$ErrorActionPreference = "Stop"
$ids = @(
  "Git.Git",
  "Microsoft.DotNet.SDK.10",
  "Python.Python.3.13",
  "Microsoft.VisualStudio.2022.BuildTools"
)
foreach ($id in $ids) {
  winget install --id $id -e --accept-source-agreements
}
New-Item -ItemType Directory -Force `
  -Path C:\studio\targets, C:\studio\captures, `
  C:\studio\tools | Out-Null
dotnet tool install --global ilspycmd
Write-Host "Install x64dbg, dnSpyEx and the RAD"
Write-Host "Debugger from their official releases."
