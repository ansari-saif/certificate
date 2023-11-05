import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .utils import generate_certificate_pdf, generate_unique_code
from .forms import EmailForm
from django.shortcuts import get_object_or_404
from .models import UserProfile

class ValidateEmailView(View):
    template_name = 'validate_email.html'

    def get(self, request):
        form = EmailForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EmailForm(request.POST)
        print('here')
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                # Check if the email address exists in the database
                user_profile = UserProfile.objects.get(email=email)
                # Generate and update the unique_code here
                if not user_profile.unique_code:
                    user_profile.unique_code = generate_unique_code()  # Implement your code to generate a unique code
                    user_profile.save()
                return redirect(f'certificate/{user_profile.unique_code}/')  # Replace 'success_page' with your actual URL name
            except UserProfile.DoesNotExist:
                form.add_error('email', 'Email address not found in the database.')
        return render(request, self.template_name, {'form': form})
    
class CertificateView(View):
    template_name = 'certificate.html'
    def get(self, request, unique_code):

        user_profile = get_object_or_404(UserProfile, unique_code=unique_code)
        return render(request, self.template_name, {'user_profile': user_profile})

        pdf_response = generate_certificate_pdf(user_profile)

        certificate_file_path = f'{unique_code}_certificate.pdf'

        with open(certificate_file_path, 'wb') as certificate_file:
            certificate_file.write(pdf_response.read())

        with open(certificate_file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{unique_code}_certificate.pdf"'

        return response

class DownloadCertificateView(View):
    def get(self, request, unique_code):
        user_profile = get_object_or_404(UserProfile, unique_code=unique_code)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{unique_code}_certificate.pdf"'

        # Create the PDF certificate and write it to the response
        generate_certificate_pdf(response, user_profile)

        return response



