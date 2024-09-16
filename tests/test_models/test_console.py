#!/usr/bin/python3
"""Unit tests for console.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNB command interpreter"""

    def test_help(self):
        """Test the 'help' command output"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_quit(self):
        """Test the 'quit' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue()
            self.assertEqual(output, "")

    def test_create(self):
        """Test the 'create' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            new_id = f.getvalue().strip()
            self.assertTrue(len(new_id) > 0)

    def test_show(self):
        """Test the 'show' command"""
        # First, create a new instance to show
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            new_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {new_id}")
            output = f.getvalue().strip()
            self.assertIn(new_id, output)

    def test_destroy(self):
        """Test the 'destroy' command"""
        # Create an instance first to destroy
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            new_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {new_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

        # Test that the instance no longer exists
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {new_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """Test the 'all' command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_update(self):
        """Test the 'update' command"""
        # First, create an instance to update
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            new_id = f.getvalue().strip()

        # Now, update the instance
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {new_id} name 'My_Model'")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

        # Test if the attribute was updated
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {new_id}")
            output = f.getvalue().strip()
            self.assertIn("'name': 'My_Model'", output)


if __name__ == "__main__":
    unittest.main()

