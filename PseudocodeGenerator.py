import yaml  # Import the PyYAML library to handle YAML file operations.

class ClassModel:
    def __init__(self, class_name, attributes=None, methods=None, inherits=None, description=None):
        # Initialize the ClassModel with provided class details.
        self.class_name = class_name  # Set the name of the class.
        self.attributes = attributes if attributes else []  # Initialize attributes; default to empty list if None.
        self.methods = methods if methods else []  # Initialize methods; default to empty list if None.
        self.inherits = inherits  # Set the parent class for inheritance, if any.
        self.description = description  # Store a description of the class for better understanding.

    def to_dict(self):
        # Convert the class model to a dictionary for easy YAML serialization.
        return {
            "class_name": self.class_name,  # Include class name.
            "description": self.description,  # Include class description.
            "attributes": [{ "name": attr[0], "type": attr[1] } for attr in self.attributes],  # Format attributes.
            "methods": [
                {
                    "name": method["name"],  # Include method name.
                    "params": method["params"],  # Include parameters of the method.
                    "return_type": method["return_type"],  # Include return type of the method.
                    "body": method["body"]  # Include the body of the method.
                } for method in self.methods  # Loop through each method to structure it.
            ]
        }

    def print_pseudocode(self):
        # Create a string representation of the class in pseudocode format.
        pseudocode_output = f"# Class: {self.class_name}\n"  # Start with class name.
        if self.description:
            pseudocode_output += f"# Description: {self.description}\n"  # Add description if available.
        
        # Class declaration, showing inheritance if it exists.
        pseudocode_output += f"Class {self.class_name}{' inherits ' + self.inherits if self.inherits else ''}:\n"
        
        # Document the attributes of the class.
        pseudocode_output += "    Attributes:\n"
        for attr, attr_type in self.attributes:  # Iterate through attributes.
            pseudocode_output += f"        - {attr}: {attr_type}\n"  # Format each attribute.

        # Document methods with parameters and return types.
        pseudocode_output += "    Methods:\n"
        for method in self.methods:
            pseudocode_output += f"        {method['name']}("  # Start method declaration.
            # Prepare parameter definitions.
            param_list = [f"{param['name']}: {param['type']}" for param in method['params']]
            pseudocode_output += ', '.join(param_list)  # Join parameters with commas.
            pseudocode_output += f") -> {method['return_type']}:\n"  # Specify the return type.
            for line in method['body']:
                pseudocode_output += f"            {line}\n"  # Add method body lines with indentation.

        return pseudocode_output  # Return the constructed pseudocode string.


# Defining the Car class with its properties and methods.
car_example = ClassModel(
    class_name="Car",  # Set the name of the class.
    description="Represents a car with its attributes and behaviors.",  # Provide a description for clarity.
    attributes=[("model", "str"), ("num_seats", "int"), ("weight_limit", "float")],  # Define attributes.
    methods=[
        {
            "name": "start_engine",  # Method to start the engine.
            "params": [],  # No parameters needed for this method.
            "return_type": "None",  # This method does not return anything.
            "body": ["# Start the car's engine", "print('Engine started')"]  # Method body lines.
        },
        {
            "name": "drive",  # Method to drive the car.
            "params": [{"name": "distance", "type": "float"}],  # Takes distance as a parameter.
            "return_type": "None",  # No return value.
            "body": ["# Simulate driving the car", "print(f'Driving {distance} miles')"]  # Method body.
        }
    ]
)

# Defining the Truck class with its properties and methods.
truck_example = ClassModel(
    class_name="Truck",  # Set the name of the class.
    description="Represents a truck with its attributes and behaviors.",  # Describe the class.
    attributes=[("model", "str"), ("cargo_capacity", "float"), ("weight_limit", "float")],  # Define truck attributes.
    methods=[
        {
            "name": "load_cargo",  # Method to load cargo onto the truck.
            "params": [{"name": "weight", "type": "float"}],  # Weight of the cargo as a parameter.
            "return_type": "None",  # No return value.
            "body": ["# Load the specified weight of cargo", "print(f'Loaded {weight} lbs of cargo')"]  # Body of the method.
        },
        {
            "name": "unload_cargo",  # Method to unload cargo from the truck.
            "params": [],  # No parameters needed.
            "return_type": "None",  # No return value.
            "body": ["# Unload cargo from the truck", "print('Cargo unloaded')"]  # Body of the method.
        }
    ]
)

# Defining the Driver class with its properties and methods.
driver_example = ClassModel(
    class_name="Driver",  # Set the name of the class.
    description="Represents a driver with a license and the cars they can drive.",  # Describe the class.
    attributes=[("name", "str"), ("license_number", "str")],  # Define driver attributes.
    methods=[
        {
            "name": "drive_car",  # Method to drive a car.
            "params": [{"name": "car", "type": "Car"}],  # Accepts a Car object as a parameter.
            "return_type": "None",  # No return value.
            "body": ["# Driver drives the specified car", "car.start_engine()"]  # Body of the method.
        }
    ]
)

# Defining the CarDriver association (1-N relationship).
car_driver_example_1n = ClassModel(
    class_name="CarDriver_1N",  # Set the name of the association class.
    description="Represents the relationship between drivers and cars (1 driver can drive many cars).",  # Describe the relationship.
    attributes=[
        ("driver_id", "int"),  # Unique ID for the driver.
        ("car_id", "int"),  # Unique ID for the car.
        ("license_number", "str")  # Driver's license number.
    ],
    methods=[
        {
            "name": "add_car",  # Method to add a car for a driver.
            "params": [{"name": "car", "type": "Car"}],  # Accepts a Car object as a parameter.
            "return_type": "None",  # No return value.
            "body": ["# Add a car to the driver's list", "print(f'Car {car.model} added for driver {self.driver_id}')"]  # Method body.
        },
        {
            "name": "get_cars",  # Method to retrieve the list of cars for a driver.
            "params": [],  # No parameters needed.
            "return_type": "List[Car]",  # This method returns a list of Car objects.
            "body": ["# Return a list of cars driven by the driver", "return self.cars"]  # Method body.
        }
    ]
)

# Defining the CarDriver association (N-N relationship).
car_driver_example_nn = ClassModel(
    class_name="CarDriver_NN",  # Set the name of the association class.
    description="Represents the many-to-many relationship between drivers and cars.",  # Describe the relationship.
    attributes=[
        ("driver_id", "int"),  # Unique ID for the driver.
        ("car_id", "int")  # Unique ID for the car.
    ],
    methods=[
        {
            "name": "assign_driver",  # Method to assign a driver to a car.
            "params": [{"name": "driver", "type": "Driver"}, {"name": "car", "type": "Car"}],  # Accepts Driver and Car objects.
            "return_type": "None",  # No return value.
            "body": ["# Assign a driver to a car", "print(f'Driver {driver.name} assigned to car {car.model}')"]  # Method body.
        },
        {
            "name": "remove_driver",  # Method to remove a driver's assignment from a car.
            "params": [{"name": "driver", "type": "Driver"}, {"name": "car", "type": "Car"}],  # Accepts Driver and Car objects.
            "return_type": "None",  # No return value.
            "body": ["# Remove a driver's assignment from a car", "print(f'Driver {driver.name} removed from car {car.model}')"]  # Method body.
        }
    ]
)

# Collect all class models for output.
class_models = [
    car_example,
    truck_example,
    driver_example,
    car_driver_example_1n,
    car_driver_example_nn
]

# Generate and print pseudocode for all classes.
pseudocode_outputs = [model.print_pseudocode() for model in class_models]  # Generate pseudocode for each class.

# Print the pseudocode for all classes.
for output in pseudocode_outputs:
    print(output)  # Output the pseudocode to the console.

# Convert class models to a dictionary for YAML representation.
yaml_output = [model.to_dict() for model in class_models]

# Write the output to a YAML file named 'pseudocode.yaml'.
with open('pseudocode.yaml', 'w') as yaml_file:
    yaml.dump(yaml_output, yaml_file, sort_keys=False)  # Save the YAML output, preserving order.

# Notify that the YAML output has been successfully written.
print("\Pseudocode written to '\pseudocode.yaml'.")
