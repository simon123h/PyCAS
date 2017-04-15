
# Init script.
# Loaded, when the package is imported.
# Defines the namespace elements to be imported with the package

# IMPORTANT: for the whole CAS to work as a package,
# the subpackages will have to prepend the CAS package name in front of
# their imports! e.g. in trs subpackage file:
# from PyCas.mathexpr.expr import Expression


from PyCas.mathexpr import * # noqa
import PyCas.rules as rules # noqa
