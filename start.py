import subprocess

# Run the PowerShell script
subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", "run.ps1"])
