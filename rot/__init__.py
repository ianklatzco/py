# rot13 utility functions

# ^ this is shown in pydoc/help

# __all__ = ['rotn','rot13'] # customizes from rot import * and changes what pydoc shows
# used to explicitly specify exports

# i think the . specifies local dir
from ._rot import rotn
from ._rot import rot13

# naming your primary code file _rot.py (note the _) makes tab completion in
# the repl not show a "rot" name, which keeps it slightly cleaner. however, if
# one wishes to use the code directly, this is somewhat clunky, since it
# requires a python ~/py/rot/_rot.py
# from ._rot import rotn
# from ._rot import rot13

# HOWEVER, i learned that you can put a __main__.py.
# this enables you to simple python ~/py/rot to get the script's CLI.
# eventually i will probably package this to resemble something like pwnlib, i suspect. (kitchen sink is good.)
# i think i want this to be a CLI lib more than anything else; quick scripts and tooling only.
# anything resembling a real library or piece of software should not depend on any of this code; i expect it to be too much in flux.
