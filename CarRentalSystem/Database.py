CAR_TYPES = ["suv", "hatchback", "sedan"]
OWNER_PASSWORD = "CRS100" 

class Database:
    """Manages all data storage and retrieval operations"""
    
    def __init__(self):
        # Car inventory data
        self.car_details = {
            1: ("Toyota Fortuner", "CarsDetails\\ToyotaFortuner.docx"),
            2: ("Mahindra Scorpio", "CarsDetails\\MahindraScorpio.docx"),
            3: ("Jeep Compass", "CarsDetails\\JeepCompass.docx"),
            4: ("Maruti Suzuki Swift", "CarsDetails\\MarutiSuzukiSwift.docx"),
            5: ("Hyundai I10", "CarsDetails\\Hyundaii10.docx"),
            6: ("Tata Altroz", "CarsDetails\\TataAltroz.docx"),
            7: ("Honda City", "CarsDetails\\HondaCity.docx"),
            8: ("Hyundai Verna", "CarsDetails\\HyundaiVerna.docx"),
            9: ("Maruti Suzuki Ciaz", "CarsDetails\\MarutiSuzukiCiaz.docx"),
        }
        
        # Car revenue data
        self.car_revenue = {
            "suv": {
                "Toyota Fortuner": 15000,
                "Mahindra Scorpio": 7000,
                "Jeep Compass": 4500,
            },
            "hatchback": {
                "Maruti Suzuki Swift": 4500,
                "Hyundai I10": 2800,
                "Tata Altroz": 6400,
            },
            "sedan": {
                "Honda City": 6000,
                "Hyundai Verna": 5600,
                "Maruti Suzuki Ciaz": 5400,
            }
        }
        
        # Car rental rates
        self.car_rental_rates = {
            "suv": {
                "Toyota Fortuner": 5000,
                "Mahindra Scorpio": 3500,
                "Jeep Compass": 4500,
            },
            "hatchback": {
                "Maruti Suzuki Swift": 1500,
                "Hyundai I10": 1400,
                "Tata Altroz": 1600,
            },
            "sedan": {
                "Honda City": 3000,
                "Hyundai Verna": 2800,
                "Maruti Suzuki Ciaz": 2700,
            }
        }
        
        # AC charges per car type
        self.ac_charges = {
            "suv": 1200,
            "hatchback": 600,
            "sedan": 300
        }
        
        # Customer data
        self.customer_details = {
            "Krish": ["pass123","8945456660", "12341234132", "31/5/2040"],
            "Mohit": ["pass122","9999888822", "11441144141", "31/4/2030"]
        }
        
        # Currently rented cars
        self.rented_cars = {
            ("Krish", "Hatchback", "Ford Figo", 600, 1400): 3400
        }
        
        # Customer activity log
        self.customer_activity = [
            ["Krish", "Hatchback", "Ford Figo", "3400", "02/02/2025"],
            ["Mohit", "SUV", "Jeep Compass", "4500", "13/01/2025", "13/01/2025"]
        ]
    
    def add_customer(self, name, password, number, aadhar, license_expiry):
        """Add a new customer to the database"""
        self.customer_details[name] = [password, number, aadhar, license_expiry]
        return True
    
    def get_customer(self, name):
        """Retrieve customer details"""
        return self.customer_details.get(name)
    
    def add_car(self, car_type, model, rent_price, file_path):
        """Add a new car to the inventory"""
        if car_type not in CAR_TYPES:
            return False
            
        # Check if car already exists
        if any(model in sub_dict for sub_dict in self.car_rental_rates.values()) or any(model in tupple for tupple in self.rented_cars):
            return False
            
        # Add to car rental rates
        self.car_rental_rates[car_type][model] = rent_price
        
        # Initialize revenue for the car
        self.car_revenue[car_type][model] = 0
        
        # Add car details document
        next_id = len(self.car_details) + 1
        self.car_details[next_id] = (model, file_path)
        
        return True
    
    def remove_car(self, car_type, model):
        """Remove a car from the inventory"""
        if car_type not in CAR_TYPES or model not in self.car_rental_rates[car_type]:
            return False
            
        # Remove from rental rates
        del self.car_rental_rates[car_type][model]
        
        # Remove from revenue tracking
        del self.car_revenue[car_type][model]
            
        # Remove from car details
        for car_id, (car_name, _) in list(self.car_details.items()):
            if car_name == model:
                del self.car_details[car_id]
                break
                
        return True
    
    def rent_car(self, name, car_type, model, ac_cost, days, rental_date):
        """Record a car rental transaction"""
        if car_type not in CAR_TYPES or model not in self.car_rental_rates[car_type]:
            return False, 0
            
        rent_per_day = self.car_rental_rates[car_type][model]
        total_rent = rent_per_day * days + ac_cost
        
        # Remove car from available inventory temporarily
        temp_rental_rate = self.car_rental_rates[car_type][model]
        del self.car_rental_rates[car_type][model]
        
        # Add to rented cars
        car_key = (name, car_type, model, ac_cost, temp_rental_rate)
        self.rented_cars[car_key] = total_rent
        
        # Update revenue
        self.car_revenue[car_type][model] += total_rent - ac_cost
        
        # Add to activity log
        customer_details = [name, car_type, model, str(total_rent), rental_date]
        self.customer_activity.append(customer_details)
        
        return True, total_rent
    
    def return_car(self, name, car_type, model, return_date):
        """Process a car return"""
        # Find the car in activity log
        found = False
        for index, details in enumerate(self.customer_activity):
            if (name in details and 
                car_type.lower() in details and 
                model in details and 
                len(details) == 5):  # Not returned yet (no return date)
                
                # Add return date
                self.customer_activity[index].append(return_date)
                found = True
                break
                
        if not found:
            return False
            
        # Find car in rented cars and return to inventory
        for car_tuple in list(self.rented_cars.keys()):
            rented_person, rented_type, rented_model, _, rent_per_hour = car_tuple
            
            if (rented_person == name and 
                rented_model == model and 
                rented_type.lower() == car_type.lower()):
                
                # Return car to available inventory
                self.car_rental_rates[car_type][model] = rent_per_hour
                
                # Remove from rented list
                del self.rented_cars[car_tuple]
                return True
                
        return False
    
    def get_rented_cars(self, name=None):
        """Get list of rented cars, optionally filtered by customer name"""
        if name:
            return {k: v for k, v in self.rented_cars.items() if k[0] == name}
        return self.rented_cars
    
    def save_activity_log(self):
        """Save customer activity to a file"""
        with open("CustomerActivity.txt", 'w') as file:
            file.write("Name\tCarType\tNameOfModel\tTotalRent\tBookedDate\tReturnDate\n")
            for line in self.customer_activity:
                if len(line) == 5:  # Not returned yet
                    file.write("\n" + "\t".join(line) + "\t---")
                else:
                    file.write("\n" + "\t".join(line))
        return True