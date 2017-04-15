"""
Rules on how Infinity and NegativeInfinity behave
"""

from mathexpr.atom import Wildcard, Num
# from mathexpr.elementary import Mul
from mathexpr.specialNumbers import Zero, Infinity, NegativeInfinity
from trs.rule import Rule, DeepRule, RuleSet


infinityRules = RuleSet(
    Rule(
        Infinity + Wildcard(),
        Wildcard()
    ),
    DeepRule(
        Infinity * Zero,
        Zero
    ),
    DeepRule(
        Infinity * Wildcard("x", Num, lambda e: e.val > 0),
        Infinity
    ),
    DeepRule(
        Infinity * Wildcard("x", Num, lambda e: e.val < 0),
        NegativeInfinity
    )
)
