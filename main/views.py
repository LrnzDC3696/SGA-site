from django.shortcuts import render
from django.http import HttpResponse


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

def contact(request):
    """Contact and social links of SGA"""
    context = {"Contact": CONTACTS, "Social": SOCIAL}
    return render(request, "main/contact.html")

def sga_officials(request):
    """Lists of sga officers"""
    return render(request, "main/sga_officials.html")

def batch_governors(request):
    """List of governors"""
    return render(request, "main/batch_governors.html")
