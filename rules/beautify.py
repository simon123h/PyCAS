"""
RuleSets for term beautification
"""


from mathexpr.atom import Num, Constant, Var, Atom
# from mathexpr.elementary import Add, Mul, Div, Pow, Sub
# from mathexpr.specialNumbers import Zero, One, Infinity
from trs.rule import DeepRule, RuleSet


# order arguments in commutative operators
def orderScore(expr):
    if expr.isa(Num):
        return 0
    if expr.isa(Constant):
        return 1
    if expr.isa(Var):
        return 2
    return 3


orderRules = RuleSet(
    DeepRule(
        lambda e: e.func(*sorted(e.args, key=orderScore)) if e.isCommutative else e,
        excludeType=Atom,
        name="reorder terms"
    )
)


beautify = orderRules
