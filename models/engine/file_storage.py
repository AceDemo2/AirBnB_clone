#!/usr/bin/python3
import json
import os

class FileStorage:
    """store in json"""
    __file_path = 'file.json'
    __objects ={}

    def all(self):
        """return dic"""
        return self.__objects

    def new(self, obj):
        """set obj"""
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """save to json file"""
        with open(self.__file_path, 'w') as f:
            obj = {}
            for k, v in self.__objects.items():
                obj[k] = v.to_dict()
            json.dump(obj, f)
    
    def classes(self):
        """return classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.user import State
        from models.user import City
        from models.user import Amenity
        from models.user import Place
        from models.user import Review
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
    
    def reload(self):
        """read from json"""
        if os.path.exists(self.__file_path):
            obj = {}
            with open(self.__file_path, 'r') as f:
                obj = json.load(f)
            for k, v in obj.items():
                clsn = v['__class__']
                # cls = global().get(clsn)
                self.__objects[k] = self.classes()[clsn](**v)
