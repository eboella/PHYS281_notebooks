#!/usr/bin/env python

# Demonstrate importing a module.

import greetings
from greetings import print_goodbye

greetings.print_hello()

help(greetings)

help(greetings.print_hello)

print_goodbye()
