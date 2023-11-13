where pipx
IF %ERRORLEVEL% EQU 0 (ECHO "pipx is installed") ELSE (python -m pip install --user pipx)

where poetry
IF %ERRORLEVEL% EQU 0 (ECHO "poetry is installed") ELSE (pip install poetry)

poetry config virtualenvs.in-project false

ECHO "Installing dependencies..."
poetry install

where lefthook
IF %ERRORLEVEL% EQU 0 (ECHO "lefthook is installed") ELSE (winget install evilmartians.lefthook)

ECHO "Setting up git hooks for this project"
lefthook install

ECHO "Done.  Configure your IDE to use the .\Scripts\python.exe interpreter in the following virtual environment path"
poetry env info -p
