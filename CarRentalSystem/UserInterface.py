import os
from abc import ABC, abstractmethod

# Constants
CAR_TYPES = ["suv", "hatchback", "sedan"]
OWNER_PASSWORD = "CRS100"

# UI Module - Base class for all user interfaces
class UserInterface(ABC):
    """Base class for all user interfaces"""
    
    def __init__(self, database):
        self.db = database
    
    def display_header(self, title, width=40):
        """Display a formatted header"""
        print("\n" + "=" * width)
        print(f" {title} ".center(width))
        print("=" * width)
    
    def show_cars(self):
        """Display available cars with rental rates"""
        self.display_header("🚘  WELCOME TO CAR RENTAL MENU  🚘")
        
        while True:
            print("\n\033[1;34m📌 Choose a Car Category:\033[0m")
            print("\033[1;33m1. SUV\n2. Hatchback\n3. Sedan\033[0m")
            print("-" * 40)
            
            car_type = input("\n\033[1;36m🔹 Enter your choice (type name):\033[0m ").lower()
            
            if car_type in CAR_TYPES:
                self.display_header(f"🚗  Cars in Category: \033[1;32m{car_type.title()}\033[0m  🚗")
                print(f"\033[1;35m{'Car Name':<25}{'Rent Per Day (₹)':<15}\033[0m")
                print("-" * 40)
                
                for car, rent in self.db.car_rental_rates[car_type].items():
                    print(f"\033[1;37m{car:<25} ₹{rent:<15}\033[0m")
                
                print("-" * 40)
                
                choice = input("\n\033[1;34m🔄 Do you want to check another category? (yes/no):\033[0m ").lower()
                if choice == "no":
                    print("\n\033[1;32m✅ Thank you for using our service! 🚗✨\033[0m")
                    break
            else:
                print("\n\033[1;31m❌ Invalid choice! Please try again.\033[0m")
    
    def show_car_details(self):
        """Display detailed information about specific cars"""
        self.display_header("🚗  WELCOME TO CAR DETAILS  🚗", 30)
        
        for index, (car, file) in self.db.car_details.items():
            print(f" ▶️  Press {index} for \033[1;32m{car}\033[0m")
        
        print("=" * 30)
        
        try:
            index = int(input("\n\033[1;34m📌 Enter the index here:\033[0m "))
            file_path = self.db.car_details[index][1]
            
            print(f"\n\033[1;33m📂 Opening {self.db.car_details[index][0]} details...\033[0m")
            os.startfile(file_path)
            
        except KeyError:
            print("\n\033[1;31m❌ Invalid selection! Please choose a valid index.\033[0m")
            
        except Exception as e:
            print(f"\n\033[1;31m⚠️ Error:\033[0m {e}")
    
    @abstractmethod
    def main_menu(self):
        """Main menu for the interface - must be implemented by subclasses"""
        pass