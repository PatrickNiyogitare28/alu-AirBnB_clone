#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from models.base_model import BaseModel
import os
import time
from io import StringIO
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel."""

    def test_instance(self):
        """Test if object is an instance of BaseModel."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_class_type(self):
        """Test the class type of the instance."""
        base = BaseModel()
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """Test the save method updates the updated_at attribute."""
        base = BaseModel()
        old_time = base.updated_at
        time.sleep(1)
        base.save()
        self.assertNotEqual(base.updated_at, old_time)

    def test_save_creates_file(self):
        """Test if save creates a file.json."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_str_representation(self):
        """Test the string representation of the object."""
        base = BaseModel()
        expected_output = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(base)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        base = BaseModel()
        dict_repr = base.to_dict()
        self.assertEqual(dict_repr['__class__'], base.__class__.__name__)


if __name__ == "__main__":
    unittest.main()
