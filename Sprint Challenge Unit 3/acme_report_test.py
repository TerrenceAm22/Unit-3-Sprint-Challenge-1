import unittest
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeReportTest(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_number_of_products(self):
        """Test default product price being 10."""
        self.assertEqual(generate_products, 30)
        
if __name__ == '__main__':
    unittest.main()
