import sys
sys.path.append('..')
from utils.tax_calculator import (
    validate_name, validate_emp_id, validate_basic_salary,
    validate_special_allowances, validate_bonus_percentage,
    get_valid_input, calculate_gross_salary, calculate_annual_gross_salary,
    calculate_taxable_income
)

def main():
    print("=== Taxable Income Calculation ===\n")
    
    name = get_valid_input("Enter Name: ", validate_name)
    emp_id = get_valid_input("Enter EmpID: ", validate_emp_id)
    basic_salary = get_valid_input("Enter Basic Monthly Salary: ", validate_basic_salary)
    special_allowances = get_valid_input("Enter Special Allowances (Monthly): ", validate_special_allowances)
    bonus_percentage = get_valid_input("Enter Bonus Percentage (Annual): ", validate_bonus_percentage)
    
    gross_monthly = calculate_gross_salary(basic_salary, special_allowances)
    annual_gross = calculate_annual_gross_salary(gross_monthly, bonus_percentage)
    taxable_income = calculate_taxable_income(annual_gross)
    
    print("\n=== Results ===")
    print(f"Annual Gross Salary: ₹{annual_gross:,.2f}")
    print(f"Standard Deduction: ₹50,000.00")
    print(f"Taxable Income: ₹{taxable_income:,.2f}")

if __name__ == "__main__":
    main()
