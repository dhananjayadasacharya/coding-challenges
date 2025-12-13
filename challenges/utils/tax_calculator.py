def validate_name(name):
    if not name or not isinstance(name, str):
        return False, "Name cannot be empty"
    if not name.replace(" ", "").isalpha():
        return False, "Name must contain only alphabets"
    if len(name) > 50:
        return False, "Name cannot exceed 50 characters"
    return True, ""

def validate_emp_id(emp_id):
    if not emp_id or not isinstance(emp_id, str):
        return False, "EmpID cannot be empty"
    if not emp_id.isalnum():
        return False, "EmpID must be alphanumeric"
    if len(emp_id) < 5 or len(emp_id) > 10:
        return False, "EmpID must be 5-10 characters"
    return True, ""

def validate_basic_salary(salary):
    try:
        salary = float(salary)
        if salary <= 0:
            return False, "Basic Salary must be positive"
        if salary > 1_00_00_000:
            return False, "Basic Salary cannot exceed ₹1,00,00,000"
        return True, ""
    except ValueError:
        return False, "Basic Salary must be a valid number"

def validate_special_allowances(allowances):
    try:
        allowances = float(allowances)
        if allowances < 0:
            return False, "Special Allowances cannot be negative"
        if allowances > 1_00_00_000:
            return False, "Special Allowances cannot exceed ₹1,00,00,000"
        return True, ""
    except ValueError:
        return False, "Special Allowances must be a valid number"

def validate_bonus_percentage(bonus):
    try:
        bonus = float(bonus)
        if bonus < 0 or bonus > 100:
            return False, "Bonus Percentage must be between 0 and 100"
        return True, ""
    except ValueError:
        return False, "Bonus Percentage must be a valid number"

def get_valid_input(prompt, validator):
    while True:
        value = input(prompt)
        valid, error = validator(value)
        if valid:
            return value if isinstance(value, str) else float(value)
        print(f"Error: {error}")

def calculate_gross_salary(basic_salary, special_allowances):
    gross_monthly = basic_salary + special_allowances
    return gross_monthly

def calculate_annual_gross_salary(gross_monthly, bonus_percentage):
    bonus_amount = (gross_monthly * 12) * (bonus_percentage / 100)
    annual_gross = (gross_monthly * 12) + bonus_amount
    return annual_gross

def calculate_taxable_income(annual_gross):
    standard_deduction = 50_000
    taxable_income = annual_gross - standard_deduction
    return max(0, taxable_income)

def calculate_tax(taxable_income):
    if taxable_income <= 0:
        return 0
    
    tax = 0
    slabs = [
        (3_00_000, 0),
        (6_00_000, 0.05),
        (9_00_000, 0.10),
        (12_00_000, 0.15),
        (15_00_000, 0.20),
        (float('inf'), 0.30)
    ]
    
    previous_limit = 0
    for limit, rate in slabs:
        if taxable_income <= previous_limit:
            break
        taxable_in_slab = min(taxable_income, limit) - previous_limit
        tax += taxable_in_slab * rate
        previous_limit = limit
    
    if taxable_income <= 7_00_000:
        tax = 0
    
    cess = tax * 0.04
    total_tax = tax + cess
    
    return total_tax, tax, cess

def calculate_net_salary(annual_gross, total_tax):
    net_salary = annual_gross - total_tax
    return net_salary
