Python Color Printer
====================

This package provides a class to print colored output on the terminal.

Author: Felix Widmaier


Installation
------------

To install the package use the `setup.py`:

    python setup.py install


Usage
-----

This is a simple example how to use the color printer:

    from colorprinter import cprint
    cprint.red().echo("This text is red")
    cprint.blue().bold().echo("This text is blue and bold")

For more details type

    import colorprinter
    help(colorprinter.ColorPrinter)
