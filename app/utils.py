
import random
import string

from django.http import HttpResponse
from .models import UserProfile
from django.template.loader import get_template
import pdfkit


def generate_unique_code():
    while True:
        generated_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        # Check if the generated_code already exists in the database
        if not UserProfile.objects.filter(unique_code=generated_code).exists():
            return generated_code



def generate_certificate_pdf(response, user_profile):
    template = get_template('certificate_template.html')
    context = {
        'name': 'John Doe',
        'unique_code': 'YF12C',
        'course': 'Course Name',
        'completion_date': '2023-11-05',
    }
    html = template.render({"user_profile":user_profile})

    pdf = pdfkit.from_string(html, False)
    response.write(pdf)
    return response
