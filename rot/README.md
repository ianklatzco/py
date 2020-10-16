tools for doing rot13 quickly (because i've written this code \>ten times)

also an exercise in learning about python packaging

### usage
```bash
# get code
git clone https://github.com/ianklatzco/py

# to us as use CLI tool
# accepts from stdin, filename, or argument
python ~/py/rot

ROTs 0 to 25
usage:
  python ~/py/rot STRING
  python ~/py/rot FILENAME
  printf 'foo' | python ~/py/rot

# alternatively, import as library

# put on path so you can import
export PYTHONPATH="$HOME/py:$PYTHONPATH" # put in in zshrc

# use it!
python -i -c 'import rot'   # for repl usage
# >>> rot.rot13('foo')
```

learned:
* [`__main__.py`](__main__.py) is for when you `python foldername/` (to invoke code like
CLI)
* [`__init__.py`](__init__.py) is for specifying exports and populates help() on REPL

see linked files for more detail

