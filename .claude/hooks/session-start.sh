#!/bin/bash
# SessionStart hook: prepare the `watch` skill so any video link "just works".
#
# What it does, idempotently, on every session start:
#   1. Installs the binaries the watch skill needs: ffmpeg / ffprobe (apt) and
#      yt-dlp (pip --user).
#   2. Scaffolds ~/.config/watch/.env with sane defaults.
#   3. If a Whisper API key is present as an environment secret
#      (OPENAI_API_KEY or GROQ_API_KEY), wires it into that config so
#      caption-less videos (TikTok, Meta ad library, etc.) can still be
#      transcribed. The key is read from the environment, never stored in git.
#
# Set the secret once in the Claude Code web environment settings; the hook
# picks it up automatically from then on.
set -euo pipefail

log() { echo "[watch-setup] $*" >&2; }

# --- 1. binaries ---------------------------------------------------------
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  log "installing ffmpeg…"
  if command -v apt-get >/dev/null 2>&1; then
    sudo apt-get install -y ffmpeg >/dev/null 2>&1 \
      || apt-get install -y ffmpeg >/dev/null 2>&1 \
      || log "ffmpeg install failed — install it manually"
  else
    log "no apt-get; install ffmpeg manually"
  fi
else
  log "ffmpeg present"
fi

if ! command -v yt-dlp >/dev/null 2>&1 && [ ! -x "$HOME/.local/bin/yt-dlp" ]; then
  log "installing yt-dlp…"
  pip3 install --user --quiet yt-dlp >/dev/null 2>&1 \
    || pip install --user --quiet yt-dlp >/dev/null 2>&1 \
    || log "yt-dlp install failed — install it manually"
else
  log "yt-dlp present"
fi

# Make sure pip --user bin is on PATH for this session.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$CLAUDE_ENV_FILE"
fi

# --- 2. watch config -----------------------------------------------------
CONFIG_DIR="$HOME/.config/watch"
CONFIG_FILE="$CONFIG_DIR/.env"
mkdir -p "$CONFIG_DIR"

# Create the file with defaults if it doesn't exist yet.
if [ ! -f "$CONFIG_FILE" ]; then
  cat > "$CONFIG_FILE" <<'EOF'
# watch skill config
WATCH_DETAIL=balanced
SETUP_COMPLETE=true
EOF
  chmod 600 "$CONFIG_FILE"
  log "scaffolded $CONFIG_FILE"
fi

# --- 3. inject Whisper API key from environment secret -------------------
inject_key() {
  # $1 = env var name, $2 = config key name
  local val="${!1:-}"
  [ -z "$val" ] && return 0
  if grep -q "^$2=" "$CONFIG_FILE" 2>/dev/null; then
    sed -i "s|^$2=.*|$2=$val|" "$CONFIG_FILE"
  else
    echo "$2=$val" >> "$CONFIG_FILE"
  fi
  log "wired $2 from environment secret"
}

inject_key OPENAI_API_KEY OPENAI_API_KEY
inject_key GROQ_API_KEY GROQ_API_KEY

# Ensure completion marker is set.
grep -q "^SETUP_COMPLETE=" "$CONFIG_FILE" 2>/dev/null \
  || echo "SETUP_COMPLETE=true" >> "$CONFIG_FILE"

chmod 600 "$CONFIG_FILE" 2>/dev/null || true
log "watch skill ready"
