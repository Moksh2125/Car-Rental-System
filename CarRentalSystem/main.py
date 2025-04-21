from Database import Database
from OwnerInterface import OwnerInterface
from CustomerInterface import CustomerInterface
# Constants
CAR_TYPES = ["suv", "hatchback", "sedan"]
OWNER_PASSWORD = "CRS100"   

# Authentication and Main Application
class CarRentalSystem:
    """Main application class"""
    
    def __init__(self):
        self.db = Database()
        self.user_objects = {}  # Store user interface objects
    
    def start(self):
        """Start the application"""
        self.main_menu()

    def main_menu(self):
        """Display main menu and handle user selection"""
        while True:
            print("\n" + "=" * 40)
            print("\033[1;35m🚗  WELCOME TO CAR RENTAL SYSTEM  🚗\033[0m".center(40))  # Purple Title
            print("=" * 40)

            print("\n\033[1;36m🔑 Login as:\033[0m")  # Cyan header
            print("\n\033[1;34m1️⃣  Owner\033[0m")  
            print("\033[1;34m2️⃣  New User\033[0m")  
            print("\033[1;34m3️⃣  Existing User\033[0m")  
            print("\033[1;34m4️⃣  Exit\033[0m")  
            print("-" * 40)

            choice = input("\n\033[1;36m🔹 Enter your choice:\033[0m ")  # Cyan text input

            if choice == "1":
                print("\n\033[1;33m🔐 Redirecting to Owner Login...\033[0m")  # Yellow message
                self.owner_login()

            elif choice == "2":
                print("\n\033[1;32m📝 Registering a new user...\033[0m")  # Green message
                self.register_new_user()

            elif choice == "3":
                print("\n\033[1;34m👤 Logging in as Existing User...\033[0m")  # Blue message
                self.existing_user_login()

            elif choice == "4":
                print("\n\033[1;31m||| Thank you for using the Car Rental System. Goodbye! |||\033[0m")  # Red message
                break

            else:
                print("\n\033[1;31m❌ Invalid choice! Please try again.\033[0m")  # Red error message


    def owner_login(self):
        """Handle owner login"""
        password = input("Enter the owner password: ")
        
        if password != OWNER_PASSWORD:
            print("\n*** Incorrect password! ***")
            return
            
        print("\n================ Welcome Owner ==================")
        owner_interface = OwnerInterface(self.db)
        owner_interface.main_menu()
    
    def register_new_user(self):
        """Register a new customer"""
        name = input("\nEnter Your Name: ")
        
        # Check if user already exists
        if name in self.db.customer_details:
            print("\n=== You are already Signed In! ===\n")
            return
            
        password = input("Create a password : ")
        confirm_password = input("Confirm password : ")
        if confirm_password != password:
            print("Oops!! confirm password is wrong.")
            return
        
        # Get user details
        number = input("Enter your Number: ")
        while len(str(number)) != 10:
            number = input("Enter Valid Number: ")
            
        aadhar_num = input("Enter Your Aadhar Number: ")
        while len(aadhar_num) != 12:
            aadhar_num = input("Enter 12-digit number: ")
            
        license_expiry = input("Enter your Licence Expiry Date (DD/MM/YYYY): ")
        
        # Add user to database
        self.db.add_customer(name, password, number, aadhar_num, license_expiry)
        
        # Create and store user interface
        customer_interface = CustomerInterface(self.db, name)
        self.user_objects[name] = customer_interface
        
        # Go to customer menu
        customer_interface.main_menu()
    
    def existing_user_login(self):
        """Handle existing user login"""
        name = input("\nEnter Name to Sign In: ")
        
        if name not in self.db.customer_details:
            print("\n*** Name not found! Please register first. ***\n")
            return
        
        check_password = input("Enter your password : ")
        if check_password != self.db.customer_details[name][0]:
            print("\n*** Incorrect Password ***")
            return
        
        # Go to customer menu
        self.user_objects[name].main_menu()


# Application entry point
if __name__ == "__main__":
    app = CarRentalSystem()
    app.start()