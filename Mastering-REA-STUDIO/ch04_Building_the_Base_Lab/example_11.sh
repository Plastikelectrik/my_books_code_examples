#!/usr/bin/env bash
check() {
  local name="$1"; shift
  if command -v "$1" >/dev/null 2>&1; then
    printf "%-12s ok   %s\n" "$name" \
      "$("$@" 2>&1 | head -n 1)"
  else
    printf "%-12s MISSING\n" "$name"
  fi
}
check java     java -version
check node     node --version
check uv       uv --version
check rea      rea --help
check jadx     jadx --version
check apktool  apktool --version
check frida    frida --version
check r2       r2 -v
check rizin    rizin -v
check imhex    imhex --version
check mitmdump mitmdump --version
check adb      adb version
check ilspycmd ilspycmd --version
