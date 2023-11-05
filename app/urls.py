from django.urls import path
from . import views

urlpatterns = [
    path('', views.ValidateEmailView.as_view(), name='validate_email'),
    path('certificate/<str:unique_code>/', views.CertificateView.as_view(), name='certificate_view'),
    path('certificate/<str:unique_code>/download/', views.DownloadCertificateView.as_view(), name='download_certificate'),

]
