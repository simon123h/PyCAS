"""
RuleSets for term beautification
"""


from mathexpr.atom import Wildcard, Int, Undefined
from mathexpr.elementary import Add, Mul, Div, Pow, Sub
from mathexpr.specialNumbers import Zero, One, Infinity
from trs.rule import Rule, DeepRule, RuleSet

nonExceptWC = Wildcard(
    matchFunc=lambda e: e is not Infinity, excludeType=[Undefined])
a = Wildcard("a")
b = Wildcard("b")
c = Wildcard("c")
d = Wildcard("d")

# Integer Addition rules (top node is Addition)
intAdd = RuleSet(
    # DeepRules fallback to hardcoded evaluation rules
    DeepRule(
        lambda expr: expr.args[0] if len(expr.args) == 1 else expr,
        matchType=Add,
        name="cancel single argument addition"
    ),
    DeepRule(
        lambda expr: Int(sum([arg.val for arg in expr.args])) if len(
            expr.args) > 1 and all(arg.isa(Int) for arg in expr.args) else expr,
        matchType=Add,
        name="evaluate int addition"
    ),
    Rule(
        Zero + Wildcard(),
        Wildcard(),
        name="cancel addition with zero"
    ),
    Rule(
        Add(a, Add(b, c)),
        Add(a, b, c),
        name="use associative property of +"
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
        matchType=Mul,
        name="cancel single argument multiplication"
    ),
    DeepRule(
        lambda expr: Int(product([arg.val for arg in expr.args])) if len(expr.args) > 1 and all(
            arg.isa(Int) for arg in expr.args) else expr,
        matchType=Mul,
        name="evaluate int multiplication"
    ),
    Rule(
        Zero * Wildcard(),
        Zero,
        name="cancel multiplication with zero"
    ),
    Rule(
        One * Wildcard(),
        Wildcard(),
        name="cancel multiplication with one"
    ),
    Rule(
        Add(a, Add(b, c)),
        Add(a, b, c),
        name="use associative property of Mul"
    )
)

# Integer exponentiation rules
intPow = RuleSet(
    Rule(
        Pow(Wildcard(), Zero),
        One,
        name="cancel exponentiation with zero"
    ),
    Rule(
        Pow(Wildcard(), One),
        Wildcard(),
        name="cancel exponentiation with one"
    ),
    Rule(
        Pow(Zero, Wildcard()),
        Zero,
        name="cancel exponentiation of zero"
    ),
    Rule(
        Pow(One, Wildcard()),
        One,
        name="cancel exponentiation of one"
    ),
    DeepRule(
        lambda e: Int(e.args[0].val**e.args[1].val) if all(arg.isa(Int)
                                                           for arg in e.args) else e,
        matchType=Pow,
        name="evaluate int exponentiation"
    )
)

# Subtraction rules
intSub = RuleSet(
    Rule(
        Sub(Wildcard("a"), Wildcard("b")),
        Wildcard("a") + (Int(-1) * Wildcard("b")),
        name="+ is * with neg. number"
    ),
    Rule(
        nonExceptWC - nonExceptWC,
        Zero,
        "cancel subtraction with equal arguments"
    ),
    Rule(
        Sub(a, Add(b, c)),
        Sub(Sub(a, b), c),
        name="resolve parentheses for + and -"
    )
)

# Division rules
intDiv = RuleSet(
    # Rule(
    #     Div(Wildcard("a"), Wildcard("b")),
    #     Wildcard("a") * Pow(Wildcard("b"), Int(-1)),
    #     name="division is multiplication with inverse"
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
        One,
        "cancel fraction"
    ),
    Rule(
        nonExceptWC / (nonExceptWC * Wildcard("a")),
        One / Wildcard("a"),
        "cancel fraction"
    ),
    Rule(
        (nonExceptWC * Wildcard("a")) / nonExceptWC,
        Div(One, Wildcard("a")),
        "cancel fraction"
    ),
    Rule(
        Mul(Wildcard("a"), Div(Wildcard("b"), Wildcard("c"))),
        Div(Mul(Wildcard("a"), Wildcard("b")), Wildcard("c")),
        "change association of Mul and Div"
    ),
    Rule(
        (a / b) + (c / d),
        (a * d + c * b) / (b * d),
        name="find common denominator"
    )
)


# combine all to a common RuleSet
# take care on order for good performance
arithmeticRules = intAdd + intSub + intMul + intDiv + intPow
