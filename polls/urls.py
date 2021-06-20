from django.urls import path, include
from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register('question', views.QuestionViewSet)
router.register('choice', views.ChoiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
