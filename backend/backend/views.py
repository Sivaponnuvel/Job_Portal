from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, JobSerializer, ApplicationSerializer
from .models import Job

@api_view(['GET'])
def hello_api(request):
    return Response({"message":"Hello from Django API"})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Register Successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def basic_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username, password=password)
        return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def apply_job(request):
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Application Submitted"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)