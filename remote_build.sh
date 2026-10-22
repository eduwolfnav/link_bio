#!/bin/bash
#!/bin/bash
export PYTHONUTF8=1
set -e

pip install --upgrade pip
pip install -r requirements.txt

rm -rf public

reflex init
reflex export --frontend-only

python -c "import zipfile; zipfile.ZipFile('frontend.zip').extractall('public')"

# Ejecutar bash build.sh
# & "C:\Program Files\Git\bin\bash.exe" build.sh

# PD: Antes de ejecutar, correc bash con .venv deactivate

# git add .
# git commit -m "Actualización del proyecto / 3°"
# git push origin master
# git push