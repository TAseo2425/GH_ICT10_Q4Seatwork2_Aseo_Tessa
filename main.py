from pyscript import display, document

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        display(f'Hi! My name is {self.name} from {self.section}. My favorite subject is {self.subject}.', target='output')

def classlist(e):
    document.getElementById('output').innerHTML = ""

    # create objects
    cm1 = Classmate("Jillian", "Sapphire", "Math")
    cm2 = Classmate("Sofia", "Sapphire", "Social Studies")
    cm3 = Classmate("Ishan", "Sapphire", "Social Studies")
    cm4 = Classmate("Francesca", "Sapphire", "Science")
    cm5 = Classmate("Jennifer", "Sapphire", "Math")

    classmates = [cm1, cm2, cm3, cm4, cm5]

    for c in classmates:
        c.introduce()

def add_classmate(e):
    name = document.getElementById('name').value
    section = document.getElementById('section').value
    subject = document.getElementById('subject').value

    new_cm = Classmate(name, section, subject)
    display(f'Hi! My name is {name}, from {section}. My favorite subject is {subject}.', target='output')