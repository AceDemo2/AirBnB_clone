import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, '')
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, '')

    def test_id(self):
        city = City()
        self.assertTrue(hasattr(city, 'id'))

if __name__ == '__main__':
    unittest.main()
