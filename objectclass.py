# Define a class called Car
class Car:
    # Constructor method to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    # Method to start the car
    def start(self):
        self.is_running = True
        print(f"{self.year} {self.make} {self.model} started.")
    
    # Method to stop the car
    def stop(self):
        self.is_running = False
        print(f"{self.year} {self.make} {self.model} stopped.")
    
    # Method to display car info
    def display_info(self):
        status = "running" if self.is_running else "not running"
        print(f"{self.year} {self.make} {self.model} is {status}.")

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Use methods of the Car object
my_car.display_info()  # Display car information
my_car.start()         # Start the car
my_car.display_info()  # Display car information again
my_car.stop()          # Stop the car
my_car.display_info()  # Display car information again
