from hospital import (hospital, ward, patient,senior_surgeon)
# create hospital and wards
h1 = hospital(1, "city_hospital")

w1 = ward(1, "general_ward")
w2 = ward(2, "icu")

h1.add_ward(w1)
h1.add_ward(w2)

# create patients
p1 = patient(1, "rahul")
p2 = patient(2, "anita")
p3 = patient(3, "suresh")

# admit patients
w1.admit_patient(p1)
w1.admit_patient(p2)
w2.admit_patient(p3)

# create surgeon
s1 = senior_surgeon(1, "dr_sharma", "cardiology", 15)
s1.add_hospital(h1)

# operate patients
s1.operate_patient(p1)
s1.operate_patient(p3)

# outputs
print("total patients operated:", s1.total_operated_patients())

print("\npatients operated by surgeon:")
for p in s1.list_operated_patients():
    print(p.name)

print("\npatients admitted in general ward:")
for p in w1.patients:
    print(p.name)
