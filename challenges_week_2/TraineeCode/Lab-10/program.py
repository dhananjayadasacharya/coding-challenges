from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        employees = [None] * 4

        print("Enter employee information")
        for i in range(len(employees)):
            print("Employee No : " + str(i + 1))

            emp_id = input("Id : ").strip()
            name = input("Name : ").strip()
            basic = float(input("Basic : ").strip())
            hra = float(input("HRA : ").strip())
            allowance_percentage = float(input("Percentage of Allowance : ").strip())

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            role = int(input().strip())

            employees[i] = Employee(emp_id, name, basic, hra, allowance_percentage, role)

        report_date = input("Enter the date of the report (dd/mm/yyyy) : ").strip()
        report = EmployeeReport()
        report.report_date = report_date
        report.display_employees(employees)

if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
