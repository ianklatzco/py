# rot13 utility functions

# ^ this is shown in pydoc/help

# __all__ = ['rotn','rot13'] # customizes from rot import * and changes what pydoc shows
# used to explicitly specific exports

# the . specifies local dir i think
from ._rot import rotn
from ._rot import rot13

# the following are possible as well; they make tab completion in the repl not
# show a "rot" name. however, if one wishes to use the code directly, this is
# somewhat clunky, since it requires a python ~/py/rot/_rot.py
# from ._rot import rotn
# from ._rot import rot13

# HOWEVER, i learned that you can put a __main__.py.
# this enables you to simple python ~/py/rot to get the script's CLI.
# eventually i will probably package this to resemble something like pwnlib, i suspect.
# i think i want this to be a CLI lib more than anything else; quick scripts and tooling only.
# anything resembling a real library or piece of software should not depend on any of this code; i expect it to be too much in flux.
