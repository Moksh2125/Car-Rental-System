# Car Rental System

A Python-based Car Rental System that provides a seamless experience for both customers and owners. The system allows customers to rent cars, view car details, and generate invoices, while owners can manage the car inventory, track customer activity, and view revenue analytics.

## Features

### For Customers:
- **View Available Cars**: Browse cars by category (SUV, Hatchback, Sedan) with rental rates.
- **Rent a Car**: Select a car, specify rental duration, and agree to terms and conditions.
- **Return a Car**: Process car returns and update the system.
- **Generate Invoice**: Get a detailed bill for rented cars.

### For Owners:
- **Manage Inventory**: Add or remove cars from the system.
- **Track Customer Activity**: Generate a log of customer activities.
- **View Revenue Analytics**: Visualize revenue distribution using pie charts.
- **Access Car Details**: Open detailed car documents.

## Project Structure
CarRentalSystem/ ├── CarsDetails/ # Contains car detail documents ├── CustomerActivity.txt # Log of customer activities ├── Moksh_Bill.txt # Example bill for a customer ├── TermsAndCondtions.txt # Terms and conditions for renting ├── Database.py # Handles data storage and retrieval ├── OwnerInterface.py # Owner-specific interface ├── CustomerInterface.py # Customer-specific interface ├── UserInterface.py # Base class for user interfaces ├── main.py # Entry point for the application ├── requirements.txt # Python dependencies └── Revolutionizing-Car-Rentals-A-Seamless-System.pptx # Presentation

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CarRentalSystem

2. Install dependencies:
    pip install -r requirements.txt

## Usage
- **Run the application:** python main.py

- **Follow the on-screen instructions to:**

- Log in as an owner or customer.
- Register as a new customer if needed.
- Perform various operations like renting cars, managing inventory, or viewing analytics.

### Dependencies
The project uses the following Python libraries:

- matplotlib for revenue analytics visualization.
- os for file operations.
- abc for abstract base classes.
Refer to requirements.txt for the full list of dependencies.

### File Descriptions
- main.py: Entry point of the application. Handles authentication and navigation.
- Database.py: Manages data storage, retrieval, and updates.
- UserInterface.py: Base class for user interfaces.
- OwnerInterface.py: Implements owner-specific functionalities.
- CustomerInterface.py: Implements customer-specific functionalities.
- TermsAndCondtions.txt: Contains the terms and conditions for renting cars.
- CustomerActivity.txt: Logs customer activities.
### Example Data
- Terms and Conditions
- Refer to TermsAndCondtions.txt for the full terms and conditions.

### Customer Activity
- Example log:

- **Name    CarType     NameOfModel     TotalRent   BookedDate   ReturnDate**
- **Krish   Hatchback   Ford Figo       3400        02/02/2025   ---**
- **Mohit   SUV         Jeep Compass    4500        13/01/2025   13/01/2025**

### Future Enhancements
- Add support for online payment integration.
- Implement a web-based interface for easier access.
- Enhance the analytics dashboard with more visualizations.
