#/usr/bin/python3
"""user"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User class"""
    place_id = ''
    user_id = ''
    text = ''
