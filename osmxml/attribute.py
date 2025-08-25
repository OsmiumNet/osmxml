from .xml import XML   

class XMLAttribute(XML):
    def __init__(self, name: str, value: str):
        self._name = name
        self._value = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    def to_string(self) -> str:
        return '{name}="{value}"'.format(name=self.name, value=self.value)
