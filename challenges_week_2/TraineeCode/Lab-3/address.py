class Address:
    _Address_1 = None
    _Address_2 = None
    _city = None
    _pincode = None

    def __init__(self):
        # Ensure instance-level values; no new attributes introduced
        self._Address_1 = None
        self._Address_2 = None
        self._city = None
        self._pincode = None

    @property
    def address_1(self):
        return self._Address_1

    @address_1.setter
    def address_1(self, value):
        self._Address_1 = str(value).strip().title() if value is not None else None

    @property
    def address_2(self):
        return self._Address_2

    @address_2.setter
    def address_2(self, value):
        self._Address_2 = str(value).strip().title() if value is not None else None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = str(value).strip().title() if value is not None else None

    @property
    def pincode(self):
        return self._pincode

    @pincode.setter
    def pincode(self, value):
        self._pincode = str(value).strip() if value is not None else None
