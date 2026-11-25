for f in golden/*.ktl; do
  python3 ktl_rebuild.py roundtrip "$f" /tmp/rt.ktl
  cmp -s "$f" /tmp/rt.ktl || echo "DIFF $f"
done
echo "round trip finished"
