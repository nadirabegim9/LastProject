from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add any additional fields here
    pass


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f'Professor - {self.user}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField()

    def __str__(self):
        return f'Student - {self.user}'


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    description = models.TextField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.code}'


class Cabinet(models.Model):
    room_number = models.IntegerField()
    building = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.room_number} - {self.building}'


class Timetable(models.Model):
    """Расписание"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    STATUS_CHOICES = (
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    )
    day_of_week = models.CharField(max_length=20, choices=STATUS_CHOICES, default='monday')

    def __str__(self):
        return f"{self.course} - {self.classroom}"


class Post_course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.course}"


class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return f'{self.course} - {self.title}'


class Post_homework(models.Model):
    assignment = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateTimeField()
    grade = models.IntegerField(null=True, blank=True)
    feedback = models.TextField()

    def __str__(self):
        return f'{self.assignment} - {self.student}'


# crud
# filter(depart, proffes(course))
# search(cou name, stud name, prof name)