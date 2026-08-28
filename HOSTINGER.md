# Deploy no VPS Hostinger (ao lado do Cria Cria)

O Caddy do Cria Cria já usa as portas **80/443**. Este site sobe como
`mecbr-web` e responde em **`mecbr.criacria.com.br`**.

## DNS

| Tipo | Nome | Dados |
|------|------|--------|
| **A** | `mecbr` | IP do VPS (mesmo de `criacria.com.br`) |

## Subir

```bash
sudo git clone https://github.com/ccheitor/mecbr.git /opt/mecbr
cd /opt/mecbr
cp deploy/.env.hostinger.example .env
```

No Caddyfile do Cria Cria (`/opt/criacria/deploy/Caddyfile`), inclua o bloco
de `deploy/Caddyfile.mecbr.snippet` e no `.env` do Cria Cria:

```bash
MECBR_DOMAIN=mecbr.criacria.com.br
```

No compose do Caddy, passe `MECBR_DOMAIN` no ambiente do serviço `caddy`.

```bash
cd /opt/criacria
docker compose -f docker-compose.prod.yml --env-file .env up -d caddy

cd /opt/mecbr
docker compose -f docker-compose.hostinger.yml --env-file .env up -d --build
```

Ou use o script automatizado:

```bash
bash /opt/mecbr/deploy/vps-up.sh
```

Teste: https://mecbr.criacria.com.br/health
