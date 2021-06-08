from django.contrib import admin
from .models import (
    Profile, Faculty, Events,
    Direction,
    Student,
    Group,
    Education,
    Specialization,
    Skills

)

admin.site.register(Profile)
admin.site.register(Direction)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Education)
admin.site.register(Specialization)
admin.site.register(Faculty)
admin.site.register(Events)
admin.site.register(Skills)