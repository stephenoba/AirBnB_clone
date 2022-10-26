#!/usr/bin/env python3
# test_base_model.py
"""Unit test for base_model
"""
import uuid
import unittest
from datetime import datetime

from models.base_model import BaseModel

class TestBaseModelInstatiation(unittest.TestCase):
    """Unittests for instantiation of BaseModel class
    """
    def setUp(self):
        self.base = BaseModel()
        self.date = datetime.now()

    def tearDown(self):
        del self.base

    def test_uuid_not_equal(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    @unittest.skip("future tasks may not need this test")
    def test_instatiate_no_args(self):
        pass

    def test_instantiate_with_args(self):
        new_base = BaseModel(id=89,
                created_at=self.date.isoformat(),
                updated_at=self.date.isoformat())
        self.assertEqual(new_base.id, 89)
        self.assertEqual(new_base.created_at, self.date)
        self.assertEqual(new_base.updated_at, self.date)

    def test_updated_at_and_created_at_equal_on_instantiation(self):
        self.assertEqual(self.base.created_at, self.base.updated_at)

    def test_instantiate_from_dict(self):
        new_base = BaseModel(**self.base.to_dict())
        self.assertFalse(new_base is self.base)
        self.assertEqual(new_base.id, self.base.id)

    @unittest.skip("Confirm what error should be raised")
    def test_instantiate_from_invalid_dict(self):
        _dict = {"invalid_id": 345, "invalid_date": "0-0-0"}
        with self.assertRaises(Exception):
            new_base = BaseModel(**_dict)

    def test_instantiate_invalid_id_None(self):
        _dict = {"created_at": self.date, "updated_at": self.date}
        with self.assertRaises(TypeError):
            new_base = BaseModel(id=None, **_dict)

    def test_instantiate_invalid_id_nonstring(self):
        _dict = {"created_at": self.date, "updated_at": self.date}
        with self.assertRaises(TypeError):
            new_base = BaseModel(id=12437563, **_dict)

    def test_instantiate_invalid_date_format(self):
        date = '2022/10/26T09:35:24.972474'
        _id = str(uuid.uuid4())
        _dict = {"id": _id, "created_at": date, "updated_at": date}
        with self.assertRaises(ValueError):
            new_base = BaseModel(**_dict)

    def test_args_not_empty(self):
        new_base = BaseModel(123)
        self.assertTrue(hasattr(new_base, "id"))
 
    def test_object_has_same_attributes(self):
        new_base = BaseModel(**self.base.to_dict())
        for key in self.base.to_dict().keys():
            self.assertEqual(getattr(new_base, key),
                    getattr(self.base, key))

class TestBaseModelInstance(unittest.TestCase):
    """Unittest for BaseModel instance
    """
    def setUp(self):
        self.base = BaseModel()
        self.base.my_number = 89

    def tearDown(self):
        del self.base

    def test_id_attribute(self):
        self.assertIn('id', self.base.__dict__)

    def test_created_at_attribute(self):
        self.assertIn('created_at',  self.base.__dict__)

    def test_created_at_attribute_type(self):
        self.assertTrue(isinstance(self.base.created_at, datetime))

    def test_updated_at_attribute(self):
        self.assertIn('updated_at', self.base.__dict__)

    def test_updated_at_attribute_type(self):
        self.assertTrue(isinstance(self.base.updated_at, datetime))

    def test_save(self):
        prev_update_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(prev_update_at, self.base.updated_at)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            self.base.save("arg")

    def test_to_dict_is_type_dict(self):
        self.assertTrue(isinstance(self.base.to_dict(), dict),
                msg=f"to_dict returns none dict type")

    def test_to_dict_contains_externally_added_attributes(self):
        self.assertIn("my_number", self.base.to_dict())

    def test_classname_in_to_dict(self):
        model_dict = self.base.to_dict()
        self.assertIn('__class__', model_dict,
                msg="key __class__ not found")
        self.assertEqual(model_dict.get("__class__"), 'BaseModel',
                msg="Invalid class name")
