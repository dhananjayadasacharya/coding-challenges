from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        addr = Address()
        # Set employee details
        emp.employee_id = "001"
        emp.employee_name = "Rajesh"
        emp.employee_gender = "M"

        # Set address details
        addr.address_1 = "No. 12, MG Road"
        addr.address_2 = "Sector 5"
        addr.city = "Bengaluru"
        addr.pincode = "560001"

        # Attach address to employee (no changes to Employee class needed)
        emp.address = addr

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        print("Employee Id : ",emp.employee_id)
        print("Employee Name : ",emp.employee_name)
        print("Employee Gender : ",emp.employee_gender)

        print("Employee Address : --------------")
        addr = getattr(emp, 'address', None)
        print("Address 1 : ", addr.address_1 if addr else "")
        print("Address 2 : ", addr.address_2 if addr else "")
        print("City : ", addr.city if addr else "")
        print("PinCode : ", addr.pincode if addr else "")
        print("----------------------------------")
        


if __name__ == "__main__":
    Program.main([])
