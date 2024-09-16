#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def test_instance_creation(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')

    def test_id(self):
        state = State()
        self.assertTrue(hasattr(state, 'id'))

if __name__ == '__main__':
    unittest.main()

