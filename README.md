# Ministério Ebenézer Church

Site institucional da igreja (Flask + Jinja2).

## Requisitos

- Python 3.11+

## Execução local

```bash
cd ebenezer-church
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app run --debug --port 5000
```

Linux / macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug --port 5000
```

URL local: http://127.0.0.1:5000

Site: https://mecbr.org

Alternativa (sem o comando `flask`):

```bash
python app.py
```

## Estrutura

```text
ebenezer-church/
├── app.py           # Aplicação Flask
├── church.json      # Textos, unidades e ministérios
├── templates/       # Páginas HTML
├── static/          # CSS, JS, imagens e vídeo
└── requirements.txt
```

## Conteúdo

Edite `church.json` para alterar textos, endereços, horários de culto e links das redes sociais.

Imagens e vídeo ficam em `static/img/`.
