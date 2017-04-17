"""
RuleSets for term beautification
"""


from mathexpr.atom import Constant, Var, Atom, Int, Real
# from mathexpr.elementary import Add, Mul, Div, Pow, Sub
# from mathexpr.specialNumbers import Zero, One, Infinity
from trs.rule import DeepRule, RuleSet


# order arguments in commutative operators
def orderScore(expr):
    if expr.isa(Int):
        return 0
    if expr.isa(Real):
        return 3
    if expr.isa(Constant):
        return 4
    if expr.isa(Var):
        return 5
    return 6


orderRules = RuleSet(
    DeepRule(
        lambda e: e.func(*sorted(e.args, key=orderScore)) if e.isCommutative else e,
        excludeType=Atom,
        name="reorder terms"
    )
)


beautify = orderRules
