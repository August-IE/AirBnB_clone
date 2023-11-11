#!/usr/bin/python3
""" A class Amenity that inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a class amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
