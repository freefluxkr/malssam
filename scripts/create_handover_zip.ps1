# scripts/create_handover_zip.ps1
$ErrorActionPreference = "Stop"

$sourceDir = "c:\DMDG_JOBs\DMDG_PRJ\dmdg_malssam_dot_com"
$zipPath = "C:\Users\tuesv\Downloads\dmdg_malssam_latest_package.zip"

if (Test-Path $zipPath) {
    Remove-Item -Path $zipPath -Force
}

Write-Host "Collecting files from: $sourceDir"
$itemsToZip = Get-ChildItem -Path $sourceDir | Where-Object { $_.Name -ne '.git' }

Write-Host "Compressing to: $zipPath ..."
Compress-Archive -Path $itemsToZip.FullName -DestinationPath $zipPath -Force

Write-Host "Success! Archive details:"
Get-Item $zipPath | Select-Object Name, Length, LastWriteTime | Format-List
