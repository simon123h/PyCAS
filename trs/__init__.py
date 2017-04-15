

# Init script.
# Loaded, when the package is imported.
# Defines the namespace elements to be imported with the package

__all__ = [
    'DeepRule', 'Rule', 'RuleSet'
]

from .rule import DeepRule, Rule, RuleSet
