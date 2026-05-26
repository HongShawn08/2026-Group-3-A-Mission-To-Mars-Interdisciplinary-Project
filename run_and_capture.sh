#!/usr/bin/env bash
set -u
cd "/Users/DK/Documents/CSA/2026-Group-3-A-Mission-To-Mars-Interdisciplinary-Project" || exit 1
echo "CWD: $(pwd)"
if [ -d .venv ]; then echo "Activating .venv"; source .venv/bin/activate; else echo "No .venv found"; fi
PY=python3
if ! command -v "$PY" >/dev/null 2>&1; then PY=python; fi
echo "Using python: $(command -v "$PY") ($("$PY" --version 2>&1))"
OUTFILE=run_output.txt
ERRFILE=run_error.txt
echo "Running $PY algae_simulation_cli.py"
"$PY" algae_simulation_cli.py >"$OUTFILE" 2>"$ERRFILE"
EXIT=$?
echo "RUN_EXIT:$EXIT"
echo "---- STDOUT ----"
cat "$OUTFILE" || true
echo "---- STDERR ----"
cat "$ERRFILE" || true
if [ "$EXIT" -ne 0 ]; then
  echo "Analyzing stderr for missing packages..."
  MISSING=$(grep -E "ModuleNotFoundError: No module named '([^']+)'" "$ERRFILE" | sed -E "s/ModuleNotFoundError: No module named '([^']+)'/\\1/" || true)
  if [ -z "$MISSING" ]; then
    MISSING=$(grep -E "ImportError: No module named ([^ ]+)" "$ERRFILE" | sed -E "s/ImportError: No module named ([^ ]+)/\\1/" || true)
  fi
  if [ -n "$MISSING" ]; then
    echo "Missing modules found:"
    echo "$MISSING" | tr ' ' '\n' | sort -u
    for mod in $(echo "$MISSING" | tr ' ' '\n' | sort -u); do
      echo "Installing inferred package for module: $mod"
      "$PY" -m pip install "$mod" || { echo "pip install failed for $mod"; }
    done
    echo "Re-running script after installing missing packages..."
    "$PY" algae_simulation_cli.py >"$OUTFILE" 2>"$ERRFILE"
    EXIT=$?
    echo "RERUN_EXIT:$EXIT"
    echo "---- STDOUT (rerun) ----"
    cat "$OUTFILE" || true
    echo "---- STDERR (rerun) ----"
    cat "$ERRFILE" || true
  else
    echo "No missing-module patterns detected."
  fi
fi
echo "FINAL_EXIT:$EXIT"
exit $EXIT
