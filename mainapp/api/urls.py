from rest_framework import routers
from .views import EducationViewSet

routers = routers.SimpleRouter()
routers.register('profile/education', EducationViewSet, basename='education')

urlpatterns = []
urlpatterns += routers.urls