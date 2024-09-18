На пк должен быть установлен Google Chrome

```bash
#Windows
git clone https://github.com/MixidFinder/EffMob-E2E.git
python -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
pytest

#Linux
git clone https://github.com/MixidFinder/EffMob-E2E.git
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
