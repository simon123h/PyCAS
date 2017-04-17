#! python3
from mathexpr import * # noqa
from trs.rule import Rule, DeepRule, RuleSet # noqa
import rules # noqa


r = Rule(Wildcard("a", Int) * Wildcard("b", Int), Wildcard("a", Int) + Wildcard("b", Int))
a = Int(2) * Int(3) * Int(4)

ce = Div(Int(5), Var("x")) - Div(Var("y"), Int(2))

simp = rules.all.apply
