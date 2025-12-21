# patient class
class patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name


# ward class
class ward:
    def __init__(self, ward_id, ward_name):
        self.ward_id = ward_id
        self.ward_name = ward_name
        self.patients = []

    def admit_patient(self, patient):
        self.patients.append(patient)


# hospital class
class hospital:
    def __init__(self, hospital_id, name):
        self.hospital_id = hospital_id
        self.name = name
        self.wards = []

    def add_ward(self, ward):
        self.wards.append(ward)


# surgeon base class
class surgeon:
    def __init__(self, surgeon_id, name):
        self.surgeon_id = surgeon_id
        self.name = name
        self.hospitals = []
        self.operated_patients = []

    def add_hospital(self, hospital):
        self.hospitals.append(hospital)

    def operate_patient(self, patient):
        self.operated_patients.append(patient)

    # 1. total number of patients being operated
    def total_operated_patients(self):
        return len(self.operated_patients)

    # 2. list all patients operated by this surgeon
    def list_operated_patients(self):
        return self.operated_patients


# senior surgeon
class senior_surgeon(surgeon):
    def __init__(self, surgeon_id, name, specialization, experience_years):
        super().__init__(surgeon_id, name)
        self.specialization = specialization
        self.experience_years = experience_years


# non-senior surgeon
class non_senior_surgeon(surgeon):
    def __init__(self, surgeon_id, name, supervision_required=True):
        super().__init__(surgeon_id, name)
        self.supervision_required = supervision_required
