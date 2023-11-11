#!/usr/bin/python3
"""A class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a class State.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
