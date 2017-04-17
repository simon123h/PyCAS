"""
RuleSets for elementary arithmetics
"""
# TODO: rename file to elementary?

from mathexpr.atom import Wildcard, Int, Undefined
from mathexpr.elementary import Add, Mul, Div, Pow
from mathexpr.specialNumbers import Zero, One, Infinity
from trs.rule import Rule, DeepRule, RuleSet

nonExceptWC = Wildcard(
    matchFunc=lambda e: e is not Infinity, excludeType=[Undefined])

# Integer Addition rules (top node is Addition)
intAdd = RuleSet(
    # DeepRules fallback to hardcoded evaluation rules
    DeepRule(
        lambda expr: expr.args[0] if len(expr.args) == 1 else expr,
        matchType=Add
    ),
    DeepRule(
        lambda expr: Int(sum([arg.val for arg in expr.args])) if len(
            expr.args) > 1 and all(arg.isa(Int) for arg in expr.args) else expr,
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
        lambda expr: Int(product([arg.val for arg in expr.args])) if len(expr.args) > 1 and all(
            arg.isa(Int) for arg in expr.args) else expr,
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
    ),
    Rule(
        Pow(Zero, Wildcard()),
        Zero
    ),
    Rule(
        Pow(One, Wildcard()),
        One
    ),
    DeepRule(
        lambda e: Int(e.args[0].val**e.args[1].val) if all(arg.isa(Int)
                                                           for arg in e.args) else e,
        matchType=Pow
    )
)

# Subtraction rules
intSub = RuleSet(
    Rule(
        Wildcard("a") - Wildcard("b"),
        Wildcard("a") + (Int(-1) * Wildcard("b"))
    ),
    Rule(
        nonExceptWC - nonExceptWC,
        Zero
    )
)

# Division rules
intDiv = RuleSet(
    # Rule(
    #     Div(Wildcard("a"), Wildcard("b")),
    #     Wildcard("a") * Pow(Wildcard("b"), Int(-1))
    # ),
    Rule(
        Div(Wildcard(), Int(0)),
        Infinity
    ),
    DeepRule(
        lambda e: Int(int(e.args[0].val / e.args[1].val)) if all(arg.isa(Int)
                                                                 for arg in e.args) and e.args[0].val % e.args[1].val == 0 else e,
        matchType=Div
    ),
    Rule(
        nonExceptWC / nonExceptWC,
        One
    )
)


# combine all to a common RuleSet
# take care on order for good performance
arithmeticRules = intAdd + intSub + intMul + intDiv + intPow
