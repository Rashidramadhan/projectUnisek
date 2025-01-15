from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('students', views.StudentViewSet)
router.register('courses', views.CourseViewSet)
router.register('universities', views.UniversityViewSet)
router.register('mentors', views.MentorViewSet)

urlpatterns = [  
    path('', include(router.urls)),
   
]
