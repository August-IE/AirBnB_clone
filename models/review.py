#!/usr/bin/python3
"""A Review class that inherits form BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a class review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review test.
    """

    place_id = ""
    user_id = ""
    text = ""
