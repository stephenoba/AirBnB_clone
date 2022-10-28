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
        try:
            os.rename("filestore.json", "tmp")
        except IOError:
            pass
        models.storage.save()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("filestore.json")
            os.rename("tmp", "filestore.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_storage_exists(self):
        self.assertTrue(os.path.exists("filestore.json"))

    def test_new(self):
        # models.storage.new(BasieModel())
        bmd = BaseModel()
        self.assertIn("BaseModel." + bmd.id, models.storage.all().keys())
        self.assertIn(bmd, models.storage.all().values())

    def test_save(self):
        bmd = BaseModel()
        models.storage.save()
        with open("filestore.json", encoding='utf8')as f:
            _dict = json.load(f)
            self.assertIn("BaseModel." + bmd.id, _dict)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

