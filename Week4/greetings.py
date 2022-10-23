"""
This module holds some very sophisticated functions for displaying greetings.

Author: Neil Drummond
Date:   22nd October, 2022
"""

def print_hello():
    """Print a message appropriate for the start of a conversation."""
    print("Hello!")

def print_goodbye():
    """Print a message appropriate for the end of a conversation."""
    print("Goodbye!")


if __name__=="__main__":
    print_hello()
    print("greetings.py is being executed as a script in its own right.")
    print_goodbye()

# The next couple of lines are just to show what happens when the module is
# imported.  In practice you would rarely want to print anything when a module
# is imported.
else:
    print("Congratulations!  You have just imported the greetings module.")
