import sys
sys.path.append('..')
from utils.tax_calculator import (
    validate_name, validate_emp_id, validate_basic_salary,
    validate_special_allowances, validate_bonus_percentage,
    get_valid_input, calculate_gross_salary, calculate_annual_gross_salary,
    calculate_taxable_income, calculate_tax, calculate_net_salary
)

def validate_all_inputs():
    print("=== Employee Input Validation ===\n")
    
    try:
        name = get_valid_input("Enter Name: ", validate_name)
        emp_id = get_valid_input("Enter EmpID: ", validate_emp_id)
        basic_salary = get_valid_input("Enter Basic Monthly Salary: ", validate_basic_salary)
        special_allowances = get_valid_input("Enter Special Allowances (Monthly): ", validate_special_allowances)
        bonus_percentage = get_valid_input("Enter Bonus Percentage (Annual): ", validate_bonus_percentage)
        
        gross_monthly = calculate_gross_salary(basic_salary, special_allowances)
        if gross_monthly <= 0:
            print("Error: Gross Monthly Salary must be greater than zero")
            return
        
        annual_gross = calculate_annual_gross_salary(gross_monthly, bonus_percentage)
        if annual_gross > 10_00_00_000:
            print("Error: Annual Gross Salary exceeds realistic values (max ₹10,00,00,000)")
            return
        
        print("\n=== Validation Successful ===")
        print(f"Name: {name} ✓")
        print(f"EmpID: {emp_id} ✓")
        print(f"Basic Salary: ₹{basic_salary:,.2f} ✓")
        print(f"Special Allowances: ₹{special_allowances:,.2f} ✓")
        print(f"Bonus Percentage: {bonus_percentage}% ✓")
        print(f"Gross Monthly Salary: ₹{gross_monthly:,.2f} ✓")
        print(f"Annual Gross Salary: ₹{annual_gross:,.2f} ✓")
        
    except Exception as e:
        print(f"Validation Error: {str(e)}")

def main():
    validate_all_inputs()

if __name__ == "__main__":
    main()
