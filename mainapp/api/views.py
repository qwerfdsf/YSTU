from rest_framework import viewsets
from .serializers import(
     SkillsSerializer,
    EducationSerializer,
    StudentSerializer
)
from ..models import Education, Student, Skills


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    action_to_serializer = {
        "list": EducationSerializer,
        "retrieve": EducationSerializer
    }


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    action_to_serializer = {
        "list": StudentSerializer,
        "retrieve": StudentSerializer
    }


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    action_to_serializer = {
        "list": SkillsSerializer,
        "retrieve": SkillsSerializer
    }

