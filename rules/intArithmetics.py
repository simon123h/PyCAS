from mathexpr.atom import Wildcard, Int
from mathexpr.elementary import Add, Mul, Div, Pow
from mathexpr.specialNumbers import Zero, One, Infinity
from trs.rule import Rule, DeepRule, RuleSet, RuleRegistry


intAdd = RuleSet(
    # Fallback to hardcoded evaluation rules
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


# Evaluate a product of all Ints list
def product(factors):
    result = 1
    for factor in factors:
        result *= factor
    return result


intMul = RuleSet(
    # Fallback to hardcoded evaluation rules
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

intSub = RuleSet(
    Rule(
        Wildcard("a") - Wildcard("b"),
        Wildcard("a") + (Int(-1) * Wildcard("b"))
    )
)

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


intArithmetics = RuleRegistry(intAdd, intSub, intMul, intDiv, intPow)
