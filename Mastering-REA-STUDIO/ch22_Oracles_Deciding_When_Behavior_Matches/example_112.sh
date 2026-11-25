python3 ktl_rebuild.py roundtrip sample.ktl out.ktl
cmp sample.ktl out.ktl && echo "byte-identical"
python3 ktl_crc.py out.ktl
