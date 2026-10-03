#!/bin/bash

source venv/Scripts/activate

pip install --upgrade pip
pip install -r requirements.txt

python -c "import shutil; shutil.rmtree('public', ignore_errors=True)"

reflex init
reflex export --frontend-only

python -c "import zipfile; zipfile.ZipFile('frontend.zip').extractall('public')"

deactivate