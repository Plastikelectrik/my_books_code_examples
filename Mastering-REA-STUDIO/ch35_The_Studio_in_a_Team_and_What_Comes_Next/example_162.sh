set -euo pipefail
python3 scripts/outsider_review.py dist/ \
  > reports/outsider.txt
python3 oracles/diff_oracle.py \
  "previous/kettle" "dist/kettle" \
  > reports/behavior-diff.txt || true
python3 scripts/check_expected_changes.py \
  reports/behavior-diff.txt release-notes.md
