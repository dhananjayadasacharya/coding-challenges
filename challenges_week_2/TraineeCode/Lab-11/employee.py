from salary_calculator import SalaryCalculator
from role_builder import RoleBuilder

class Employee:
    """
    Properties of the class
    """
    def __init__(self, emp_id="", name="", basic=0.0, hra=0.0, allowance_percentage=0.0, role=0):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.hra = hra
        self.allowance_percentage = allowance_percentage
        self.role = role

    """
    Method to get allowance by delegating to SalaryCalculator
    """
    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)

    """
    Method to get salary by delegating to SalaryCalculator
    """
    def get_salary(self):
        return SalaryCalculator.get_salary(self)

    """
    Method to get role description by delegating to RoleBuilder
    """
    def get_role_description(self):
        return RoleBuilder.get_role_description(self.role)
