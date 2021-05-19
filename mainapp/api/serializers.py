from rest_framework import serializers
from ..models import (
    Student, Profile,
    Group, Education,
    Specialization, Faculty,
    Direction, Events
)


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    faculty = FacultySerializer()
    direction = DirectionSerializer()
    events = EventsSerializer()

    class Meta:
        model = Specialization
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Student
        fields = ('surname', 'student_name', 'middlename', 'group')


class EducationListRetrieveSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    specialization = SpecializationSerializer()

    class Meta:
        model = Education
        fields = '__all__'
