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
        Wildcard()
    ),
    Rule(
        Infinity * Zero,
        Zero
    ),
    Rule(
        Infinity * Wildcard("x", Num, lambda e: e.val > 0),
        Infinity
    ),
    Rule(
        Infinity * Wildcard("x", Num, lambda e: e.val < 0),
        NegativeInfinity
    ),
    DeepRule(
        lambda e: Undefined if Undefined in e.args else e
    )
)
