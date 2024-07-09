#!/usr/bin/python3
"""
class with common attributes for other classes to inherit from

"""

from datetime import datetime
import uuid

class BaseModel:
    """Defines all common attributes
    """

    def __init__(self, *args, **kwargs):
        """initialises all attributes in class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at'
                value = datetime.now()
                format_date = value.isoformat()
                setattr(self, key, format_date)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now();
            self.updated_at = self.created_at

    def __str__(self):
        """prints class name, id and attribute dictionary
        """
        print("[{}] ({}) {}".format(type(self).__name__, self.d, self.__dict__))

    def save(self):
        """updates updated_at attribute with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        """

        new_dictionary  = self.__dict__.copy()
        
        for key, value in new_dictionary:
            if key == "created_at" or key == "updated_at":
                new_dictionary[key] == value.isoformat()
            
            else:
                if value:
                    new_dictionary(key) = value

            new_dictionary["__class__"] = self.__class__.__name__
        
        return new_dictionary










