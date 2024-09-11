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

    def reload(self):
        """read from json"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
                FileStorage.__objects = obj_dict
                """obj = json.load(f)
                for k, v in obj.items():
                    clsn = v['__class__']
                    self.__objects[k] = globals()[clsn](**v)"""
