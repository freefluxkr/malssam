# scripts/list_zip_contents.ps1
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead("C:\Users\tuesv\Downloads\dmdg_malssam_latest_package.zip")
Write-Host "=== ZIP 파일 내 모듈화 파일 목록 ==="
$zip.Entries | Where-Object { $_.FullName -match '^(data|js|css|scripts)[\\/]' } | Select-Object -Property FullName, Length | Format-Table -AutoSize
$zip.Dispose()
