from rest_framework import routers
from .views import EducationViewSet, SkillsViewSet

routers = routers.SimpleRouter()
routers.register('profile/education', EducationViewSet, basename='education')
routers.register('profile/skills', SkillsViewSet, basename='skills')
urlpatterns = []
urlpatterns += routers.urls