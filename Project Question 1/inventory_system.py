# inventory_system.py
import time
from hash_table import HashTable
from models import BabyProduct

class BabyShopStorage:
    """Local storage system for baby products using hash table"""
    
    def __init__(self, size=15):
        self.hash_table = HashTable(size)
        self.predefined_products = [
            ("BP001", "Baby Bottle", "Feeding", 12.99, 50, "0-6 months"),
            ("BP002", "Diapers Pack", "Hygiene", 24.99, 100, "0-12 months"),
            ("BP003", "Soft Teddy Bear", "Toys", 15.99, 30, "6-12 months"),
            ("BP004", "Baby Onesie", "Clothing", 8.99, 75, "0-3 months"),
            ("BP005", "Baby Monitor", "Safety", 89.99, 20, "0-24 months"),
            ("BP006", "Baby Shampoo", "Bathing", 6.99, 40, "0-12 months"),
            ("BP007", "Teething Ring", "Teething", 5.99, 60, "3-9 months"),
            ("BP008", "Stroller", "Travel", 199.99, 15, "0-36 months"),
            ("BP009", "Baby Wipes", "Hygiene", 4.99, 80, "0-12 months"),
            ("BP010", "Rattle Toy", "Toys", 7.99, 45, "3-6 months")
        ]
        self._insert_predefined_products()
    
    def _insert_predefined_products(self):
        """Insert predefined products into the hash table"""
        for product_data in self.predefined_products:
            product_id, name, category, price, quantity, age_range = product_data
            product = BabyProduct(product_id, name, category, price, quantity, age_range)
            self.hash_table.insert(product_id, product)
    
    def get_all_products_array(self):
        """Get all products as array for performance comparison"""
        products = []
        for i in range(self.hash_table.size):
            current = self.hash_table.table[i]
            while current is not None:
                products.append(current.value)
                current = current.next
        return products

class InventorySystem:
    """Command-line Inventory System for baby products"""
    
    def __init__(self):
        self.storage = BabyShopStorage()
        self.products_array = self.storage.get_all_products_array()
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("    BABY SHOP INVENTORY SYSTEM")
        print("="*50)
        print("1. Insert New Product")
        print("2. Search Product")
        print("3. Display All Products")
        print("4. Performance Comparison")
        print("5. Exit")
        print("="*50)
    
    def insert_product(self):
        """Insert a new product into the inventory"""
        print("\n--- INSERT NEW PRODUCT ---")
        
        try:
            product_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            category = input("Enter Category: ").strip()
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            age_range = input("Enter Age Range: ").strip()
            
            existing = self.storage.hash_table.search(product_id)
            if existing:
                print(f"Error: Product ID {product_id} already exists!")
                return
            
            new_product = BabyProduct(product_id, name, category, price, quantity, age_range)
            self.storage.hash_table.insert(product_id, new_product)
            self.products_array = self.storage.get_all_products_array()
            
            print(f"Product '{name}' inserted successfully!")
            
        except ValueError:
            print("Error: Please enter valid numeric values for price and quantity!")
        except Exception as e:
            print(f"Error: {e}")
    
    def search_product(self):
        """Search for a product by ID"""
        print("\n--- SEARCH PRODUCT ---")
        
        product_id = input("Enter Product ID to search: ").strip()
        
        start_time = time.time()
        product = self.storage.hash_table.search(product_id)
        hash_table_time = time.time() - start_time
        
        if product:
            print(f"\nProduct Found:")
            print(product)
            print(f"Search time (Hash Table): {hash_table_time:.6f} seconds")
        else:
            print(f"Product with ID '{product_id}' not found!")
    
    def display_all_products(self):
        """Display all products in the system"""
        print("\n--- ALL PRODUCTS IN INVENTORY ---")
        self.storage.hash_table.display()
    
    def performance_comparison(self):
        """Compare search performance between hash table and array"""
        print("\n--- PERFORMANCE COMPARISON ---")
        
        if not self.products_array:
            print("No products available for comparison!")
            return
        
        test_ids = ["BP001", "BP005", "BP010", "NON_EXISTENT"]
        
        print(f"{'Product ID':<15} {'Hash Table Time':<20} {'Array Time':<15} {'Faster By'}")
        print("-" * 70)
        
        for test_id in test_ids:
            # Hash Table Search
            start_time = time.perf_counter()
            hash_result = self.storage.hash_table.search(test_id)
            hash_time = time.perf_counter() - start_time
            
            # Array Search (Linear Search)
            start_time = time.perf_counter()
            array_result = None
            for product in self.products_array:
                if product.product_id == test_id:
                    array_result = product
                    break
            array_time = time.perf_counter() - start_time
            
            if hash_time < array_time:
                faster_by = f"{array_time/hash_time:.2f}x"
                winner = "Hash Table"
            else:
                faster_by = f"{hash_time/array_time:.2f}x"
                winner = "Array"
            
            print(f"{test_id:<15} {hash_time:<20.6f} {array_time:<15.6f} {faster_by} ({winner})")
        
        print("\n" + "="*70)
        print("PERFORMANCE ANALYSIS:")
        print(f"Total products: {len(self.products_array)}")
        print(f"Hash table size: {self.storage.hash_table.size}")
        print(f"Load factor: {self.storage.hash_table.count / self.storage.hash_table.size:.2f}")
        
        # Run detailed analysis
        self.detailed_performance_analysis()
    
    def detailed_performance_analysis(self):
        """Detailed performance analysis with multiple test cases"""
        print("\n" + "="*60)
        print("DETAILED PERFORMANCE ANALYSIS")
        print("="*60)
        
        products_array = self.storage.get_all_products_array()
        test_cases = [
            ("BP001", "First item"),
            ("BP005", "Middle item"), 
            ("BP010", "Last item in array"),
            ("BP999", "Non-existent item")
        ]
        
        print(f"{'Test Case':<25} {'Hash Table (s)':<15} {'Array (s)':<15} {'Speedup':<10}")
        print("-" * 65)
        
        hash_times = []
        array_times = []
        
        for test_id, description in test_cases:
            # Hash table search (multiple iterations for accuracy)
            hash_time = 0
            for _ in range(1000):
                start = time.perf_counter()
                self.storage.hash_table.search(test_id)
                hash_time += time.perf_counter() - start
            hash_time_avg = hash_time / 1000
            
            # Array search (multiple iterations for accuracy)
            array_time = 0
            for _ in range(1000):
                start = time.perf_counter()
                for product in products_array:
                    if product.product_id == test_id:
                        break
                array_time += time.perf_counter() - start
            array_time_avg = array_time / 1000
            
            hash_times.append(hash_time_avg)
            array_times.append(array_time_avg)
            
            speedup = array_time_avg / hash_time_avg if hash_time_avg > 0 else 0
            print(f"{description + ' (' + test_id + ')':<25} "
                  f"{hash_time_avg:<15.8f} {array_time_avg:<15.8f} {speedup:.2f}x")
        
        print("\n" + "="*65)
        print("SUMMARY STATISTICS:")
        print(f"Average Hash Table Search Time: {sum(hash_times)/len(hash_times):.8f} seconds")
        print(f"Average Array Search Time: {sum(array_times)/len(array_times):.8f} seconds")
        print(f"Overall Speedup: {sum(array_times)/sum(hash_times):.2f}x")
        print("\nCONCLUSION: Hash table provides consistent O(1) performance while")
        print("array search varies from O(1) to O(n), making hash tables superior")
        print("for frequent search operations in inventory systems.")
    
    def run(self):
        """Main method to run the inventory system"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                self.insert_product()
            elif choice == '2':
                self.search_product()
            elif choice == '3':
                self.display_all_products()
            elif choice == '4':
                self.performance_comparison()
            elif choice == '5':
                print("Thank you for using Baby Shop Inventory System!")
                break
            else:
                print("Invalid choice! Please try again.")