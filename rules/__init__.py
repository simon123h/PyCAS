
# Init script.
# Loaded, when the package is imported.
# Defines the namespace elements to be imported with the package

__all__ = [
    'all',
    'arithmetics',
    'infinity',
    'beautify'
]

from .arithmetics import arithmeticRules as arithmetics
from .infinity import infinityRules as infinity
from .beautify import beautify as beautify

# All rules
all = arithmetics + infinity + beautify
