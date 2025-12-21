"""
Class to represent employee information
"""
class Employee:
    _employee_id = None
    _employee_name = None
    _employee_gender = None

    def __init__(self):
        self._employee_id = None
        self._employee_name = None
        self._employee_gender = None

    @property
    def employee_id(self):
        return self._employee_id
    
    @property
    def employee_name(self):
        return self._employee_name
    
    @property
    def employee_gender(self):
        return self._employee_gender
    
    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = "E" + str(value).strip()

    @employee_name.setter
    def employee_name(self, value):
        self._employee_name = str(value).strip().capitalize()

    @employee_gender.setter
    def employee_gender(self, value):
        v = str(value).strip()
        self._employee_gender = "Male" if v and v[0].lower() == "m" else "Female"