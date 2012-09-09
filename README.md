android-scripts
===============

A collection of rough and ready utility scripts to aid with android
development.

debug.sh
--------
debug.sh is a small script I use to build, manage and deploy my Android
projects from the command line using Ant.

Building, re-installing and launching your project is as easy as:

    $ ./debug.sh -x

from the project root.

Commands used in the various steps can be overridden with environment
variables, have a look at the usage message or browse through the script for
more info.  (Maven is a nicer solution to all this but there are some problems
with Maven currently that I can't stand).

get\_strings.py
---------------
Takes an en strings.xml and outputs the bare strings.
Use to seed a new Google Doc for sharing with translators.

strings\_generate.py
--------------------
Takes an en strings.xml and a list of translations, and outputs a new
strings.xml file mapping those translations.
