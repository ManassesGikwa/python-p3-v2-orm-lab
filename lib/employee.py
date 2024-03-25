from lib import CURSOR, CONN
from .review import Review

class Employee:
    def __init__(self, name, department):
        self.id = None
        self.name = name
        self.department = department

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, department={self.department})"

    def save(self):
        pass  # Implement save method

    @classmethod
    def create(cls, name, department):
        pass  # Implement create class method

    @classmethod
    def instance_from_db(cls, row):
        pass  # Implement instance_from_db class method

    @classmethod
    def find_by_id(cls, employee_id):
        pass  # Implement find_by_id class method

    def update(self):
        pass  # Implement update instance method

    def delete(self):
        pass  # Implement delete instance method

    @classmethod
    def get_all(cls):
        pass  # Implement get_all class method

    def reviews(self):
        pass  # Implement reviews method
