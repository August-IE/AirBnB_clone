#!/usr/bin/python3
"""A class City that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a class city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
