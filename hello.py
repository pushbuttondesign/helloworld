#!/usr/bin/env python3
# shebang for linux

#!/usr/local/bin/python3
# shebang for mac osx

"""
MODULE DESCRIPTION

MODULE FEATURES
"""

# import std lib
import sys
# import 3rd party lib
# import usr lib

# global var

# start debugging
#import pdb
#pdb.set_trace()
DEBUG = 0;

def main(argv):
    """
    FUNCTION DESCRIPTION
    OTHER COMMENTS

    INPUTS
    OUTPUTS

    EXAMPLES
    >>> main();
    hello world
    """

    try:
        print("hello world");
    except ValueError as err:
        print("something went wrong: %s" % err, file=sys.stderr);

    return;

# script autorun
if __name__ == "__main__":

    #run program
    try:
        main(sys.argv);
    except UserWarning as err:
        print("%s" % err, file=sys.stderr);
        exit(1);

    if DEBUG == 1:
        # unit test
        import doctest;
        doctest.testmod();
