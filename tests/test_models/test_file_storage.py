#!/usr/bin/python3
"""Contains unittests for models/engine/file_storage.py"""

import unittest
import json
from datetime import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_Instantiation(unittest.TestCase):
    """Unittests for instantiation of FileStorage class"""

    def test_FileStorage_instantiation_with_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


class TestFileStorage_Methods(unittest.TestCase):
    """Unittests for the methods of FileStorage class"""

    def test_new(self):
        models.storage.new(BaseModel())
        bmd = BaseModel()
        self.assertIn("BaseModel." + bmd.id, models.storage.all().keys())
        self.assertIn(bmd, models.storage.all().values())

    def test_save(self):
        pass

