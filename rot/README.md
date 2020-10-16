quick experiments in learning about python packaging, and rewriting rotN
code i've now written on several occasions

usage:
  export PYTHONPATH="$HOME/py:$PYTHONPATH" # put in in zshrc
  
  git clone https://github.com/ianklatzco/py

  python ~/py/rot             # for CLI tool; pipe, filename, or string literal
  python -i -c 'import rot'   # for repl usage


see __init__.py for summary of what i learned about packaging.
