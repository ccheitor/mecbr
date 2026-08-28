#!/bin/bash
set -euo pipefail

DOMAIN_MECBR="mecbr.criacria.com.br"

echo "[mecbr] clone/update"
if [ ! -d /opt/mecbr/.git ]; then
  git clone https://github.com/ccheitor/mecbr.git /opt/mecbr
else
  cd /opt/mecbr
  git fetch origin
  git reset --hard origin/main
fi

cd /opt/mecbr

if [ ! -f .env ]; then
  cp deploy/.env.hostinger.example .env
fi

# Patch Caddyfile do Cria Cria
CADDY=/opt/criacria/deploy/Caddyfile
if ! grep -q 'MECBR_DOMAIN' "$CADDY"; then
  cat >> "$CADDY" <<'EOF'

# Ministério Ebenézer Church — subdomínio (container mecbr-web)
{$MECBR_DOMAIN:mecbr.criacria.com.br} {
	encode gzip
	reverse_proxy mecbr-web:8000
}
EOF
fi

if ! grep -q '^MECBR_DOMAIN=' /opt/criacria/.env; then
  echo "MECBR_DOMAIN=${DOMAIN_MECBR}" >> /opt/criacria/.env
fi

COMPOSE=/opt/criacria/docker-compose.prod.yml
if ! grep -q 'MECBR_DOMAIN' "$COMPOSE"; then
  python3 - <<'PY'
from pathlib import Path
p = Path("/opt/criacria/docker-compose.prod.yml")
text = p.read_text()
needle = "      ESTANCIA_DOMAIN: ${ESTANCIA_DOMAIN:-estanciavalenca.criacria.com.br}\n"
insert = needle + "      MECBR_DOMAIN: ${MECBR_DOMAIN:-mecbr.criacria.com.br}\n"
if "MECBR_DOMAIN" not in text and needle in text:
    p.write_text(text.replace(needle, insert, 1))
    print("compose patched")
else:
    print("compose already ok or needle missing")
PY
fi

cd /opt/criacria
docker compose -f docker-compose.prod.yml --env-file .env up -d caddy

cd /opt/mecbr
docker compose -f docker-compose.hostinger.yml --env-file .env up -d --build

sleep 3
docker ps --format 'table {{.Names}}\t{{.Status}}' | grep -E 'mecbr|caddy|NAMES'
docker exec mecbr-web curl -fsS http://127.0.0.1:8000/health
echo
curl -fsSI "https://${DOMAIN_MECBR}/health" | head -n 15 || true
