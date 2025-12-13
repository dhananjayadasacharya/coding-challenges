import sys
sys.path.append('..')
from utils.tax_calculator import (
    validate_name, validate_emp_id, validate_basic_salary,
    validate_special_allowances, validate_bonus_percentage,
    get_valid_input, calculate_gross_salary, calculate_annual_gross_salary
)

def main():
    print("=== Employee Salary Calculation ===\n")
    
    name = get_valid_input("Enter Name: ", validate_name)
    emp_id = get_valid_input("Enter EmpID: ", validate_emp_id)
    basic_salary = get_valid_input("Enter Basic Monthly Salary: ", validate_basic_salary)
    special_allowances = get_valid_input("Enter Special Allowances (Monthly): ", validate_special_allowances)
    bonus_percentage = get_valid_input("Enter Bonus Percentage (Annual): ", validate_bonus_percentage)
    
    gross_monthly = calculate_gross_salary(basic_salary, special_allowances)
    annual_gross = calculate_annual_gross_salary(gross_monthly, bonus_percentage)
    
    print("\n=== Results ===")
    print(f"Name: {name}")
    print(f"EmpID: {emp_id}")
    print(f"Gross Monthly Salary: ₹{gross_monthly:,.2f}")
    print(f"Annual Gross Salary: ₹{annual_gross:,.2f}")

if __name__ == "__main__":
    main()
