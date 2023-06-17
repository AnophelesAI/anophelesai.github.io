from experta import *


DB = {}
Name_Checked = {}

class Patient(Fact):
    """Info about the patient."""
    pass
class HaveMalaria(KnowledgeEngine):
    @Rule(Patient(name=MATCH.name), OR(
            Patient(muscle_or_joint_pain = True),
            Patient(shivering_and_chills = True),
            Patient(body_ache = True),
            Patient(headache = True),
            Patient(no_appetite = True),
            Patient(nausea = True),
            Patient(weakness = True),
            Patient(fatigue = True),
            Patient(discomfort = True),
    ), salience=3 )
    def major_symptoms(self, name ): # 4th
        if Name_Checked[name] != True:
            Name_Checked[name] = True
            DB[name] = "There is a high likelihood that you have malaria. Please visit a healthcare professional for further testing and treatment."
        

    @Rule(Patient(name=MATCH.name),
        OR(
        AND(Patient(cough = True),Patient(vomiting = True)),
        AND(Patient(cough = True),Patient(sore_throat = True)),
        AND(Patient(cough = True),Patient(sneezing = True)),
        AND(Patient(cough = True),Patient(mouth_sore = True)),
        Patient(vomiting = True),
        Patient(sore_throat = True),
        Patient(sneezing = True),
        Patient(mouth_sore = True),           
    ), salience=2)
    def medium_symptoms(self,name ): # 3rd
        if Name_Checked[name] != True:
            Name_Checked[name] = True
            DB[name] = "There is a moderate likelihood that you have malaria. Please monitor your symptoms and consider visiting a healthcare professional if your symptoms worsen."

    @Rule(Patient(name=MATCH.name),
        OR(
        Patient(cough = True),
        Patient(rash = True),
        Patient(convulsion = True),
        Patient(rapid_breathing = True),
        Patient(rapid_heart_rate = True),
        Patient(chest_and_abdominal_pain = True),
        Patient(stooling = True),
        Patient(earache = True),
        Patient(facial_pain = True),
        Patient(stiff_neck = True),
        Patient(difficulty_breathing = True),
        Patient(jaundice = True)            
    ),salience=1)
    def no_likely_symptoms(self, name): # 2nd
        if Name_Checked[name] != True:
            Name_Checked[name] = True
            DB[name] = "The symptoms you have are unlikely to be related to malaria. However, if your symptoms persist or worsen, please consult a healthcare professional."

    @Rule(Patient(name=MATCH.name),Patient(none = True), salience=4)
    def no_symptoms(self, name): # 1st
        DB[name] = "There is a low likelihood that you have malaria. However, you need to visit the hospital for a check up."
