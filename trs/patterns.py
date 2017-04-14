from mathexpr.expr import Expression
from mathexpr.atom import Atom, Wildcard


# returns boolean if pattern matches expr (including Wildcards)
# and returns a list of required Wildcard substitutions to turn
# pattern into expr
def match(expr, pattern):
    if not isinstance(pattern, Expression):     # is pattern a Expression?
        return False, []
    if pattern.isa(Wildcard):                   # Wildcards always match
        return True, [(pattern, expr)]          # but return requirements
    if expr.isa(Wildcard):
        return True, [(expr, pattern)]
    if expr.type != pattern.type:               # check for equality, like in __eq__
        return False, []
    if expr.isa(Atom) or pattern.isa(Atom):     # no recursion for Atoms
        return expr == pattern, []
    if len(expr.args) is not len(pattern.args):
        return False, []
    requirements = []
    for arg1, arg2 in zip(expr.args, pattern.args):     # match children recursively
        argsMatch, argReqs = match(arg1, arg2)
        if not argsMatch:
            return False, []
        for argReq in argReqs:                  # check for wildcard
            for req in requirements:            # substitution collisions
                if req[0] == argReq[0] and not req[1] == argReq[1]:
                    return False, []
        requirements += argReqs
    return True, requirements


# Replace part of expr matching pattern by new
def replace(expr, pattern, new):
    for perm in expr.perms():
        matching, requirements = match(perm, pattern)
        if matching:                         # if pattern matches expr,
            for wc, sub in requirements:     # substitute wildcards into new
                new = new.set(wc, sub)
            return new
        if perm.isa(Atom):                   # if not matching: pass recursively
            return perm
        args = [replace(arg, pattern, new) for arg in perm._args]
        return perm.func(*args)
    return expr
