from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []        
    name = sample(ADJECTIVES + NOUNS, k=10)
    for i in range(30):
        products.append(name)
        return products
    
def inventory_report(products):
    for i in products:
        print(len(products))
        print(products)
        return
            
    
    
if __name__ == '__main__':
    inventory_report(generate_products())
       


