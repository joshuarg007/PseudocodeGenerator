class ClassModel:
    def __init__(self, class_name, attributes, methods):
        self.class_name = class_name
        self.attributes = attributes
        self.methods = methods

    def print_pseudocode(self):
        print(f"class {self.class_name}:")
        print("    Attributes:")
        for attr in self.attributes:
            print(f"        - {attr}")
        print("    Methods:")
        for method in self.methods:
            print(f"        - {method}()")


# Example usage
class_name = "Student"
attributes = ["name", "age", "grade", "student_id"]
methods = ["enroll", "take_exam", "get_grade"]

# Create the model
student_class = ClassModel(class_name, attributes, methods)

# Print the pseudocode
student_class.print_pseudocode()
