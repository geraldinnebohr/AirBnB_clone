#!/usr/bin/python3
import json
import os.path
from models.base_model import BaseModel
from models.user import User

class  FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        first_dict = {}
        for key, val in FileStorage.__objects.items():
            if val:
                first_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(first_dict, f)

    def reload(self):
        my_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as q:
                other_dict = json.loads(q.read())
                for key, val in other_dict.items():
                    self.new(my_dict[val['__class__']](**val))
