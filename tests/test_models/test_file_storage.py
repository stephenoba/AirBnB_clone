#!/usr/bin/python3
"""Contains unittests for models/engine/file_storage.py"""

import os
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

    def test_class_attributes_private(self):
        storage = FileStorage()
        self.assertTrue("__file_path" not in storage.__dict__)
        self.assertTrue("__objects" not in storage.__dict__)


class TestFileStorage_Methods(unittest.TestCase):
    """Unittests for the methods of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        cls.file_path = "filestore.json"
        cls.initial_obj = BaseModel()

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile(cls.file_path):
            os.remove(cls.file_path)

    def test_storage_exists(self):
        models.storage.reload()
        self.assertTrue(os.path.exists(self.file_path))

    def test_new(self):
        models.storage.new(BaseModel())
        bmd = BaseModel()
        self.assertIn("BaseModel." + bmd.id, models.storage.all().keys())
        self.assertIn(bmd, models.storage.all().values())

    def test_save(self):
        pass

    def test_all(self):
        pass

