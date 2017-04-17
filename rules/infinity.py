"""
Rules on how Infinity and NegativeInfinity behave
"""

from mathexpr.atom import Num, Wildcard, Undefined
# from mathexpr.elementary import Mul
from mathexpr.specialNumbers import Zero, Infinity, NegativeInfinity
from trs.rule import Rule, DeepRule, RuleSet


infinityRules = RuleSet(
    Rule(
        Infinity + Wildcard(),
        Infinity,
        name=Infinity.__str__() + " dominates addition"
    ),
    Rule(
        Infinity * Zero,
        Zero,
        name="0 * oo = 0"
    ),
    Rule(
        Infinity * Wildcard("x", Num, lambda e: e.val > 0),
        Infinity,
        name="Infinity dominates multiplication"
    ),
    Rule(
        Infinity * Wildcard("x", Num, lambda e: e.val < 0),
        NegativeInfinity,
        name="Infinity dominates multiplication"
    ),
    DeepRule(
        lambda e: Undefined if Undefined in e.args else e,
        name="undefined dominates expression"
    )
)
