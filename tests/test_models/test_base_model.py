#!/usr/bin/bash/python3
"""tests"""
import unittest
from models.base_model import BaseModel
import datetime import datetime
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """test cases for basemodel class"""
    
    @classmethod
    def setUpClass(cls):
        """create instance"""
        cls.ins = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """cleaan up"""
        del cls.ins

    def test_instancecreation(self):
        """test case for instance creation"""
        self.assertIsInstance(self.ins, BaseModel)
        self.assertIsInstance(self.ins.id, str)
        self.assertIsInstance(self.ins.created_at, datetime)
        self.assertIsInstance(self.ins.updated_at, datetime)
        self.assertEqual(self.ins.created_at, self.ins.updated_at)

    def test_id(self):
        """check id"""
        ins2 = BaseModel()
        self.assertNotEqual(self.ins.id, ins2.id)

    def test_save(self):
        """check save"""
        oldtime = self.ins.updated_at
        self.ins.save()
        self.assertNotEqual(self.ins.update_at, oldtime)

    def test_dic(self):
        """check dictionary"""
        dic = self.ins.to_dict()
        self.assertEqual(dic['updated_at'], self.ins.updated_at.isoformat())
        self.assertEqual(dic['created_at'], self.ins.created_at.isoformat())
        self.assertEqual(dic['id'], self.ins.id)
        self.assertEqual(dic['__class__'], self.ins.__name__)
    
    def test_str(self):
        """check str output"""
        strout = str(self.ins) 
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(strout, expected) 

class TestFileStorage:
    """test cases for file storage"""
    
    @classmethod
    def setUpClass(cls):
        """create storage instance"""
        cls.storage = storage.FileStorage()
        cls.ins = BaseModel()
        cls.ins.name = 'Model'
        cls._file_path = cls.storage._FileStorage__file_path
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """cleaan up"""
        del cls.ins
        try:
            os.remove(cls.file_path)
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
        self.assertEqual(obj[f"BaseModel.{self.ins.id}"]['name'], 'Model')
    
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
        self.assertIn(f'{BaseModel}.{nmodel.id}', obj)
        self.assertEqual(obj[f"BaseModel.{nmodel.id}"]['name'], 'new_model')


if __name__ == "__main__":
    unittest.main()
