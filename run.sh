#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR/toolboxlauncher"

export QT_QPA_PLATFORM=xcb
python3 topnoiselauncher.py