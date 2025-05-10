# Nordliv Cache Warmer

Detta GitHub Actions-projekt besöker automatiskt nordlivpodcast.se:s förstasida och de senaste 10 inläggen var sjätte timme för att värma cachen hos Cloudflare.

## Innehåll
- `cachewarmer.py`: Python-skript som läser RSS-flödet och besöker sidorna.
- `.github/workflows/cachewarmer.yml`: Kör skriptet automatiskt via GitHub Actions.