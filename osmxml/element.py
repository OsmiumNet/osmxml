from typing import Optional, List

from .xml import XML   
from .attribute import XMLAttribute

class XMLElement(XML):
    def __init__(
            self, 
            name: str, 
            attributes: Optional[List[XMLAttribute]] = None,
            children: Optional[List[XML]] = None,
        ):
        self._name = name 
        self._attributes = attributes if attributes is not None else []
        self._children = children if children is not None else []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


    @property
    def attributes(self) -> List[XMLAttribute]:
        return self._attributes.copy()

    @attributes.setter
    def attributes(self, attributes: List[XMLAttribute]):
        self._attributes = attributes


    @property
    def children(self) -> List[XML]:
        return self._children.copy()

    @name.setter
    def children(self, children: List[XML]):
        self._children = children


    def add_attribute(self, attribute: XMLAttribute):
        self._attributes.append(attribute) 

    def remove_attribute_by_index(self, index: int):
        del self._attributes[index]


    def add_child(self, child: XML):
        self._children.append(child)

    def remove_child_by_index(self, index: int):
        del self._children[index]


    def has_attributes(self):
        return len(self.attributes > 0)

    def has_children(self):
        return len(self.children > 0)


    def to_string(self) -> str:
        attrs_str = self._combine_attributes()

        if (not self.has_children()):
            return "<{name}{attrs}/>".format(name=self.name, attrs=attrs_str)

        children_str = "".join(["\n\t{child}".format(child=child.to_string()) for child in self._children])
       
        element_str = "<{name}{attrs}>{children}\n</{name}>".format(
            name=self.name,
            attrs=attrs_str,
            children=children_str
        )

        return element_str

    def _combine_attributes(self) -> str:
        if (self.has_attributes()):
            return " {attrs}".format(attrs=" ".join(attr.to_string() for attr in self._attributes))
        return ""
