#!/usr/bin/env python3
# test_base_model.py
"""Unit test for base_model
"""
import unittest
import datetime

from models.base_model import BaseModel

class TestBaseModelInstatiation(unittest.TestCase):
    """Unittests for instantiation of BaseModel class
    """
    def test_uuid_not_equal(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    @unittest.skip("future tasks may not need this test")
    def test_instatiate_no_args(self):
        pass

    @unittest.skip("to be implemented for task 4")
    def test_instantiate_with_args(self):
        pass

    def test_updated_at_and_created_at_equal_on_instantiation(self):
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)


class TestBaseModelInstance(unittest.TestCase):
    """Unittest for BaseModel instance
    """
    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_id_attribute(self):
        self.assertIn('id', self.base.__dict__)

    def test_created_at_attribute(self):
        self.assertIn('created_at',  self.base.__dict__)

    def test_created_at_attribute_type(self):
        self.assertTrue(isinstance(self.base.created_at, datetime.datetime))

    def test_updated_at_attribute(self):
        self.assertIn('updated_at', self.base.__dict__)

    def test_updated_at_attribute_type(self):
        self.assertTrue(isinstance(self.base.updated_at, datetime.datetime))

    def test_save(self):
        prev_update_at = self.base.updated_at
        self.base.my_number = 89
        self.base.save()
        self.assertNotEqual(prev_update_at, self.base.updated_at)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            self.base.save("arg")

    def test_to_dict_is_type_dict(self):
        self.assertTrue(isinstance(self.base.to_dict(), dict),
                msg=f"to_dict returns none dict type")

    def test_to_dict_contains_externally_added_attributes(self):
        self.base.my_number = 98
        self.assertIn("my_number", self.base.to_dict())

    def test_classname_in_to_dict(self):
        model_dict = self.base.to_dict()
        self.assertIn('__class__', model_dict,
                msg="key __class__ not found")
        self.assertEqual(model_dict.get("__class__"), 'BaseModel',
                msg="Invalid class name")
