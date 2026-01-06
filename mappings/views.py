from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingListSerializer
from patients.models import Patient


class PatientDoctorMappingListCreateView(APIView):
    """API view for listing and creating patient-doctor mappings."""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """Get all patient-doctor mappings for authenticated user's patients."""
        mappings = PatientDoctorMapping.objects.filter(patient__user=request.user)
        serializer = PatientDoctorMappingListSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new patient-doctor mapping."""
        serializer = PatientDoctorMappingSerializer(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Doctor assigned to patient successfully',
                'mapping': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDoctorsByPatientView(APIView):
    """API view for getting all doctors assigned to a specific patient."""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, patient_id):
        """Get all doctors assigned to a specific patient."""
        # Verify patient belongs to authenticated user
        patient = get_object_or_404(Patient, id=patient_id, user=request.user)
        
        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        serializer = PatientDoctorMappingListSerializer(mappings, many=True)
        
        return Response({
            'patient_id': patient_id,
            'patient_name': patient.name,
            'doctors': serializer.data
        }, status=status.HTTP_200_OK)


class PatientDoctorMappingDetailView(APIView):
    """API view for retrieving and deleting a specific patient-doctor mapping."""
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk, user):
        """Get mapping object by pk and verify it belongs to authenticated user."""
        return get_object_or_404(
            PatientDoctorMapping,
            pk=pk,
            patient__user=user
        )
    
    def get(self, request, pk):
        """Get details of a specific mapping."""
        mapping = self.get_object(pk, request.user)
        serializer = PatientDoctorMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        """Remove a doctor from a patient."""
        mapping = self.get_object(pk, request.user)
        mapping.delete()
        return Response({
            'message': 'Doctor removed from patient successfully'
        }, status=status.HTTP_200_OK)
