class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("name", self.name)
        print("age", self.age)

class Patient(Person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.__disease = disease

    def display_info(self):
        super().display_info()
        print("patient_id", self.patient_id)
        print("Disease", self.__disease)

    def get_disease(self):
        return self.__disease
    
    def set_disease(self, new_disease):
        self.__disease = new_disease



class Hospital:
    def __init__(self):
        self.patient = []

    def add_patient(self, Patient):
        self.patient.append(Patient)
        print("the patient is added to the hospital")

    def display_patient(self):
        print("patient")
        for patient in self.patient:
            patient.display_info()
        print("patient displayed successfully")

    def search_patient(self, patient_id):
        for patient in self.patient:
            if patient.patient_id == patient_id:
                patient.display_info()
                print("patient displayed successfully")
                return
        print("patient not found")

    def remove_patient(self, patient_id):
            for patient in self.patient:
                if patient.patient_id == patient_id:
                    self.patient.remove(patient)
                    print("patient remove successfully")
                    return
            print("patient not found")
            


patient1 = Patient("Ali", 34, "P101", "cancer")
patient2= Patient("Ahmad", 37, "P102", "fiver")

Hospital = Hospital()

Hospital.add_patient(patient2)
Hospital.add_patient(patient1)
Hospital.display_patient()
Hospital.search_patient("P101")
Hospital.remove_patient("P102")
new_disease = input("enter new disease")
patient1.set_disease(new_disease)        

        

    