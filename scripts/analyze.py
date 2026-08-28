"""Extrai o sistema visual de um site (SkillUI) para usar como referência de leiaute."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Análise reversa de leiaute (SkillUI) — o site em si roda em Python/Flask."
    )
    parser.add_argument(
        "--url",
        default="https://hillsong.com/",
        help="URL de referência visual",
    )
    parser.add_argument(
        "--out",
        default=str(ROOT / "design"),
        help="Pasta de saída",
    )
    parser.add_argument("--name", default="hillsong")
    parser.add_argument("--screens", type=int, default=8)
    parser.add_argument(
        "--mode",
        choices=("default", "ultra"),
        default="ultra",
    )
    args = parser.parse_args()

    skillui = shutil.which("skillui")
    if skillui is None:
        print("SkillUI não encontrado. Instale com: npm install -g skillui")
        print("Para o modo ultra: npm install -g playwright && npx playwright install chromium")
        return 1

    cmd = [
        skillui,
        "--url",
        args.url,
        "--mode",
        args.mode,
        "--screens",
        str(args.screens),
        "--name",
        args.name,
        "--out",
        args.out,
    ]
    print("Rodando:", " ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
