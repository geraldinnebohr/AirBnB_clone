#!/usr/bin/python3
import json
import os.path
from models.base_model import BaseModel

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
            first_dict[key] = val.to_dict()
        print(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(first_dict, f)
            
    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as q:
                other_dict = json.loads(q.read())
                for key, val in other_dict.items():
                    FileStorage.__objects[key] = BaseModel(val)
                    