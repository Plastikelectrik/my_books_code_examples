#!/usr/bin/env bash
out=~/studio/notes/versions-$(date +%Y%m%d).txt
{
  date
  java -version 2>&1 | head -n 1
  node --version
  rea --help 2>&1 | head -n 1
  jadx --version 2>&1
  apktool --version 2>&1
  frida --version 2>&1
  r2 -v 2>&1 | head -n 1
  rizin -v 2>&1 | head -n 1
  mitmdump --version 2>&1 | head -n 1
} > "$out" 2>&1
echo "written $out"
