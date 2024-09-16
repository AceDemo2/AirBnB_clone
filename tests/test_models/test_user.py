#!/usr/bin/python3
"""tests"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """test cases for basemodel class"""
    
    @classmethod
    def setUpClass(cls):
        """create instance"""
        cls.ins = User()
        cls.ins.email = "test1@mail.com"
        cls.ins.password = "password1"
        cls.ins.first_name = "John"
        cls.ins.last_name = "Doe"

    @classmethod
    def tearDownClass(cls):
        """cleaan up"""
        del cls.ins

    def test_instancecreation(self):
        """test case for instance creation"""
        self.assertIsInstance(self.ins, User)
        self.assertIsInstance(self.ins.id, str)
        self.assertIsInstance(self.ins.created_at, datetime)
        self.assertIsInstance(self.ins.updated_at, datetime)
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)
        self.assertEqual(self.user1.email, "test1@mail.com")
        self.assertEqual(self.user1.password, "password1")
        self.assertEqual(self.user1.first_name, "John")
        self.assertEqual(self.user1.last_name, "Doe")
    
    def test_id(self):
        """check id"""
        ins2 = User()
        self.assertNotEqual(self.ins.id, ins2.id)

    def test_save(self):
        """check save"""
        oldtime = self.ins.updated_at
        self.ins.save()
        self.assertNotEqual(self.ins.updated_at, oldtime)

    def test_dic(self):
        """check dictionary"""
        dic = self.ins.to_dict()
        self.assertEqual(dic['updated_at'], self.ins.updated_at.isoformat())
        self.assertEqual(dic['created_at'], self.ins.created_at.isoformat())
        self.assertEqual(dic['id'], self.ins.id)
        self.assertEqual(dic['__class__'], self.ins.__class__.__name__)
    
    def test_str(self):
        """check str output"""
        strout = str(self.ins) 
        expected = f"[User] ({self.ins.id}) {self.ins.__dict__}"
        self.assertEqual(strout, expected) 

if __name__ == "__main__":
    unittest.main()
