where pipx
IF %ERRORLEVEL% EQU 0 (ECHO "pipx is installed") ELSE (python -m pip install --user pipx)

where poetry
IF %ERRORLEVEL% EQU 0 (ECHO "poetry is installed") ELSE (pip install poetry)

where java
IF %ERRORLEVEL% EQU 0 (ECHO "java is installed") ELSE (winget install Microsoft.OpenJDK.21)

poetry config virtualenvs.in-project false

ECHO "Installing dependencies..."
poetry install

ECHO "Done.  Configure your IDE to use the .\Scripts\python.exe interpreter in the following virtual environment path"
poetry env info -p
