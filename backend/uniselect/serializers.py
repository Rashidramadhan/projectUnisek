from rest_framework import serializers
from . import models

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = ['student_username', 'full_names', 'gender', 'birth_date', 'home_address', 'email', 'phone',
                  'college_date', 'college_considering', 'majoring_courses', 'registration_date']
        
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MentorModel
        fields = ['mentor_username', 'full_names', 'gender', 'address', 'email', 'phone',
                  'area_specialisation']
        
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UniversityModel
        fields = ['university_id', 'university_name', 'courses_offered', 'address', 'email', 'phone',]
        
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoursesModel
        fields = ['course_id','university_name', 'course_name', 'duration', 'fee']