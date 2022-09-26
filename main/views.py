from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

class Person:
    def __init__(self, first_name=None, last_name=None, middle_name=None, description="Watashi ha person desu", email=None, birthday=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.description = description
        self.email = email
        self.birthday = birthday

    @property
    def full_name(self):
        return f"{self.first_name} {'' if self.middle_name is None else self.middle_name[0]} {self.last_name}"

    @property
    def age(self):
        if self.birthday is None:
            return None

        born = self.birthday
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return self.full_name

PERSON = {
    # president
    1: Person("Pres, Maria", "Dela Cruz"),
    # vice president
    2: Person("Vice Pres, Juan", "Dela Cruz"),

    # nth year governor
    3: Person("4th year Gov, Maria", "Dela Cruz"),
    4: Person("3rd year Gov, Maria", "Dela Cruz"),
    5: Person("2rd year Gov, Maria", "Dela Cruz"),

    # grade 12 governor
    7: Person("12th Grade Gov, Maria","Dela Cruz"),
}

print(PERSON[1])

SGA_MEMBERS = [
    {
        "batch": "2022-2023" ,
        "officers": {
            "President": PERSON[1],
            "Vice President": PERSON[2],
            "4th year Governor": PERSON[3],
            "3rd year Governor": PERSON[4],
            "2nd year Governor": PERSON[5],
            "Grade 12 Governor": PERSON[7],
        }
    }, 
]

ABOUT_US = """We are the student government association.
Here to bring organization to our school!"""

CONTACTS = {
    "email": "???",
    "phone": "???",
    "at school": "???",
}

SOCIAL = {
    "discord": "???",
    "facebook": "???",
}


def index(request):
    """Recent news, new annoucements other stuff?"""
    return render(request, "main/index.html")
    
def about(request):
    """What the sga is all about."""
    context = {"ABOUT_US": ABOUT_US}
    return render(request, "main/about.html", context=context)

# change to generic view!
def contact(request):
    """Contact and social links of SGA"""
    context = {"Contact": CONTACTS, "Social": SOCIAL}
    return render(request, "main/contact.html")

def sga_officials(request):
    """Lists of sga officers"""
    context = {"SGA":SGA_MEMBERS}
    return render(request, "main/sga_officials.html", context = context)
