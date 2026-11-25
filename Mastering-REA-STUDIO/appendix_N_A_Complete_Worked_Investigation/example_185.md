# Report: kettle 1.0 behavior and rebuild

Question: what does kettle print for any input?
Answer: We confirmed the complete brew rules, the
checksum and all error cases in scope, in the code
and at runtime. A clean-room rebuild in Python
passes all oracles.
Limits: Linux x86-64 build only. We could not
determine behavior with a closed standard output
or names longer than 4096 bytes (not tested).
Recommendation: use the rebuild for Linux x86-64
compatibility; observe the Windows build before
using it there, because number parsing differs.
Risk if nothing is done: none; documentation only.
