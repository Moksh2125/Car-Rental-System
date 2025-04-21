from UserInterface import UserInterface
CAR_TYPES = ["suv", "hatchback", "sedan"]
OWNER_PASSWORD = "CRS100"
# Customer Interface
class CustomerInterface(UserInterface):
    """Interface for customer interactions"""
    
    def __init__(self, database, name):
        super().__init__(database)
        self.name = name
    
    def main_menu(self):
        """Display the customer menu and process selections"""
        self.display_header(f"🚗  Welcome, {self.name}! 🚗")
    
        while True:
            print("\n" + "=" * 40)
            print(" 📌  CUSTOMER MENU ".center(40))
            print("=" * 40)
            print("\033[1;34m1️⃣  Show Available Cars\033[0m")  
            print("\033[1;34m2️⃣  Show Car Details\033[0m")  
            print("\033[1;34m3️⃣  Rent a Car\033[0m")  
            print("\033[1;34m4️⃣  Return a Car\033[0m")  
            print("\033[1;34m5️⃣  Get Invoice\033[0m")  
            print("\033[1;34m6️⃣  Back to Main Menu\033[0m")  
            print("-" * 40)

            customer_choice = input("\n\033[1;36m🔹 Enter your choice:\033[0m ")  # Cyan text input

            if customer_choice == "1":
                print("\n\033[1;33m🔍 Showing available cars...\033[0m")  # Yellow text
                self.show_cars()

            elif customer_choice == "2":
                print("\n\033[1;33m📄 Fetching car details...\033[0m")
                self.show_car_details()

            elif customer_choice == "3":
                print("\n\033[1;32m🛒 Proceeding to rent a car...\033[0m")
                self.rent_car()

            elif customer_choice == "4":
                print("\n\033[1;32m🔄 Processing car return...\033[0m")
                self.return_car()

            elif customer_choice == "5":
                print("\n\033[1;35m🧾 Generating invoice...\033[0m")  # Purple text
                self.generate_bill()

            elif customer_choice == "6":
                print("\n\033[1;31m🚪 Returning to Main Menu...\033[0m")  # Red text
                break

            else:
                print("\n\033[1;31m❌ Invalid choice! Please select a valid option.\033[0m")  # Red error message

    
    def rent_car(self):
        """Process for a customer to rent a car"""
        car_type = input("Enter car type (SUV/Hatchback/Sedan): ").lower()
        
        if car_type not in CAR_TYPES:
            print("Oops! Wrong car type. Please choose a valid car type.")
            return
            
        model = input("\nEnter the car model you want to rent: ").title()
        
        if model not in self.db.car_rental_rates[car_type]:
            print("\n=== Sorry, the requested car model is not available. ===\n")
            return
            
        days = int(input("Enter the number of days you want to rent the car: "))
        ac_choice = input("Do you want AC features (yes/no)? : ").lower()
        
        ac_cost = 0
        if ac_choice == "yes":
            ac_cost = self.db.ac_charges[car_type]
            
        rental_date = input("Enter today's date (DD/MM/YYYY): ")
        
        # Show terms and conditions
        with open("TermsAndCondtions.txt", "r") as file:
            terms = file.read()
            print("Terms and Conditions:")
            print(terms)
            
        agree = input("Do you agree to the terms and conditions? (yes/no): ")
        if agree.lower() != "yes":
            print("You must agree to the terms and conditions to rent a car.")
            return
            
        # Process the rental
        success, total_rent = self.db.rent_car(
            self.name, car_type, model, ac_cost, days, rental_date
        )
        
        if success:
            print("\n=== Car rented successfully!! ===\n")
        else:
            print("\n=== Failed to rent the car. Please try again. ===\n")
    
    def return_car(self):
        """Process for a customer to return a rented car"""
        
        car_type = input("Enter car type (SUV/Hatchback/Sedan): ").lower()
        if car_type not in CAR_TYPES:
            print("Oops! Wrong car type. Please choose a valid car type.")
            return
        
        model = input("\nEnter Model name: ").title()
        return_date = input("Enter returning date (DD/MM/YYYY): ")
        
        success = self.db.return_car(self.name, car_type, model, return_date)
        
        if success:
            print("\n=== Car returned successfully! ===\n")
        else:
            print("\n=== No car rented with your name and model. ===\n")
    
    def generate_bill(self):
        """Generate a bill for the customer's rentals"""
        rented_cars = self.db.get_rented_cars(self.name)
        
        if not rented_cars:
            print("\n=== There is no bill available. ===\n")
            return
            
        with open(self.name + "_Bill.txt", 'w') as bill:
            bill.write(f"============== Bill ==============\nCarType\tModel\t\tAC Charges\tRentPerHour\tTotal\n")
            temp, total = "", 0
            
            for tupple, value in rented_cars.items():
                temp += f"{tupple[1]}\t{tupple[2]}\t{tupple[3]}\t{tupple[4]}\t\t {value}\n"
                total += value
                
            temp += f"-------------------------------------------------\n\tGrand Total : {total}"
            bill.write(temp)
            
        print("\n=== Bill is generated in your directory. ===\n")