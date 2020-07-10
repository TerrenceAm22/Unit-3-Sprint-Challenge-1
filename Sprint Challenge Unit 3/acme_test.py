import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """ Making sure Acme products are the tops!
    """
    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
   
    def test_default_product_explode(self):
        prod = Product('A cool toy')
        self.assertTrue(prod.explode, "boom")
    
    def test_steal(self):
        prod = Product('A cool toy')
        self.assertTrue(prod.stealability, "Very Stealable")


if __name__ == '__main__':
    unittest.main()
