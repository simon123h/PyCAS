from .Rule import Rule, RuleSet, RuleRegistry
from mathexpr.atom import Wildcard, Int
from mathexpr.elementary import Div, Pow
from mathexpr.specialNumbers import Zero, One, Infinity


intAdd = RuleSet(
    Rule(
        Wildcard("a"),     # Fallback to hardcoded evaluation rules
        Wildcard("a").eval()     # TODO: doesnt work!! FIX!!
    ),
    Rule(
        Zero + Wildcard(),
        Wildcard()
    )
)

intMul = RuleSet(
    Rule(
        # Fallback to hardcoded evaluation rules
        Wildcard("a", Int),
        Wildcard("a").eval()
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


integerArithmetic = intAdd + intSub + intMul + intDiv + intPow

arithm = RuleRegistry([integerArithmetic])
