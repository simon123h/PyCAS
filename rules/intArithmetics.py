"""
RuleSets for Integer arithmetics
"""

from mathexpr.atom import Wildcard, Int
from mathexpr.elementary import Add, Mul, Div, Pow
from mathexpr.specialNumbers import Zero, One, Infinity
from trs.rule import Rule, DeepRule, RuleSet, RuleRegistry


# Integer Addition rules (top node is Addition)
intAdd = RuleSet(
    # DeepRules fallback to hardcoded evaluation rules
    DeepRule(
        lambda expr: expr.args[0] if len(expr.args) == 1 else expr,
        matchType=Add
    ),
    DeepRule(
        lambda expr: Int(sum([arg.val for arg in expr.args])) if all(arg.isa(Int) for arg in expr.args) else expr,
        matchType=Add
    ),
    Rule(
        Zero + Wildcard(),
        Wildcard()
    )
)


# helping function: Evaluate a product of all Ints list
def product(factors):
    result = 1
    for factor in factors:
        result *= factor
    return result


# Integer Multiplication rules (top node is Multiplication)
intMul = RuleSet(
    # DeepRules fallback to hardcoded evaluation rules
    DeepRule(
        lambda expr: expr.args[0] if len(expr.args) == 1 else expr,
        matchType=Mul
    ),
    DeepRule(
        lambda expr: Int(product([arg.val for arg in expr.args])) if all(arg.isa(Int) for arg in expr.args) else expr,
        matchType=Mul
    ),
    Rule(
        Zero * Wildcard(),
        Zero
    ),
    Rule(
        One * Wildcard(),
        Wildcard()
    )
)

# Integer exponentiation rules
intPow = RuleSet(
    Rule(
        Pow(Wildcard(), Zero),
        One
    ),
    Rule(
        Pow(Wildcard(), One),
        Wildcard()
    )
)

# Subtraction rules
intSub = RuleSet(
    Rule(
        Wildcard("a") - Wildcard("b"),
        Wildcard("a") + (Int(-1) * Wildcard("b"))
    )
)

# Division rules
intDiv = RuleSet(
    Rule(
        Div(Wildcard("a"), Wildcard("b")),
        Wildcard("a") * Pow(Wildcard("b"), Int(-1))
    ),
    Rule(
        Div(Wildcard(), Int(0)),
        Infinity
    )
)


# combine all to a common RuleSet/RuleRegistry
# take care on order for good performance
# TODO: make this a set, RuleRegistry should not be needed at all
intArithmetics = RuleRegistry(intAdd, intSub, intMul, intDiv, intPow)
