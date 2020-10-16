# rot13 utility functions

# ^ this is shown in pydoc/help

# __all__ = ['rotn','rot13'] # customizes from rot import * and changes what pydoc shows
# used to explicitly specific exports

# the . specifies local dir i think
from .rot import rotn
from .rot import rot13

# the following are possible as well; they make tab completion in the repl not
# show a "rot" name. however, if one wishes to use the code directly, this is
# somewhat clunky.
# from ._rot import rotn
# from ._rot import rot13
