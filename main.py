#! python3
from mathexpr import * # noqa
from trs.rule import Rule, DeepRule, RuleSet # noqa
import rules # noqa


r = Rule(Wildcard("a", Int) * Wildcard("b", Int), Wildcard("a", Int) + Wildcard("b", Int))
a = Int(2) * Int(3) * Int(4)

# helping function: Evaluate a product of all Ints list
def product(factors):
    result = 1
    for factor in factors:
        result *= factor
    return result

r2 = DeepRule(
    lambda expr: Int(product([arg.val for arg in expr.args])) if len(expr.args) > 1 and all(
        arg.isa(Int) for arg in expr.args) else expr,
    matchType=Mul
)
