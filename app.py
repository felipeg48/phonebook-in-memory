class Person:
    def __init__(self, person_name, person_phone, person_email):
        self.name = person_name
        self.phone = person_phone
        self.email = person_email

    def __str__(self):
        return f"Person\n- Name: {self.name}\n- Phone: {self.phone}\n- Email: {self.email}"


people = []


def add_person():
    name = input("Person's name: ")
    phone = input("Person's phone: ")
    email = input("Person's email: ")

    p1 = Person(name, phone, email)

    print(p1)
    people.append(p1)


def print_people():
    for p in people:
        print(p)


add_person()
add_person()
add_person()
print_people()
