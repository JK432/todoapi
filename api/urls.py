from .views import *
from rest_framework import routers
from django.urls import path, include

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'todo',ToDoViewSet,basename="todo")

urlpatterns=[
    path('', include(router.urls)),
]