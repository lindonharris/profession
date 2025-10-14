#!/bin/bash
# Auto-regenerate venue map from rolodex.json
# This script automatically runs whenever rolodex.json is modified

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 ~/.claude/direct-access-tools/venues/sync-rolodex.py "$SCRIPT_DIR/rolodex.json"
