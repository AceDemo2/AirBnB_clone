#!/usr/bin/python3
"""tests"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """test cases for file storage"""
    
    @classmethod
    def setUpClass(cls):
        """create storage instance"""
        cls.storage = FileStorage()
        cls.ins = BaseModel()
        cls.ins.name = 'Model'
        cls._file_path = cls.storage._FileStorage__file_path
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """cleaan up"""
        del cls.ins
        try:
            os.remove(cls._file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """check all method"""
        self.assertIsInstance(self.storage.all(), dict)
   
    def test_reload(self):
        """check reload method"""
        self.storage.reload()
        obj = self.storage.all()
        self.assertIn(f"BaseModel.{self.ins.id}", obj)
        self.assertEqual(obj[f"BaseModel.{self.ins.id}"].name, 'Model')
    
    def test_save(self):
        """check save method"""
        self.assertTrue(os.path.isfile(self._file_path))

    def test_new(self):
        """check new method"""
        nmodel = BaseModel()
        nmodel.name = 'new_model'
        self.storage.new(nmodel)
        self.storage.save()
        self.storage.reload()
        obj = self.storage.all()
        self.assertIn(f'BaseModel.{nmodel.id}', obj)
        self.assertEqual(obj[f"BaseModel.{nmodel.id}"].name, 'new_model')


if __name__ == "__main__":
    unittest.main()
