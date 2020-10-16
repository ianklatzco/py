tools for doing rot13 quickly (because i've written this code \>ten times)

also an exercise in learning about python packaging

```bash
usage:
  # get code
  git clone https://github.com/ianklatzco/py

  # to us as use CLI tool
  # accepts from stdin, filename, or argument
  python ~/py/rot

	ROTs 0 to 25
	usage:
	  python rotn.py STRING
	  python rotn.py FILENAME
	  printf 'foo' | python rotn.py


  # alternatively, import as library

  # put on path so you can use within python
  export PYTHONPATH="$HOME/py:$PYTHONPATH" # put in in zshrc
  
  python -i -c 'import rot'   # for repl usage
  >>> rot.rot13('foo')
```

learned:
* [`__main__.py`](__main__.py) is for when you `python foldername/` (to invoke code like
CLI)
* [`__init__.py`](__init__.py) is for specifying exports and populates help() on REPL

see linked files for more detail

