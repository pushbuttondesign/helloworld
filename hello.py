#!/usr/bin/env python3
# shebang for linux

#!/usr/local/bin/python3
# shebang for mac osx

"""
MODULE DESCRIPTION: prints hello world & acts as python3 template

MODULE USAGE EXAMPLE:
>>> main();
hello world
"""

# import std lib
# import 3rd party lib
# import usr lib

# global var

# start debugging
#pdb.set_trace()
DEBUG = 0;

def main():
    """
    MODULE TITLE: main

    MODULE DESCRIPTION: main

    EXAMPLES:
    >>> main();
    hello world
    """

    try:
        print("hello world");
    except:
        print("something went wrong");

    if DEBUG == 1:
        None;
        return;

    return;

# script autorun
if __name__ == "__main__":

    # run program
    main();

    # unit test
    import doctest;
    doctest.testmod();
    