import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel with unique ID and creation time."""

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())  # unique id converted to string
        self.created_at = datetime.now()  # current datetime for creation
        self.updated_at = datetime.now()  # updated_at same as as created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, tform))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        # Copy the instance's __dict__ and add the __class__ key
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO 8601 format strings
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
