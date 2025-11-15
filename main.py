# main.py
from inventory_system import InventorySystem

def main():
    """Main function to run the Baby Shop Inventory System"""
    print("Initializing Baby Shop Inventory System...")
    print("Loading predefined products...")
    
    # Create and run the inventory system
    system = InventorySystem()

    print("\nSystem ready! Predefined products loaded:")
    print("- Baby Bottle (BP001)")
    print("- Diapers Pack (BP002)") 
    print("- Soft Teddy Bear (BP003)")
    print("- Baby Onesie (BP004)")
    print("- Baby Monitor (BP005)")
    print("- Baby Shampoo (BP006)")
    print("- Teething Ring (BP007)")
    print("- Stroller (BP008)")
    print("- Baby Wipes (BP009)")
    print("- Rattle Toy (BP010)")
    
    # Start the system
    system.run()

if __name__ == "__main__":
    main()
