# Cybersecurity blog
Blog, určený pro sdílení nejnovějších exploitů, data breachů atd., pro co nejlepší cybersecurity awareness jeho čtenářů.

## Instalace
### 1.Naklonování repozitáře
```bash
git clone https://github.com/gyarab/2024_WA_INF1_hanslik_python.git
```
### 2.Vytvoření virtual environmentu
```bash
cd 2024_WA_INF1_hanslik_python
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
```
### 3.Instalace balíčků
```bash
pip install -r requirements.txt
```
### 4.Načtení databáze
```bash
python manage.py migrate
python manage.py loaddata blog/fixtures/blog
```
### 5.Spuštění vývojářského serveru
```bash
python manage.py runserver
```
