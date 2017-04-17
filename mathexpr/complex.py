"""
Class for complex numbers
"""

from .expr import Expression


# TODO: elaborate
class Complex(Expression):
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return "(" + self.re.__str__() + " + " + self.im.__str__()+"i" + ")"
