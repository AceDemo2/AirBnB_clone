#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')

    def test_id(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))

if __name__ == '__main__':
    unittest.main()
