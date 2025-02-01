import numpy as np
import sys
from .StandardScalar import StandardScalar
from .Generator import Generator
from .Output import Output
from .AudiPy import AudiPy 

sys.modules[__name__] = AudiPy()

__all__ = ["AudiPy", "StandardScalar", "Generator", "Output"]
