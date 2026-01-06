from django.urls import path
from .views import (
    PatientDoctorMappingListCreateView,
    PatientDoctorsByPatientView,
    PatientDoctorMappingDetailView
)

urlpatterns = [
    path('', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:patient_id>/', PatientDoctorsByPatientView.as_view(), name='mapping-by-patient'),
    path('detail/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
]
