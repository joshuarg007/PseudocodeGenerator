class ClassModel:
    def __init__(self, class_name, attributes, relationships=None):
        self.class_name = class_name
        self.attributes = attributes
        self.relationships = relationships if relationships else []

    def print_pseudocode(self):
        print(f"class {self.class_name}:")
        print("    Attributes:")
        for attr in self.attributes:
            print(f"        - {attr}")
        if self.relationships:
            print("    Relationships:")
            for relationship in self.relationships:
                print(f"        - {relationship['type']} with {relationship['target_class']}, multiplicity: {relationship['multiplicity']}")


# Define the vehicle model classes and relationships
vehicle_class = ClassModel(
    class_name="Vehicle",
    attributes=["Manufacturer", "VehicleID"],
)

car_class = ClassModel(
    class_name="Car",
    attributes=["CarModel", "NumSeats"],
    relationships=[{"type": "Inheritance", "target_class": "Vehicle", "multiplicity": "1-to-1"}]
)

truck_class = ClassModel(
    class_name="Truck",
    attributes=["TruckModel", "WeightLimit"],
    relationships=[{"type": "Inheritance", "target_class": "Vehicle", "multiplicity": "1-to-1"}]
)

driver_class = ClassModel(
    class_name="Driver",
    attributes=["LicenseNumber", "Name"]
)

car_driver_relationship_1n = {
    "type": "Association",
    "target_class": "Car",
    "multiplicity": "1-to-Many"
}

car_driver_relationship_nn = {
    "type": "Association",
    "target_class": "Car",
    "multiplicity": "Many-to-Many"
}

# Print pseudocode for Vehicle, Car, Truck, and Driver classes
print("Vehicle/Car/Truck Database Model:")
vehicle_class.print_pseudocode()
print()  # Blank line for better readability
car_class.print_pseudocode()
print()
truck_class.print_pseudocode()
print()

# Print pseudocode for Driver class with relationships
print("Car/Driver Database Model (1-N Multiplicity):")
driver_class.relationships.append(car_driver_relationship_1n)
driver_class.print_pseudocode()

print()
print("Car/Driver Database Model (N-N Multiplicity):")
driver_class.relationships = [car_driver_relationship_nn]  # Reset to N-N relationship
driver_class.print_pseudocode()
