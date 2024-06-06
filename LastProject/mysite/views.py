from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class FacultyViewSets(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', ]


class ProfessorViewSets(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', ]


class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', ]


class CourseViewSets(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['professor', ]
    search_fields = ['name', ]


class CabinetViewSets(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class TimetableViewSets(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


class Post_courseViewSets(viewsets.ModelViewSet):
    queryset = Post_course.objects.all()
    serializer_class = Post_courseSerializer


class HomeworkViewSets(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class Post_homeworkViewSets(viewsets.ModelViewSet):
    queryset = Post_homework.objects.all()
    serializer_class = Post_homeworkSerializer
