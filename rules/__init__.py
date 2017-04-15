
# Init script.
# Loaded, when the package is imported.
# Defines the namespace elements to be imported with the package

__all__ = [
    'all',
    'arithmetics',
    'infinity'
]

from .arithmetics import arithmeticRules as arithmetics
from .infinity import infinityRules as infinity

# All rules
all = arithmetics + infinity
