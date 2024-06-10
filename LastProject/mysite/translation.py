from modeltranslation.translator import translator, TranslationOptions
from .models import *


class ProfessorTranslationOptions(TranslationOptions):
    fields = ('user', )


translator.register(Professor, ProfessorTranslationOptions)


class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Faculty, FacultyTranslationOptions)


class StudentTranslationOptions(TranslationOptions):
    fields = ('user',)


translator.register(Student, StudentTranslationOptions)


class CourseTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Course, CourseTranslationOptions)


class CabinetTranslationOptions(TranslationOptions):
    fields = ('room_number', )


translator.register(Cabinet, CabinetTranslationOptions)


# class CabinetTranslationOptions(TranslationOptions):
#     fields = '__all__'
#
#
# translator.register(Cabinet, CabinetTranslationOptions)


class TimetableTranslationOptions(TranslationOptions):
    fields = ('course',)


translator.register(Timetable, TimetableTranslationOptions)


# class HomeworkTranslationOptions(TranslationOptions):
#     fields = '__all__'
#
#
# translator.register(Homework, HomeworkTranslationOptions)
#
#
# class Post_homeworkTranslationOptions(TranslationOptions):
#     fields = '__all__'
#
#
# translator.register(Post_homework, Post_homeworkTranslationOptions)
#
#
# class Post_courseTranslationOptions(TranslationOptions):
#     fields = '__all__'
#
#
# translator.register(Post_course, Post_courseTranslationOptions)
#
#
#
#
#
#
