# Code examples — Mastering REA STUDIO

Every numbered example from the book *Mastering REA STUDIO: Build Your Own Reverse Engineering Studio with AI Agents* by Oscar Gomez, organized by chapter. Example 01 → `example_01.*`.

## How to use

- Run everything in a lab virtual machine, as described in Chapters 3 and 4. Never run the practice targets or the instrumentation scripts on your personal system.
- Shell scripts (`.sh`) are for the Linux analysis VM; PowerShell scripts (`.ps1`) are for the Windows lab VM.
- Python scripts need Python 3.11 or newer. Create a virtual environment per tool, for example `python3 -m venv .venv && .venv/bin/pip install angr` (Chapter 17) or `hypothesis pytest` (Chapter 22).
- `.hexpat` files are ImHex patterns. `.mk` files are Makefiles: rename `example_105.mk` to `Makefile` before running `make`.
- The C, C#, Kotlin, Python and JavaScript programs form the **Kettle Suite**, the practice targets of the book. You build them yourself and you are free to analyze them.
- Placeholders such as `TAG`, `VERSION` or `PASTE_DIGEST_FROM_RELEASE_PAGE` must be replaced with real values from the official sources listed in Appendix I.

## Responsible use

These examples are for the lawful analysis of software that you own or are authorized to examine. They are not tools for circumventing protection measures, accessing systems without permission or intercepting traffic of others. The book is an independent guide and is not affiliated with or endorsed by the REA project or any other tool vendor.

## License

The code is released under the MIT License (see the LICENSE file in the root of this repository). Third-party libraries, tools and models keep their own licenses.

## List of examples

| Folder | File | Title |
|---|---|---|
| ch02_Law_Licences_and_Ethics_for_a_Studio | example_01.md | Scope statement template |
| ch03_Designing_the_Studio | example_02.sh | Create the studio folder layout |
| ch04_Building_the_Base_Lab | example_03.sh | Install base packages on the analysis VM |
| ch04_Building_the_Base_Lab | example_04.sh | Install uv with pipx |
| ch04_Building_the_Base_Lab | example_05.sh | Install Node.js 24 |
| ch04_Building_the_Base_Lab | example_06.sh | Verify a downloaded archive |
| ch04_Building_the_Base_Lab | example_07.ps1 | Install base tools on the Windows lab VM |
| ch04_Building_the_Base_Lab | example_08.sh | Create an Android emulator for the lab |
| ch04_Building_the_Base_Lab | example_09.c | The kettle program (kettle.c) |
| ch04_Building_the_Base_Lab | example_10.sh | Build the debug and stripped versions |
| ch04_Building_the_Base_Lab | example_11.sh | Studio verification script (check_studio.sh) |
| ch05_Ghidra_the_Free_Engine | example_12.sh | Install Ghidra into /opt |
| ch05_Ghidra_the_Free_Engine | example_13.sh | Set Ghidra environment variables |
| ch05_Ghidra_the_Free_Engine | example_14.java | List functions in a Ghidra script (ListFunctions.java) |
| ch05_Ghidra_the_Free_Engine | example_15.sh | Run a script with the headless analyzer |
| ch06_REA_as_the_Studio_Hub | example_16.sh | Run the guided REA setup |
| ch06_REA_as_the_Studio_Hub | example_17.sh | Install the rea command globally |
| ch06_REA_as_the_Studio_Hub | example_18.sh | Run the readiness check |
| ch06_REA_as_the_Studio_Hub | example_19.sh | Register REA by hand in a command-line agent |
| ch06_REA_as_the_Studio_Hub | example_20.sh | List providers and capabilities |
| ch06_REA_as_the_Studio_Hub | example_21.sh | Get an overview of the target |
| ch06_REA_as_the_Studio_Hub | example_22.sh | Search for a clue and trace it to code |
| ch06_REA_as_the_Studio_Hub | example_23.sh | Request a function dossier |
| ch06_REA_as_the_Studio_Hub | example_24.md | First research prompt for the agent |
| ch06_REA_as_the_Studio_Hub | example_25.sh | Validate and store an exported bundle |
| ch07_GhidraMCP_Letting_the_Agent_Drive_Ghidra | example_26.sh | Register GhidraMCP in a command-line agent |
| ch07_GhidraMCP_Letting_the_Agent_Drive_Ghidra | example_27.sh | Start GhidraMCP in headless mode |
| ch07_GhidraMCP_Letting_the_Agent_Drive_Ghidra | example_28.sh | Build the GhidraMCP extension from source |
| ch08_IDA_Pro_and_ida-pro-mcp | example_29.sh | Activate idalib for Python |
| ch08_IDA_Pro_and_ida-pro-mcp | example_30.sh | Install ida-pro-mcp manually |
| ch08_IDA_Pro_and_ida-pro-mcp | example_31.sh | Start the headless IDA MCP server |
| ch08_IDA_Pro_and_ida-pro-mcp | example_32.md | Instruction for number conversions |
| ch08_IDA_Pro_and_ida-pro-mcp | example_33.sh | Compare two engines on one function |
| ch09_Orchestrating_Several_MCP_Servers | example_34.json | Project MCP configuration for a native investigation |
| ch09_Orchestrating_Several_MCP_Servers | example_35.md | Engine roles in the scope statement |
| ch09_Orchestrating_Several_MCP_Servers | example_36.md | Untrusted content rule for every session |
| ch10_jadx_From_Android_Packages_to_Java | example_37.kt | The brew rules in Kotlin (BrewCalculator.kt) |
| ch10_jadx_From_Android_Packages_to_Java | example_38.kt | A minimal activity (MainActivity.kt) |
| ch10_jadx_From_Android_Packages_to_Java | example_39.sh | Install jadx |
| ch10_jadx_From_Android_Packages_to_Java | example_40.sh | Decompile an APK to a folder |
| ch10_jadx_From_Android_Packages_to_Java | example_41.sh | Android analysis with REA |
| ch11_Apktool_Decoding_and_Rebuilding_Packages | example_42.sh | Install Apktool on Linux |
| ch11_Apktool_Decoding_and_Rebuilding_Packages | example_43.sh | Decode the release APK |
| ch11_Apktool_Decoding_and_Rebuilding_Packages | example_44.xml | Lab network security configuration (lab_network.xml) |
| ch11_Apktool_Decoding_and_Rebuilding_Packages | example_45.sh | Rebuild, align and sign a lab build |
| ch11_Apktool_Decoding_and_Rebuilding_Packages | example_46.sh | Install the lab build in the emulator |
| ch12_Frida_Observing_Apps_at_Runtime | example_47.sh | Install Frida client tools |
| ch12_Frida_Observing_Apps_at_Runtime | example_48.sh | Install frida-server in the lab emulator |
| ch12_Frida_Observing_Apps_at_Runtime | example_49.js | Observe brewTime in the Android app (watch_brew.js) |
| ch12_Frida_Observing_Apps_at_Runtime | example_50.sh | Start the app with the script |
| ch12_Frida_Observing_Apps_at_Runtime | example_51.sh | Trace all methods of the app package |
| ch12_Frida_Observing_Apps_at_Runtime | example_52.js | Observe strcmp calls (watch_strcmp.js) |
| ch12_Frida_Observing_Apps_at_Runtime | example_53.py | Spawn a program with a Frida script (run_frida.py) |
| ch12_Frida_Observing_Apps_at_Runtime | example_54.sh | Run the native trace |
| ch12_Frida_Observing_Apps_at_Runtime | example_55.sh | Save a reproducible capture |
| ch13_NET_with_ILSpy_and_dnSpyEx | example_56.sh | Create the .NET projects |
| ch13_NET_with_ILSpy_and_dnSpyEx | example_57.cs | The brew rules in C# (Brew.cs) |
| ch13_NET_with_ILSpy_and_dnSpyEx | example_58.cs | The console program (Program.cs) |
| ch13_NET_with_ILSpy_and_dnSpyEx | example_59.sh | Build and run the .NET target |
| ch13_NET_with_ILSpy_and_dnSpyEx | example_60.sh | Install the ILSpy command-line tool |
| ch13_NET_with_ILSpy_and_dnSpyEx | example_61.sh | Decompile an assembly to a C# project |
| ch13_NET_with_ILSpy_and_dnSpyEx | example_62.sh | Managed-code evidence with REA |
| ch14_radare2_and_rizin_in_the_Terminal | example_63.sh | Install radare2 from source |
| ch14_radare2_and_rizin_in_the_Terminal | example_64.sh | Build rizin from a source release |
| ch14_radare2_and_rizin_in_the_Terminal | example_65.sh | Open a binary with analysis |
| ch14_radare2_and_rizin_in_the_Terminal | example_66.sh | Install the Ghidra decompiler plugin for radare2 |
| ch14_radare2_and_rizin_in_the_Terminal | example_67.sh | Create a scripting environment |
| ch14_radare2_and_rizin_in_the_Terminal | example_68.py | Find functions that use given constants (fingerprint.py) |
| ch14_radare2_and_rizin_in_the_Terminal | example_69.sh | Run the fingerprint script |
| ch15_Debugging_Native_Code_x64dbg_and_the_RAD_Debugger | example_70.sh | Debug brew_time with gdb |
| ch15_Debugging_Native_Code_x64dbg_and_the_RAD_Debugger | example_71.ps1 | Build kettle.exe with a PDB file |
| ch16_ImHex_Reading_File_Formats | example_72.sh | Install ImHex from a Debian package |
| ch16_ImHex_Reading_File_Formats | example_73.py | Generate a sample recipe file (make_ktl.py) |
| ch16_ImHex_Reading_File_Formats | example_74.sh | Create the sample file |
| ch16_ImHex_Reading_File_Formats | example_75.hexpat | KTL format pattern (ktl.hexpat) |
| ch16_ImHex_Reading_File_Formats | example_76.py | Check the trailing CRC-32 of a .ktl file (ktl_crc.py) |
| ch16_ImHex_Reading_File_Formats | example_77.hexpat | Pattern with checks and comments (ktl_v2.hexpat) |
| ch17_angr_Symbolic_Execution | example_78.c | The lock puzzle (kettle-lock.c) |
| ch17_angr_Symbolic_Execution | example_79.sh | Build kettle-lock |
| ch17_angr_Symbolic_Execution | example_80.sh | Install angr in a virtual environment |
| ch17_angr_Symbolic_Execution | example_81.py | Find an input that opens the lock (solve_lock.py) |
| ch17_angr_Symbolic_Execution | example_82.sh | Run the solver |
| ch18_mitmproxy_Observing_Your_Own_Traffic | example_83.py | A small recipe server (kettle_server.py) |
| ch18_mitmproxy_Observing_Your_Own_Traffic | example_84.py | A small recipe client (kettle_client.py) |
| ch18_mitmproxy_Observing_Your_Own_Traffic | example_85.sh | Install mitmproxy |
| ch18_mitmproxy_Observing_Your_Own_Traffic | example_86.sh | Capture client traffic in reverse mode |
| ch18_mitmproxy_Observing_Your_Own_Traffic | example_87.py | Log and redact with an addon (kettle_addon.py) |
| ch18_mitmproxy_Observing_Your_Own_Traffic | example_88.sh | Run mitmdump with the addon |
| ch18_mitmproxy_Observing_Your_Own_Traffic | example_89.sh | Export a capture to HAR and analyze it with REA |
| ch19_Web_JavaScript_and_Electron_Targets | example_90.js | The brew rules as a module (brew.js) |
| ch19_Web_JavaScript_and_Electron_Targets | example_91.html | A minimal page (index.html) |
| ch19_Web_JavaScript_and_Electron_Targets | example_92.sh | Serve kettle-web locally |
| ch19_Web_JavaScript_and_Electron_Targets | example_93.js | Electron main process (main.js) |
| ch19_Web_JavaScript_and_Electron_Targets | example_94.js | Electron preload script (preload.js) |
| ch19_Web_JavaScript_and_Electron_Targets | example_95.sh | Create and package the desktop app |
| ch19_Web_JavaScript_and_Electron_Targets | example_96.sh | Build an application graph |
| ch19_Web_JavaScript_and_Electron_Targets | example_97.sh | Start a lab browser profile with remote debugging |
| ch19_Web_JavaScript_and_Electron_Targets | example_98.sh | Allow REA to observe only the local lab page |
| ch20_Connecting_the_Tools | example_99.py | Convert shared names to a radare2 script (names_to_r2.py) |
| ch20_Connecting_the_Tools | example_100.sh | Apply Ghidra names in radare2 |
| ch20_Connecting_the_Tools | example_101.py | Run a target over many inputs (observe.py) |
| ch20_Connecting_the_Tools | example_102.sh | Collect observations of kettle |
| ch20_Connecting_the_Tools | example_103.py | Build an evidence index (index_evidence.py) |
| ch20_Connecting_the_Tools | example_104.sh | Index the evidence of an investigation |
| ch20_Connecting_the_Tools | example_105.mk | Repeatable investigation steps (Makefile) |
| ch21_Writing_SPECmd | example_106.md | SPEC.md template |
| ch21_Writing_SPECmd | example_107.md | SPEC.md for kettle (SPEC.md) |
| ch22_Oracles_Deciding_When_Behavior_Matches | example_108.py | A differential oracle for kettle (diff_oracle.py) |
| ch22_Oracles_Deciding_When_Behavior_Matches | example_109.sh | Sanity checks for the oracle |
| ch22_Oracles_Deciding_When_Behavior_Matches | example_110.py | A property-based differential test (test_kettle_props.py) |
| ch22_Oracles_Deciding_When_Behavior_Matches | example_111.sh | Run the property test |
| ch22_Oracles_Deciding_When_Behavior_Matches | example_112.sh | Round-trip check for .ktl files |
| ch23_The_Clean-Room_Loop | example_113.sh | Create a builder account with limited access |
| ch23_The_Clean-Room_Loop | example_114.sh | Run a build session in a container |
| ch23_The_Clean-Room_Loop | example_115.py | Rebuild version 1, written from SPEC.md (kettle_rebuild.py) |
| ch23_The_Clean-Room_Loop | example_116.py | A strategy for 32-bit wrap-around inputs |
| ch23_The_Clean-Room_Loop | example_117.md | New requirement after iteration 2 |
| ch23_The_Clean-Room_Loop | example_118.py | Rebuild version 2: the end of parse_strength |
| ch24_REA_Workflows_and_Research_Prompts | example_119.md | P1 triage prompt (p1_triage.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_120.md | P2 feature trace prompt (p2_trace.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_121.md | P3 function dossier prompt (p3_dossier.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_122.md | P4 runtime plan prompt (p4_runtime_plan.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_123.md | P5 specification draft prompt (p5_spec.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_124.md | P6 specification review prompt (p6_review.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_125.md | P7 builder prompt (p7_build.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_126.md | P8 difference triage prompt (p8_triage_diff.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_127.md | P9 boundary hunt prompt (p9_boundaries.md) |
| ch24_REA_Workflows_and_Research_Prompts | example_128.md | P10 report prompt (p10_report.md) |
| ch26_Securing_the_Studio_Itself | example_129.py | A hook that blocks risky shell commands (block_risky.py) |
| ch27_Comparing_Versions | example_130.sh | Build kettle 1.1 |
| ch27_Comparing_Versions | example_131.sh | Compare digests and sizes |
| ch27_Comparing_Versions | example_132.sh | Run a REA version investigation |
| ch27_Comparing_Versions | example_133.sh | Compare the behavior of two versions |
| ch27_Comparing_Versions | example_134.md | Change log entries for version 1.1 |
| ch28_Four_Complete_Studio_Projects | example_135.py | A clean-room reader and writer for .ktl (ktl_rebuild.py) |
| ch28_Four_Complete_Studio_Projects | example_136.sh | Run the round-trip oracle over all golden files |
| ch28_Four_Complete_Studio_Projects | example_137.js | Print the Android brew table with Frida (table.js) |
| ch28_Four_Complete_Studio_Projects | example_138.py | Compare normalized brew tables (compare_tables.py) |
| ch28_Four_Complete_Studio_Projects | example_139.js | Print the brew table of the web module (table.mjs) |
| ch29_Firmware_and_Other_Architectures | example_140.sh | Install firmware and cross-architecture tools |
| ch29_Firmware_and_Other_Architectures | example_141.sh | Cross-compile kettle for AArch64 |
| ch29_Firmware_and_Other_Architectures | example_142.sh | Create the root file system |
| ch29_Firmware_and_Other_Architectures | example_143.py | Build the firmware image (make_fw.py) |
| ch29_Firmware_and_Other_Architectures | example_144.sh | Build and scan the image |
| ch29_Firmware_and_Other_Architectures | example_145.hexpat | Pattern for the firmware header (ktfw.hexpat) |
| ch29_Firmware_and_Other_Architectures | example_146.sh | Extract the image with REA and Unblob |
| ch29_Firmware_and_Other_Architectures | example_147.sh | Run the ARM program with QEMU user mode |
| ch30_Binary_Protocols | example_148.py | The kettle-bin server (kb_server.py) |
| ch30_Binary_Protocols | example_149.py | The kettle-bin client (kb_client.py) |
| ch30_Binary_Protocols | example_150.py | Record raw TCP messages (kb_record.py) |
| ch30_Binary_Protocols | example_151.sh | Relay and record the kettle-bin conversation |
| ch30_Binary_Protocols | example_152.hexpat | Pattern for a kettle-bin message (kb.hexpat) |
| ch30_Binary_Protocols | example_153.py | Replay recorded requests and compare answers (kb_replay.py) |
| ch30_Binary_Protocols | example_154.sh | Replay against the original server |
| ch31_Windows_Programs_in_Depth | example_155.ps1 | Read headers and imports with dumpbin |
| ch31_Windows_Programs_in_Depth | example_156.py | A short PE report (pe_report.py) |
| ch31_Windows_Programs_in_Depth | example_157.sh | Run the PE report |
| ch31_Windows_Programs_in_Depth | example_158.ps1 | Check the Authenticode signature of a file |
| ch32_Long_Investigations_with_Agents | example_159.md | Example STATE.md |
| ch33_Building_Practice_Targets | example_160.c | Encoded tea names for a practice target (kettle_enc.c) |
| ch33_Building_Practice_Targets | example_161.sh | Build and check the encoded target |
| ch35_The_Studio_in_a_Team_and_What_Comes_Next | example_162.sh | A minimal pipeline step for release checks |
| appendix_C_Templates | example_163.md | Template: SCOPE.md |
| appendix_C_Templates | example_164.md | Template: findings.md |
| appendix_C_Templates | example_165.md | Template: channel question and answer |
| appendix_C_Templates | example_166.md | Template: tool evaluation |
| appendix_C_Templates | example_167.md | Template: report.md |
| appendix_F_Standing_Rules_for_Agents | example_168.md | Standing rule: evidence (rules_evidence.md) |
| appendix_F_Standing_Rules_for_Agents | example_169.md | Standing rule: untrusted content (rules_untrusted.md) |
| appendix_F_Standing_Rules_for_Agents | example_170.md | Standing rule: numbers and addresses (rules_numbers.md) |
| appendix_F_Standing_Rules_for_Agents | example_171.md | Standing rule: actions (rules_actions.md) |
| appendix_F_Standing_Rules_for_Agents | example_172.md | Standing rule: build side (rules_build.md) |
| appendix_F_Standing_Rules_for_Agents | example_173.md | Session start message (session_start.md) |
| appendix_K_Lab_Builder_Scripts | example_174.sh | Analysis VM base setup (setup_analysis_vm.sh) |
| appendix_K_Lab_Builder_Scripts | example_175.sh | Create the Python environments (setup_envs.sh) |
| appendix_K_Lab_Builder_Scripts | example_176.sh | Install an archive after digest verification (install_verified.sh) |
| appendix_K_Lab_Builder_Scripts | example_177.sh | Example use of the verified installer |
| appendix_K_Lab_Builder_Scripts | example_178.sh | Build the native Kettle Suite targets (build_kettle.sh) |
| appendix_K_Lab_Builder_Scripts | example_179.sh | Print a dated snapshot name (snapname.sh) |
| appendix_K_Lab_Builder_Scripts | example_180.sh | Record installed tool versions (versions.sh) |
| appendix_K_Lab_Builder_Scripts | example_181.ps1 | Windows lab VM base setup (setup_windows_lab.ps1) |
| appendix_N_A_Complete_Worked_Investigation | example_182.md | Worked example: SCOPE.md |
| appendix_N_A_Complete_Worked_Investigation | example_183.md | Worked example: STATE.md |
| appendix_N_A_Complete_Worked_Investigation | example_184.md | Worked example: findings extract |
| appendix_N_A_Complete_Worked_Investigation | example_185.md | Worked example: report summary |
