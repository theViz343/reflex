"""A class that holds props to be passed or applied to a component."""

from __future__ import annotations

from reflex.base import Base
from reflex.ivars.object import LiteralObjectVar
from reflex.utils import format


class PropsBase(Base):
    """Base for a class containing props that can be serialized as a JS object."""

    def json(self) -> str:
        """Convert the object to a json-like string.

        Vars will be unwrapped so they can represent actual JS var names and functions.

        Keys will be converted to camelCase.

        Returns:
            The object as a Javascript Object literal.
        """
        return LiteralObjectVar.create(
            {format.to_camel_case(key): value for key, value in self.dict().items()}
        ).json()
