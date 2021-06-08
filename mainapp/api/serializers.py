
from rest_framework import serializers
from ..models import (
    Student, Profile,
    Group, Education,
    Specialization, Faculty,
     Direction, Events, Skills
)


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.group_name')

    class Meta:
        model = Student
        fields = ('surname', 'student_name', 'middlename', 'group_name')


class SpecializationSerializer(serializers.ModelSerializer):
    profile = serializers.CharField(source='profile.profile_name')
    faculty = serializers.CharField(source='faculty.faculty_name')
    direction = serializers.CharField(source='direction.direction_name')

    class Meta:
        model = Specialization
        fields = ('profile', 'faculty', 'direction')


class EducationSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    specialization = SpecializationSerializer()

    class Meta:
        model = Education
        fields = ('student', 'specialization')



