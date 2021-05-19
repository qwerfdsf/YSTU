from rest_framework import viewsets
from .serializers import(
    EducationSerializer,
    EducationListRetrieveSerializer
)
from ..models import Education


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    action_to_serializer = {
        "list": EducationListRetrieveSerializer,
        "retrieve": EducationListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class,
        )




