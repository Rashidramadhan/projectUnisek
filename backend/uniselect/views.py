from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from . import serializers, models


# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':
        response = f'Hey {request.user}, You are accessing a GET response'
        return Response({'response': response}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('hello there')
        response = f'Hey {request.user}, your text is {text}'
        return Response({'response': response}, status=status.HTTP_200_OK)
    
    return Response({}, status=status.HTTP_400_BAD_REQUEST)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.StudentModel.objects.all()
    serializer_class = serializers.StudentsSerializer
    permission_classes = [AllowAny]

class MentorViewSet(viewsets.ModelViewSet):
    queryset = models.MentorModel.objects.all()
    serializer_class = serializers.MentorSerializer
    permission_classes = [AllowAny]

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = models.UniversityModel.objects.all()
    serializer_class = serializers.UniversitySerializer
    permission_classes = [AllowAny]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.CoursesModel.objects.all()
    serializer_class = serializers.CoursesSerializer
    permission_classes = [AllowAny]