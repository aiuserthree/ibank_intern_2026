#!/usr/bin/env bash
# 시각은 LaunchAgent plist의 StartCalendarInterval이 정함(로컬 Mac 시계; 서울 시간대면 KST).
# Weekdays: stage current working tree (no file edits), commit if there are changes, push.
# Does not run git pull — remote-only commits must be integrated manually if needed.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

LOG_PREFIX="[daily-git-sync $(date '+%Y-%m-%d %H:%M:%S')]"

git add -A
if git diff --cached --quiet; then
  echo "$LOG_PREFIX Nothing to commit; working tree already matches index."
  exit 0
fi

MSG="chore: scheduled sync $(date '+%Y-%m-%d %H:%M:%S %z')"
git commit -m "$MSG"
git push
echo "$LOG_PREFIX Committed and pushed."
