import sys
sys.path.append('..')
from utils.tax_calculator import (
    validate_name, validate_emp_id, validate_basic_salary,
    validate_special_allowances, validate_bonus_percentage,
    get_valid_input, calculate_gross_salary, calculate_annual_gross_salary,
    calculate_taxable_income, calculate_tax
)

def main():
    print("=== Tax and Rebate Calculation ===\n")
    
    name = get_valid_input("Enter Name: ", validate_name)
    emp_id = get_valid_input("Enter EmpID: ", validate_emp_id)
    basic_salary = get_valid_input("Enter Basic Monthly Salary: ", validate_basic_salary)
    special_allowances = get_valid_input("Enter Special Allowances (Monthly): ", validate_special_allowances)
    bonus_percentage = get_valid_input("Enter Bonus Percentage (Annual): ", validate_bonus_percentage)
    
    gross_monthly = calculate_gross_salary(basic_salary, special_allowances)
    annual_gross = calculate_annual_gross_salary(gross_monthly, bonus_percentage)
    taxable_income = calculate_taxable_income(annual_gross)
    total_tax, base_tax, cess = calculate_tax(taxable_income)
    
    print("\n=== Tax Breakdown ===")
    print(f"Taxable Income: ₹{taxable_income:,.2f}")
    if taxable_income <= 7_00_000:
        print("Section 87A Rebate Applied: 100% (Tax = ₹0)")
        print(f"Base Tax: ₹0.00")
        print(f"Health & Education Cess (4%): ₹0.00")
    else:
        print(f"Base Tax: ₹{base_tax:,.2f}")
        print(f"Health & Education Cess (4%): ₹{cess:,.2f}")
    print(f"Total Tax Payable: ₹{total_tax:,.2f}")

if __name__ == "__main__":
    main()
