"""
This module holds some very sophisticated code for displaying greetings.

Author: Neil Drummond
Date:   22nd October, 2022
"""

import random

class greeter:
    """Class for displaying greetings messages."""

    def __init__(self,name=None):
        self.name=name

    def __str__(self):
        if self.name is None:
            return "Generic greetings."
        return "Greetings for {0:s}.".format(self.name)

    def print_hello(self):
        """Print a message appropriate for the start of a conversation."""
        if self.name is None:
            print("Hello!")
        else:
            print("Hello {0:s}!".format(self.name))

    @staticmethod
    def print_goodbye():
        """Print a message appropriate for the end of a conversation."""
        print("Goodbye!")


def random_name():
    """Return a randomly selected name."""
    return random.choice(("Erlend","Haakon","Paul","Magnus","Thorfinn"))


if __name__=="__main__":
    print("greetings.py is being executed as a script in its own right.")

    g=greeter()
    h=greeter(random_name())

    g.print_hello()
    print(g)

    h.print_hello()
    print(h)

    greeter.print_goodbye()

# The next couple of lines are just to show what happens when the module is
# imported.  In practice you would rarely want to print anything when a module
# is imported.
else:
    print("Congratulations!  You have just imported the greetings module.")
