# install.ps1

# Define paths
$venvPath = ".\venv\Scripts\Activate.ps1"
$requirementsFile = "requirements.txt"

# Check if venv exists
if (Test-Path $venvPath) {
    Write-Host "Virtual environment found. Activating..."
    . $venvPath
} else {
    Write-Host "Virtual environment not found! Please create it with 'python -m venv venv'"
    exit 1
}

# Check if requirements.txt exists
if (Test-Path $requirementsFile) {
    Write-Host "Installing dependencies from $requirementsFile..."
    pip install -r $requirementsFile

    if ($LASTEXITCODE -eq 0) {
        Write-Host "All dependencies installed successfully!"
    } else {
        Write-Host "pip install failed."
    }
} else {
    Write-Host "⚠️ requirements.txt not found. Skipping dependency installation."
}
