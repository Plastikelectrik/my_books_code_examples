E=~/studio/tools/oracle-env
python3 -m venv "$E"
"$E/bin/pip" install hypothesis pytest
PYTEST="$E/bin/pytest"
KETTLE_ORIGINAL=./kettle-stripped \
KETTLE_REBUILD=./kettle-stripped \
  "$PYTEST" -q test_kettle_props.py
