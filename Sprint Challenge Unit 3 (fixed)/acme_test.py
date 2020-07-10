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
class AcmeReportTests(unittest.TestCase):
    def test_product(self):
        products = generate_products(30)
        self.assertEqual(len(products), 30)
    """Attempting stretch I guess
    """
    def test_legal_names(self):
        products = generate_products(30)
        name_pool = ADJECTIVES+NOUNS
        i = 0
        while i < 30:
            x = products[i].name.split()
            for item in x:
                self.assertIn(item, name_pool)
            i += 1



if __name__ == '__main__':
    unittest.main()
