class SalaryCalculator:
    """
    Method to calculate the salary of an employee
    """
    @staticmethod
    def get_salary(emp):
        return emp.basic + emp.hra + SalaryCalculator.get_allowance(emp)

    """
    Method to get the allowance for an employee based on the percentage
    """
    @staticmethod
    def get_allowance(emp):
        return emp.basic * emp.allowance_percentage / 100.0
