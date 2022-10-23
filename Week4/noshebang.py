# Some Python code:
if 2+2==5:
    print("Orwellian nightmare.")
else:
    print("Freedom.")

# COMMENT OUT THE ABOVE CODE AND RERUN THE SCRIPT...

# On Linux or a Mac it will execute the following shell script using the
# default shell:

echo -e "Toto, I've a feeling we aren't in Python anymore...\nShell: $SHELL\n"

if ((2+2==5)); then
  echo "Orwellian nightmare."
else
  echo "Freedom."
fi

# Outcome will be different in Windows, where the .py extension specifies
# Python.

# In any case, it is usually good practice to provide a shebang in the very
# first line to clarify what program will be used to run a script.  Usual
# shebang for Python:

#!/usr/bin/env python
