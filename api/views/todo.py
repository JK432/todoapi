from rest_framework.viewsets import ModelViewSet
from ..serializer import *
from ..model import *


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        queryset = ToDo.objects.all()
        return queryset
