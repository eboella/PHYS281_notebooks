#!/usr/bin/env python

# Demonstrate importing a module containing a class and a function.

# Some different ways of dealing with imports.
import greetings
from greetings import greeter as gr # Import greeter class, renaming it as gr.

help(greetings)      # Display help about the module.  Press "q" to quit.
help(gr)             # Display help about the greeter class.
help(gr.print_hello) # Display help about the print_hello method.

user=gr("user")    # Equivalent to:  user=greetings.greeter("user")
user.print_hello()

# We can use the function defined in the greetings module.
print("Here is a random name: {0:s}".format(greetings.random_name()))

# random was imported into the greetings module, so is available here.
print("Here is a random number: {0:.15g}".format(greetings.random.random()))

user.print_goodbye()
