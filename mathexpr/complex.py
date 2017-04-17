"""
Class for complex numbers
"""


# TODO: elaborate
class Complex():
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return "(" + self.re.__str__() + " + " + self.im.__str__()+"i" + ")"
