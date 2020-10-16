import string
import sys
# import argparse
import logging

helpstr = '''
  ROTs 0 to 25
  usage: 
    python rotn.py STRING
    python rotn.py FILENAME
    printf 'foo' | python rotn.py
'''
# you can also import as module: export PYTHONPATH /home/ian/py and then import rot

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# default level is warning

# parser = argparse.ArgumentParser()
# parser.parse_args()
# eh, not too useful because i want highly versatile behavior

def rotn(instr, n):
    '''rotate instr by n characters'''
    instr = instr.lower()

    mapping = string.ascii_lowercase
    mapping = mapping[n:] + mapping[0:n]

    d = dict(zip(string.ascii_lowercase, mapping))

    s = ""

    for c in instr:
        if d.get(c):
            s += d.get(c)
        else:
            s += c
        
    return s

def rot13(instr):
    '''rot13 instr'''
    return rotn(instr,13)

def main():
    # get input into a variable
    instr = ""

    if not sys.stdin.isatty():
        logging.debug("received input on stdin, string is being piped in")
        instr = sys.stdin.read()
    else:
        # invocation was `python rotn.py`
        if len(sys.argv) < 2:
            logging.debug("no input on stdin, no args; printing help message")
            print(helpstr)
            sys.exit()

        # invocation was `python rotn.py STRING`
        instr = sys.argv[1]

        try:
            logging.debug("checking for filename")
            # first, check for a filename in the current dir
            f = open(instr)
            instr = f.read()
        except OSError:
            # if that fails, it's just a string literal, maybe it has spaces
            logging.debug("no file found, assuming string literal")

    logging.info("input string was: " + str(instr))

    # now the fun part

    for n in range(26):
        num = str(n).rjust(2)
        print(num, rotn(instr,n))

    # i should probably just rewrite this in JS so i can paste the strings into a browser

if __name__ == "__main__":
    main()
