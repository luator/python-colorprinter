# -*- coding: utf-8 -*-

class ColorPrinter:
    """
    Print colored text to the terminal, using ANSI codes.

    Usage
    -----
    The following colors are available using ANSI codes:

     * black
     * red
     * green
     * yellow
     * blue
     * magenta
     * cyan
     * white

    For each color there is a method `color()` that changes the color
    of the text and a method `on_color()` that changes the background.

    Further there are the following methods to change other properties
    of the text:

     * bold()
     * faint()


    Each of these methods returns a new instance of ColorPrinter, where
    the corresponding option is set. To get the resulting string use
    `to_str()` or `echo()` to print it directly.


    Examples
    --------

        cprint = ColorPrinter()

        cprint.red().echo("This text is red")
        cprint.green().on_blue().echo("Green text with blue background")
        cprint.bold().echo("This text is bold")

        foo = cprint.blue().to_str("Get string instead of printing")
    """

    def __init__(self, code_seq=[]):
        self._code_sequence = code_seq


    def to_str(self, text):
        """Return `text` with surrounding ANSI codes."""
        codes = ";".join(self._code_sequence)
        return "\x1b[{}m{}\x1b[0m".format(codes, text)

    def echo(self, text):
        """Print `text` with formatting."""
        print self.to_str(text)


    def black(self):
        return ColorPrinter(self._code_sequence + ["30"])

    def red(self):
        return ColorPrinter(self._code_sequence + ["31"])

    def green(self):
        return ColorPrinter(self._code_sequence + ["32"])

    def yellow(self):
        return ColorPrinter(self._code_sequence + ["33"])

    def blue(self):
        return ColorPrinter(self._code_sequence + ["34"])

    def magenta(self):
        return ColorPrinter(self._code_sequence + ["35"])

    def cyan(self):
        return ColorPrinter(self._code_sequence + ["36"])

    def white(self):
        return ColorPrinter(self._code_sequence + ["37"])


    def on_black(self):
        return ColorPrinter(self._code_sequence + ["40"])

    def on_red(self):
        return ColorPrinter(self._code_sequence + ["41"])

    def on_green(self):
        return ColorPrinter(self._code_sequence + ["42"])

    def on_yellow(self):
        return ColorPrinter(self._code_sequence + ["43"])

    def on_blue(self):
        return ColorPrinter(self._code_sequence + ["44"])

    def on_magenta(self):
        return ColorPrinter(self._code_sequence + ["45"])

    def on_cyan(self):
        return ColorPrinter(self._code_sequence + ["46"])

    def on_white(self):
        return ColorPrinter(self._code_sequence + ["47"])


    def bold(self):
        return ColorPrinter(self._code_sequence + ["1"])

    def faint(self):
        return ColorPrinter(self._code_sequence + ["2"])

# global instance for convenience
cprint = ColorPrinter()
