#!/usr/bin/env bash
# 시각은 LaunchAgent plist의 StartCalendarInterval이 정함(로컬 Mac 시계; 서울 시간대면 KST).
# Weekdays: stage current working tree (no file edits), commit if there are changes, push.
# Does not run git pull — remote-only commits must be integrated manually if needed.
# 기간: Asia/Seoul(한국) 달력 기준 2026-06-05(금)까지 동작(당일 13:00 실행 포함), 그다음날부터는 아무것도 하지 않음.
set -euo pipefail

# launchd는 종료일을 지정할 수 없어, KST 날짜로 여기서 구간을 제한한다.
SCHEDULE_UNTIL_KST="20260605" # YYYYMMDD, inclusive
TODAY_KST="$(TZ=Asia/Seoul date +%Y%m%d)"
if [[ "$TODAY_KST" -gt "$SCHEDULE_UNTIL_KST" ]]; then
  echo "[daily-git-sync] Period ended (after 2026-06-05 KST). No commit/push. Remove LaunchAgent if no longer needed."
  exit 0
fi

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
