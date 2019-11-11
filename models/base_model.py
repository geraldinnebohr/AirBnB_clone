#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #self.my_number = 0
            #self.name = ''
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(kwargs[key], "%Y-%m-%dT %H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT %H:%M:%S.%f")
        new_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT %H:%M:%S.%f")
        return new_dict
