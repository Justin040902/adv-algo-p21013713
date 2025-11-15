# models.py
class BabyProduct:
    """Entity class for baby products in the retail shop"""
    
    def __init__(self, product_id, name, category, price, quantity, age_range):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)
        self.age_range = age_range
    
    def __str__(self):
        return (f"ID: {self.product_id}, Name: {self.name}, "
                f"Category: {self.category}, Price: ${self.price:.2f}, "
                f"Quantity: {self.quantity}, Age Range: {self.age_range}")