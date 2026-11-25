# Scope: kettle 1.0 (stripped build)

Owner and legal basis: I wrote this program.
Purpose: document behavior; verified rebuild.
Question: what does kettle print for any input?
Allowed: static analysis; runs in lab VM with no
network; Frida and gdb on the lab VM.
Not allowed: network; patching the original.
Data rules: synthetic inputs only.
AI provider: allowed; target has no secrets.
Engines: primary REA (ghidra); confirm REA (ida)
and radare2.
Stopping criteria: all REQ tested; oracles pass;
boundary review done; 5 of 5 mutants killed.
Output: SPEC.md, rebuild, oracles, report.
Approved by: me, 2026-11-02
