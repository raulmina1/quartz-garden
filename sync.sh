#!/bin/bash
# Syncs all .md files from the Obsidian vault blog folder to Quartz content/,
# then commits and pushes to trigger GitHub Pages deploy.

VAULT_BLOG="/c/Vaults/YellowVault/11_GEBOTE/02_RA BLOG"
REPO_DIR="/c/Users/DELLPHOTO/OneDrive/Documents/GitHub/quartz-garden"
REPO_CONTENT="${REPO_DIR}/content"

echo "Syncing vault → content/..."
cp "${VAULT_BLOG}"/*.md "${REPO_CONTENT}/"

cd "${REPO_DIR}"
git add content/

if git diff --cached --quiet; then
  echo "Nothing new to publish."
  exit 0
fi

TIMESTAMP=$(date '+%B %d, %Y, %I:%M %p')
git commit -m "sync: ${TIMESTAMP}"
NODE_OPTIONS="--use-system-ca" git push origin v4
echo "Done — GitHub Actions will deploy in ~1-2 min."
echo "Live site: https://raulmina1.github.io/ra-blog/"
