from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """
    Welcome endpoint - provides information about available API endpoints.
    """
    return Response({
        'message': 'Welcome to Healthcare Backend API',
        'version': '1.0.0',
        'status': 'Running',
        'endpoints': {
            'authentication': {
                'register': '/api/auth/register/ [POST]',
                'login': '/api/auth/login/ [POST]',
            },
            'patients': {
                'list_create': '/api/patients/ [GET, POST]',
                'detail': '/api/patients/<id>/ [GET, PUT, DELETE]',
            },
            'doctors': {
                'list_create': '/api/doctors/ [GET, POST]',
                'detail': '/api/doctors/<id>/ [GET, PUT, DELETE]',
            },
            'mappings': {
                'list_create': '/api/mappings/ [GET, POST]',
                'by_patient': '/api/mappings/<patient_id>/ [GET]',
                'detail': '/api/mappings/detail/<id>/ [GET, DELETE]',
            },
            'admin': '/admin/',
        },
        'documentation': 'See README.md and API_DOCUMENTATION.md for detailed API documentation',
        'test_credentials': {
            'admin': 'admin@healthcare.com / admin@123',
            'user1': 'rajesh.kumar@email.com / Test@123',
            'user2': 'priya.sharma@email.com / Test@123',
            'user3': 'amit.patel@email.com / Test@123',
        },
        'note': 'All endpoints except /api/auth/register/ and /api/auth/login/ require JWT authentication',
    }, status=status.HTTP_200_OK)
