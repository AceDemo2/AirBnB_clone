#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def test_instance_creation(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, '')
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, '')
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, '')

    def test_id(self):
        review = Review()
        self.assertTrue(hasattr(review, 'id'))

if __name__ == '__main__':
    unittest.main()
