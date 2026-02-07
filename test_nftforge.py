# test_nftforge.py
"""
Tests for NFTForge module.
"""

import unittest
from nftforge import NFTForge

class TestNFTForge(unittest.TestCase):
    """Test cases for NFTForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTForge()
        self.assertIsInstance(instance, NFTForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
