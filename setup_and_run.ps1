# Bloomberg Data Downloader - Setup and Run Script
# =================================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Bloomberg Data Downloader - Setup" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Step 1: Create virtual environment
Write-Host "[1/4] Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "   Virtual environment already exists. Removing old one..." -ForegroundColor Gray
    Remove-Item -Recurse -Force venv
}
python -m venv venv
Write-Host "   ✓ Virtual environment created`n" -ForegroundColor Green

# Step 2: Activate virtual environment
Write-Host "[2/4] Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
Write-Host "   ✓ Virtual environment activated`n" -ForegroundColor Green

# Step 3: Install requirements
Write-Host "[3/4] Installing required packages..." -ForegroundColor Yellow
Write-Host "   This may take a few minutes...`n" -ForegroundColor Gray
python -m pip install --upgrade pip
pip install -r requirements.txt
Write-Host "`n   ✓ Packages installed successfully`n" -ForegroundColor Green

# Step 4: Show available symbols
Write-Host "[4/4] Loading Bloomberg symbols..." -ForegroundColor Yellow
if (Test-Path "BB_symbol.csv") {
    Write-Host "`n   Available Bloomberg Symbols (first 20):" -ForegroundColor Cyan
    Write-Host "   ========================================" -ForegroundColor Cyan
    $symbols = Import-Csv "BB_symbol.csv" | Select-Object -First 20
    $symbols | Format-Table Ticker, "Short Name", "Market Cap" -AutoSize | Out-String | Write-Host
    Write-Host "   Total symbols available: $((Import-Csv 'BB_symbol.csv').Count)`n" -ForegroundColor Gray
}

Write-Host "========================================" -ForegroundColor Green
Write-Host "✓ SETUP COMPLETE!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green

Write-Host "Usage Examples:" -ForegroundColor Cyan
Write-Host "---------------" -ForegroundColor Cyan
Write-Host "1. Download HDFCB data:" -ForegroundColor White
Write-Host "   python download_bloomberg_data.py --symbol HDFCB`n" -ForegroundColor Gray

Write-Host "2. Download IOCL data:" -ForegroundColor White
Write-Host "   python download_bloomberg_data.py --symbol IOCL`n" -ForegroundColor Gray

Write-Host "3. Download RELIANCE data with custom wait time:" -ForegroundColor White
Write-Host "   python download_bloomberg_data.py --symbol RELIANCE --wait 30`n" -ForegroundColor Gray

Write-Host "4. Download with custom output directory:" -ForegroundColor White
Write-Host "   python download_bloomberg_data.py --symbol TCS --output_dir ./my_data`n" -ForegroundColor Gray

# Ask if user wants to run a test
Write-Host "`nWould you like to test with a symbol now? (y/n): " -ForegroundColor Yellow -NoNewline
$response = Read-Host

if ($response -eq 'y' -or $response -eq 'Y') {
    Write-Host "`nEnter Bloomberg symbol (e.g., HDFCB, IOCL, RELIANCE): " -ForegroundColor Yellow -NoNewline
    $symbol = Read-Host
    
    Write-Host "`nStarting download for $symbol..." -ForegroundColor Cyan
    Write-Host "Note: Bloomberg Terminal must be running!`n" -ForegroundColor Red
    
    python download_bloomberg_data.py --symbol $symbol
} else {
    Write-Host "`nYou can run the script anytime using:" -ForegroundColor Cyan
    Write-Host "   python download_bloomberg_data.py --symbol <SYMBOL>`n" -ForegroundColor Gray
}

Write-Host "To deactivate the virtual environment later, type: deactivate`n" -ForegroundColor Gray
