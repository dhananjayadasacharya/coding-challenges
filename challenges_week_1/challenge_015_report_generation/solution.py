import sys
sys.path.append('..')
from utils.tax_calculator import (
    validate_name, validate_emp_id, validate_basic_salary,
    validate_special_allowances, validate_bonus_percentage,
    get_valid_input, calculate_gross_salary, calculate_annual_gross_salary,
    calculate_taxable_income, calculate_tax, calculate_net_salary
)

def generate_report(name, emp_id, gross_monthly, annual_gross, taxable_income, total_tax, net_salary):
    print("\n" + "="*50)
    print("EMPLOYEE TAX REPORT")
    print("="*50)
    print(f"{'Field':<30} {'Details':>18}")
    print("-"*50)
    print(f"{'Name':<30} {name:>18}")
    print(f"{'EmpID':<30} {emp_id:>18}")
    print(f"{'Gross Monthly Salary':<30} {'₹' + f'{gross_monthly:,.2f}':>17}")
    print(f"{'Annual Gross Salary':<30} {'₹' + f'{annual_gross:,.2f}':>17}")
    print(f"{'Taxable Income':<30} {'₹' + f'{taxable_income:,.2f}':>17}")
    print(f"{'Tax Payable':<30} {'₹' + f'{total_tax:,.2f}':>17}")
    print(f"{'Annual Net Salary':<30} {'₹' + f'{net_salary:,.2f}':>17}")
    print("="*50)

def main():
    print("=== Employee Tax Report Generation ===\n")
    
    name = get_valid_input("Enter Name: ", validate_name)
    emp_id = get_valid_input("Enter EmpID: ", validate_emp_id)
    basic_salary = get_valid_input("Enter Basic Monthly Salary: ", validate_basic_salary)
    special_allowances = get_valid_input("Enter Special Allowances (Monthly): ", validate_special_allowances)
    bonus_percentage = get_valid_input("Enter Bonus Percentage (Annual): ", validate_bonus_percentage)
    
    gross_monthly = calculate_gross_salary(basic_salary, special_allowances)
    annual_gross = calculate_annual_gross_salary(gross_monthly, bonus_percentage)
    taxable_income = calculate_taxable_income(annual_gross)
    total_tax, _, _ = calculate_tax(taxable_income)
    net_salary = calculate_net_salary(annual_gross, total_tax)
    
    generate_report(name, emp_id, gross_monthly, annual_gross, taxable_income, total_tax, net_salary)

if __name__ == "__main__":
    main()
