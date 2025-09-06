students = [ 
    {"name": "Harry", "house": "Griffindor", "Patronus": "Stag"},
    {"name": "Hermione", "house": "Griffindor", "Patronus": "Otter"},
    {"name": "Ron", "house": "Griffindor", "Patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin",  "Patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["Patronus"], sep=", ")

