from UserInterface import UserInterface
import matplotlib.pyplot as plt
CAR_TYPES = ["suv", "hatchback", "sedan"]
OWNER_PASSWORD = "CRS100" 
# Owner Interface
class OwnerInterface(UserInterface):
    """Interface for owner operations"""
    
    def main_menu(self):
        """Display the owner menu and process selections"""
        while True:
          #  self.display_header("\033[1;35m🔑 OWNER MENU 🔑\033[0m")  # Purple header for Owner Menu
        
            print("\n" + "=" * 40)
            print("📌  OWNER MENU OPTIONS ".center(40))
            print("=" * 40)
            print("\033[1;34m1️⃣  Show Cars\033[0m")  
            print("\033[1;34m2️⃣  Add Car\033[0m")  
            print("\033[1;34m3️⃣  Remove Car\033[0m")  
            print("\033[1;34m4️⃣  Track Customer Activity\033[0m")  
            print("\033[1;34m5️⃣  Show Net Turnover\033[0m")  
            print("\033[1;34m6️⃣  Car Details\033[0m")  
            print("\033[1;34m7️⃣  Back to Main Menu\033[0m")  
            print("-" * 40)

            owner_choice = input("\n\033[1;36m🔹 Enter your choice:\033[0m ")  # Cyan input prompt

            if owner_choice == "1":
                print("\n\033[1;33m🚘 Displaying available cars...\033[0m")  # Yellow text
                self.show_cars()

            elif owner_choice == "2":
                print("\n\033[1;32m➕ Adding a new car...\033[0m")  # Green text
                self.add_car()

            elif owner_choice == "3":
                print("\n\033[1;31m🗑 Removing a car...\033[0m")  # Red text
                self.remove_car()

            elif owner_choice == "4":
                print("\n\033[1;36m📊 Tracking customer activity...\033[0m")  # Cyan text
                self.track_customer_activity()

            elif owner_choice == "5":
                print("\n\033[1;35m💰 Calculating net turnover...\033[0m")  # Purple text
                self.show_net_turnover()

            elif owner_choice == "6":
                print("\n\033[1;33m📄 Showing car details...\033[0m")
                self.show_car_details()

            elif owner_choice == "7":
                print("\n\033[1;31m🚪 Returning to Main Menu...\033[0m")
                break

            else:
                print("\n\033[1;31m❌ Invalid choice! Please try again.\033[0m")  # Red error message


    def add_car(self):
        """Add a new car to the inventory"""
        self.display_header("Add New Car")
        
        car_type = input("Enter the Type: ").lower()
        
        if car_type not in CAR_TYPES:
            print("\n*** Oops! Invalid Type. ***")
            return
            
        model = input("\nEnter Car Model: ").title()
        rent_price = int(input("Rent Price: "))
        word_file_path = input("Enter WordFile Path : ")
        
        success = self.db.add_car(car_type, model, rent_price, word_file_path)
        
        if success:
            print("\n=== Car Added Successfully ===\n")
        else:
            print("\n*** This car is already in the Collection! ***\n")
    
    def remove_car(self):
        """Remove a car from the inventory"""
        self.display_header("Remove Car")
        
        car_type = input("Enter the Type: ").lower()
        
        if car_type not in CAR_TYPES:
            print("\n*** Oops! Invalid Type. ***")
            return
            
        model = input("\nEnter Car Model to Remove: ").title()
        
        success = self.db.remove_car(car_type, model)
        
        if success:
            print("\n=== Model Removed Successfully ===\n")
        else:
            print("\n*** No such model found in the collection! ***\n")
    
    def track_customer_activity(self):
        """Generate a report of customer activity"""
        self.display_header("Track Customer Activity")
        
        if self.db.customer_activity:
            self.db.save_activity_log()
            print("\n*** Customer activity file generated in your directory! ***\n")
        else:
            print("\n*** No activity recorded yet! ***\n")
    
    def show_net_turnover(self):
        """Display revenue analytics using matplotlib"""
        fig, axes = plt.subplots(1, 4, figsize=(24, 6))
        
        grand_total = 0
        
        # Create pie charts for each category
        for ax, (category, cars) in zip(axes[:-1], self.db.car_revenue.items()):
            labels = list(cars.keys())
            values = list(cars.values())
            
            subtotal = sum(values)
            grand_total += subtotal
            
            # Identify highest revenue car
            max_index = values.index(max(values)) if values else 0
            explode = [0.1 if i == max_index else 0 for i in range(len(values))]
            
            # Function to format currency
            def format_currency(value):
                return f"₹{value:,.0f}"
            
            # Create pie chart
            wedges, texts, autotexts = ax.pie(
                values,
                labels=labels,
                autopct=lambda p: format_currency(p * sum(values) / 100) if values else "₹0",
                startangle=90,
                explode=explode,
                wedgeprops={'edgecolor': 'black'},
                shadow=True
            )
            
            # Style text
            for autotext in autotexts:
                autotext.set_color('black')
                autotext.set_fontsize(10)
                
            ax.set_title(f"{category.title()} Revenue Distribution\nSubtotal: {format_currency(subtotal)}", fontsize=14)
        
        # Display grand total
        axes[-1].axis("off")
        axes[-1].text(
            0.5, 0.5,
            f"TOTAL REVENUE : \n{format_currency(grand_total)}",
            fontsize=18, fontweight="bold", ha="center", va="center", color="darkred"
        )
        
        plt.tight_layout()
        plt.show()