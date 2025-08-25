__version__ = "0.1.0"
__author__ = "osmiumnet"

from .xml import XML
from .element import XMLElement
from .attribute import XMLAttribute

__all__ = [
    "XML",
    "XMLElement",
    "XMLAttribute",
]
