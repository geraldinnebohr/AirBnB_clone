#!/usr/bin/python3
"""
class user the best important
"""
from models.base_model import BaseModel


class User(BaseModel):
    """inheritated class User from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """the init constructor"""
        super().__init__(**kwargs)
