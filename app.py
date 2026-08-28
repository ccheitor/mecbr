from __future__ import annotations

import json
import os
from pathlib import Path

from flask import Flask, abort, render_template

ROOT = Path(__file__).resolve().parent

app = Flask(__name__)


def load_church() -> dict:
    with (ROOT / "church.json").open(encoding="utf-8") as handle:
        return json.load(handle)


@app.context_processor
def inject_church() -> dict:
    data = load_church()
    data["nav"] = [
        {"href": "/", "label": "Sobre"},
        {"href": "/visite", "label": "Unidades"},
        {"href": "/ministerios", "label": "Ministérios"},
        {"href": "/contato", "label": "Contato"},
    ]
    return {"church": data}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/visite")
def visit():
    return render_template("visite.html")


@app.route("/ministerios")
def ministries():
    return render_template("ministerios.html")


@app.route("/ministerios/<slug>")
def ministry(slug: str):
    data = load_church()
    item = next((m for m in data["ministries"] if m["slug"] == slug), None)
    if item is None:
        abort(404)
    return render_template("ministerio.html", ministry=item)


@app.route("/contato")
def contact():
    return render_template("contato.html")


@app.route("/health")
def health():
    return {"status": "ok"}, 200


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=True)
