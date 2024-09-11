#!/usr/bin/python3
import uuid
from models.engine.file_storage import storage
from datetime import datetime


class BaseModel:
    """Base class"""
    def __init__(self, *arg, **kwargs):
        """initialization"""
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            storage.new(self)

    def __str__(self):
        """str"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """save obj"""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """returns dict"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
