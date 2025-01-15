from django.db import models

# Create your models here.
class StudentModel(models.Model):
    student_username = models.CharField(max_length=10, null=True)
    full_names = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    home_address = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    college_date = models.CharField(max_length=100, null=True)
    college_considering = models.TextField(null=True)
    majoring_courses = models.TextField(null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    extra_data = models.TextField(null=True)

    class Meta:
        db_table = 'student'

class MentorModel(models.Model):
    mentor_username = models.CharField(max_length=20, null=True)
    full_names = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)#Address
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    area_specialisation = models.TextField(null=True)
    date_added = models.DateField(auto_now_add=True)
    added_by = models.CharField(max_length=100, null=True)
    extra_data = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'mentor'


class UniversityModel(models.Model):
    university_id = models.CharField(max_length=20, null=True)
    university_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    courses_offered = models.TextField(null=True)
    date_added = models.DateField(auto_now_add=True)
    added_by = models.CharField(max_length=100, null=True)
    extra_data = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'university'

    def __str__(self):
        return self.university_name


class CoursesModel(models.Model):
    course_id = models.CharField(max_length=100, null=True)  # Cource001
    university_name = models.ForeignKey(UniversityModel, on_delete=models.CASCADE, related_name='university')  
    course_name = models.CharField(max_length=100, null=True)  # BSc. Chemical Engineering
    duration = models.CharField(max_length=100, null=True)
    fee = models.CharField(max_length=100, null=True)
    date_added = models.DateField(auto_now_add=True)
    added_by = models.CharField(max_length=100, null=True)
    extra_data = models.TextField(max_length=100, null=True)

    class Meta:
        db_table = 'courses'

