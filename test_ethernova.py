# test_ethernova.py
"""
Tests for EtherNova module.
"""

import unittest
from ethernova import EtherNova

class TestEtherNova(unittest.TestCase):
    """Test cases for EtherNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherNova()
        self.assertIsInstance(instance, EtherNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
