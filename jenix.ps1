# PowerShell wrapper for ager.py
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptPath "Jenix.py"

# Forward all arguments to the Python script
python $pythonScript $args 