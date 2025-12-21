from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        employees = []

        print("Enter the date of the report (dd/mm/yyyy) : ")
        dt_report = input().strip()

        print("Enter number of employees : ")
        num_employees = int(input().strip())

        print("Enter employee information")
        for i in range(num_employees):
            print("Employee No : " + str(i + 1))

            emp = Employee()
            emp.emp_id = input("Id : ").strip()
            emp.name = input("Name : ").strip()
            emp.basic = float(input("Basic : ").strip())
            emp.hra = float(input("HRA : ").strip())
            emp.allowance_percentage = float(input("Percentage of Allowance : ").strip())

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER.value))
            print(str(Roles.TEST_ENGINEER.value) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER.value))
            print(str(Roles.SR_DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER.value))
            print(str(Roles.DESIGNER.value) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER.value))
            role = int(input().strip())

            emp.role = role
            employees.append(emp)

        report = EmployeeReport(dt_report)
        report.display_employees(employees)

if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
