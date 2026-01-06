from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """Serializer for PatientDoctorMapping model."""
    
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'patient_name', 'doctor_name',
            'patient_details', 'doctor_details', 'assigned_date', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'assigned_date', 'created_at', 'updated_at']
    
    def validate(self, attrs):
        """Validate that the patient belongs to the requesting user."""
        request = self.context.get('request')
        patient = attrs.get('patient')
        
        if patient and request and request.user:
            if patient.user != request.user:
                raise serializers.ValidationError(
                    {"patient": "You can only assign doctors to your own patients."}
                )
        
        return attrs


class PatientDoctorMappingListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing mappings."""
    
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    doctor_specialization = serializers.CharField(source='doctor.specialization', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'patient_name', 'doctor_name',
            'doctor_specialization', 'assigned_date', 'notes'
        ]
