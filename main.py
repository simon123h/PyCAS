#! python3
# TODO: Kommentare auf englisch uebersetzen
from mathexpr import *
from trs import *
# from patternmatching import *


# testing

x = Wildcard("x")
m = Add(Int(5), Int(6))
p = Add(x, Int(6))
r = Mul(x, Int(2))

a = Int(3) + Int(4)


# TODO: nichtassoziative/nichtkommutative Operatoren
# TODO: elaborate Number classes
# TODO: Kommentare schreiben
# TODO: InfinityRules
